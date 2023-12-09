# coding=utf-8
""" make_xml.py
 Reads/Writes utf-8
 11-14-2020. remove .encode('utf-8') .  For python3 coding
"""
from __future__ import print_function
import xml.etree.ElementTree as ET
import sys, re,codecs
from hwparse import init_hwrecs,HW
xmlroot = HW.dictcode

def dig_to_xml_specific(x):
 """ no changes particular to digitization"""
 return x
 # There are a couple entries with an <H> element.
 # Just remove these lines
 if x.startswith('<H>'):
  print("REMOVING <H> LINE",x)
  return ''
 x = re.sub(r'<P>','<div n="P">',x) # 2322 cases
 #if '<g></g>' in x: # once only. Already converted in stc.txt
 # x = x.replace('<g></g>','<lang n="greek"></lang>')
 #x = re.sub(r'<Picture>','<div n="Picture">',x) # 71 cases
 # markup like <C1>x1<C2>x2...  indicates tabular data in vcp.
 #x = re.sub(r'<C([0-9]+)>',r'<C n="\1"/>',x)
 # change '--' to mdash
 x = x.replace('--',u'—')  #597 cases
 #{^X^}  superscript
 x = re.sub(r'{\^(.*?)\^}',r'<sup>\1</sup>',x)
 return x


def dig_to_xml_general(x):
 return x
 """ These changes likely apply to ALL digitizations"""
 # xml requires that an ampersand be represented by &amp; entity
 x = x.replace('&','&amp;')
 # remove broken bar.  In xxx.txt, this usu. indicates a headword end
 x = x.replace(u'¦',' ')
 # bold, italic, and Sanskrit markup converted to xml forms.
 x = re.sub(r'{@','<b>',x)
 x = re.sub(r'@}','</b>',x)
 x = re.sub(r'{%','<i>',x)
 x = re.sub(r'%}','</i>',x)
 x = re.sub(r'{#','<s>',x)
 x = re.sub(r'#}','</s>',x)
 return x

def dig_to_xml(xin):
 x = xin
 x = dig_to_xml_general(x)
 x = dig_to_xml_specific(x)
 return x

def dbgout(dbg,s):
 if not dbg:
  return
 filedbg = "make_xml_dbg.txt"
 fout = codecs.open(filedbhg,"a","utf-8")
 fout.write(s + '\n')
 fout.close()

def close_divs(line):
 """ line is the full xml record, but the <div> elements have not been
  closed.  Don't close empty div tags.
 """
 divregex = r'<div[^>]*?[^/]>'
 if not re.search(divregex,line):
  # no divs to close
  return line
 ans = [] # strings parts of data
 idx0 = 0
 # div can have attribute
 for m in re.finditer(divregex,line):
   idx1=m.start()
   idx2 = m.end()
   line1 = line[idx0:idx1] # text preceding this div
   ans.append(line1)
   if idx0 != 0:
    # close the previous div
    ans.append('</div>')
   # include this div
   linediv = line[idx1:idx2]
   ans.append(linediv)
   idx0 = idx2 # reset for next iteration
 # construct string for all text in line upto position idx0
 new = ''.join(ans)
 # The last div will not be closed
 rest = line[idx0:]
 # We can assume that rest contains
 # <type>*</type></body> -> </div><type>*</type></body>
 # (no type)</body> -> </div></body>
 if re.search(r'(<type>.*?</type>)</body>',rest):
  newrest = re.sub(r'<type>',r'</div><type>',rest)
 elif re.search(r'</body>',rest):
  newrest = re.sub(r'</body>','</div></body>',rest)
 else:
  raise ValueError("close_divs_error: %s"%line)
 newline = new + newrest
 return newline

def construct_xmlhead(hwrec):
 key2 = hwrec.k2
 key1 = hwrec.k1
 hom = hwrec.h
 if hom == None:
  # no homonym
  h = "<key1>%s</key1><key2>%s</key2>" % (key1,key2)
 else:
  h = "<key1>%s</key1><key2>%s</key2><hom>%s</hom>" % (key1,key2,hom)
 return h

def construct_xmltail(hwrec):
 L = hwrec.L
 pagecol = hwrec.pc
 tail = "<L>%s</L><pc>%s</pc>" % (L,pagecol)
 if hwrec.type == None:
  # normal
  return tail
 # otherwise, also <hwtype n="type" ref="LP"
 hwtype = '<hwtype n="%s" ref="%s"/>' %(hwrec.type,hwrec.LP)
 tail = tail + hwtype
 return tail

def body_alt(bodylines,hwrec):
 """
  insert an extra body line at the top.
 """
 hwtype = hwrec.type
 assert hwtype in ['alt','sub', 'fem', 'neu'],"body_alt error: %s"%hwtype
 LP = hwrec.LP  # L-number of parent
 hwrecP = HW.Ldict[LP]
 key1P = hwrecP.k1
 key1 = hwrec.k1
 templates = {
  'alt':'<alt>%s is an alternate of %s.</alt>',
  'sub':'<alt>%s is a sub-headword of %s.</alt>',
  'fem':'<alt>%s is feminine form of %s.</alt>',
  'neu':'<alt>%s is neuter form of %s.</alt>',
 }
 if HW.Sanskrit:
  # prepare for conversion from slp1 to user choice
  key1P = '<s>%s</s>' %key1P
  key1 = '<s>%s</s>' %key1
 template = templates[hwtype]
 extraline = template %(key1,key1P)
 # insert extraline at the front
 return [extraline]+bodylines


def construct_xmlstring_2_helper(syns):
 # syns = a,b,c ...
 # each syn is either k1 or k1-gender
 # return list of k1s.
 parts = syns.split(',')
 synk1s = []
 for part in parts:
  # part is either x-y or x
  subparts = part.split('-')
  k1 = subparts[0]
  synk1s.append(k1)
 return synk1s

def construct_xmlstring_2(datalines,hwrec):
 # for koshas like abch
 dbg = False
 datalines1 = []
 # 1. h (head)
 h = construct_xmlhead(hwrec)
 dbgout(dbg,"head: %s" % h)
 #2. construct tail
 tail = construct_xmltail(hwrec)
 dbgout(dbg,"tail: %s" % tail)
 #3. construct body
 """ 
Sample entr
<L>1233<pc>39
<info kvvv="<s>tiryakkARqaH</s>, <s>pfTvIkAyaH</s>"/>
<eid>3076<syns><s>SilA-strI,aDodAru-klI</s>
<eid>3077<syns><s>nAsA-strI,urDvadAru-klI</s>
<s>stamBAdeH syAdaDodArO SilA nAsorDvadAruRi .. 1008 ..</s>
<LEND>
constructed html
 """
 # partition datalines into infos hwdetails and entrydetails
 infos = []
 hwdetails = []
 entrydetails = []
 for i,x0 in enumerate(datalines):
  # remove <s> markup
  x = re.sub(r'</?s>','',x0)
  if x.startswith('<info'):
   infos.append(x)
  elif x.startswith('<'):
   hwdetails.append(x)
  else:
   entrydetails.append(x)
 # add formatting to entrydetails
 entrydetails1 = []
 for i,x in enumerate(entrydetails):
  y = '<s>%s</s>' % x
  z = '<entrydetail>%s</entrydetail>' % y
  entrydetails1.append(z)
 entrydetails_str = ''.join(entrydetails1)
                                 
 # add formatting to hwdetails
 hwdetails1 = []
 for i,x in enumerate(hwdetails):
  yerr = '<div> %s -->' % x
  m = re.search(r'<eid>(.*?)<syns>(.*?)$',x)
  if m == None:  # error condition
   y = '<!-- ERROR wrong form: %s -->' %x
   hwdetails1.append(y)
   continue
  eid = m.group(1)
  syns = m.group(2)
  k1 = hwrec.k1
  if k1 not in construct_xmlstring_2_helper(syns):
   continue
  y1 = '<eid>%s</eid>' % eid
  y2 = '<syns><s>%s</s></syns>' % syns
  y = '%s%s' % (y1,y2)
  z = '<hwdetail>%s</hwdetail>' % y
  hwdetails1.append(z)
 # add formatting to info(s)
 # Assume exactly 1 info line
 info = infos[0]
 m = re.search(r'<info kvvv="(.*?)"/>',info)
 if m != None:
  kvvv_val = m.group(1) # value of kvvv
  info_str = "<s>%s</s>" % kvvv_val
 # string form
 hwdetails_str = ''.join(hwdetails1)
 # construct body0, by combining hwdetails and entrydetails
 bodya = '<hwdetails>' + hwdetails_str + '</hwdetails>'
 bodyb = '<entrydetails>' + entrydetails_str +'</entrydetails>'
 bodyc = '<div>%s</div>' % info_str  # put it into a div
 body = bodyc + bodya + bodyb
 
 dbgout(dbg,"body: %s" % body)
 #4. construct result
 data = "<H1><h>%s</h><body>%s</body><tail>%s</tail></H1>" % (h,body,tail)
 #5. Close the <div> elements
 # data = close_divs(data)
 return data
def xml_header(xmlroot):
 # write header lines
 text = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE %s SYSTEM "%s.dtd">
<!-- Copyright Universitat Koln 2013 -->
<%s>
""" % (xmlroot,xmlroot,xmlroot)
 lines = text.splitlines()
 lines = [x.strip() for x in lines if x.strip()!='']
 return lines

def get_datalines1(hw,datalines):
 # used for abch
 ans= []
 for line in datalines:
  m = re.search(r'<k1>(.*?)<meanings>(.*?)$',line)
  if m == None: # keep verselines
   ans.append(line)
   continue
  # keep line only when hw matches one of the headwords of line
  k1 = get_k1(m.group(1))
  meanings_str = m.group(2)
  meaning_items = meanings_str.split(',')
  meanings_k1 = [get_k1(item) for item in meaning_items]
  allhws = [k1] + meanings_k1
  if hw in allhws:
   ans.append(line)
  # otherwise, the line is not kept.
 return ans

def get_datalines(hwrec,inlines):
 # for structure of hwrec, refer to hwparse.py
 n1 = int(hwrec.ln1)
 n2 = int(hwrec.ln2)
 # By construction, n1 is the meta line, and n2 is the <lend> line of
 # this entry in xxx.txt.
 # For our purposes, we do not need this first and last line
 n1 = n1 + 1
 n2 = n2 - 1
 # Next, we make indexes into the inlines array, which are 0-based
 # whereas n1 and n2 are 1-based
 idx1 = n1 - 1
 idx2 = n2 - 1
 datalines = inlines[idx1:idx2+1]
 # restrict further to the hwdetails that mention this hw
 hw = hwrec.k1
 datalines = get_datalines1(hw,datalines)
 return datalines

def make_xml(filedig,filehw,fileout):
 # slurp txt file into list of lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
    inlines = [line.rstrip('\r\n') for line in f]
 # parse xxxhw.txt
 hwrecs = init_hwrecs(filehw)
 # open output xml file
 fout = codecs.open(fileout,'w','utf-8')
 nout = 0  # count of lines written to fout
 # generate xml header lines
 lines = xml_header(xmlroot)
 for line in lines:
  fout.write(line + '\n')
  nout = nout + 1
 # process hwrecs records one at a time and generate output
 nerr = 0
 for ihwrec,hwrec in enumerate(hwrecs):
  if ihwrec > 1000000: # 12
   print("debug stopping")
   break
  datalines = get_datalines(hwrec,inlines)
  # construct output
  # using abch form
  xmlstring = construct_xmlstring_2(datalines,hwrec)
  # data is a string, which should be well-formed xml
  # try parsing this string to verify well-formed.
  try:
   root = ET.fromstring(xmlstring)
  except:
   # 01-09-2021. Remove conditional err messaging
   # since some Python versions (e.g. 2.7.5) give false occasions
   nerr = nerr + 1
   # For debugging, change False to True
   if False:
    outarr = []
    out = "<!-- xml error #%s: L = %s, hw = %s-->" %(nerr,hwrec.L,hwrec.k1)
    outarr.append(out)
    outarr.append("datalines = ")
    outarr = outarr + datalines
    outarr.append("xmlstring=")
    outarr.append(xmlstring)
    outarr.append('')
    for out in outarr:
     print(out)
    #exit(1) continue
  # write output
  fout.write(xmlstring + '\n')
  nout = nout + 1

 # write closing line for xml file.
 out = "</%s>\n" % xmlroot
 fout.write(out)
 fout.close()
 if (nerr == 0):
  print("All records parsed by ET")
 else:
  print("WARNING: make_xml.py:",nerr,"records records not parsed by ET")
if __name__=="__main__":
 print('make_xml.py BEGINS !!!!!')
 filein = sys.argv[1] # xxx.txt
 # filein1 = xxxhw.txt for dictlo = mw; for other dictlo, filein1 = xxxhw2.txt
 filein1 = sys.argv[2]
 fileout = sys.argv[3] # xxx.xml
 make_xml(filein,filein1,fileout)
 print('make_xml.py ENDS !!!!!')
 
