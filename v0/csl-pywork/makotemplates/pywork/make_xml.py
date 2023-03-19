# coding=utf-8
""" make_xml.py
 Reads/Writes utf-8
 applies only to harsa dictionary
"""
from __future__ import print_function
import xml.etree.ElementTree as ET
import sys, re,codecs
from hwparse import init_hwrecs,HW
xmlroot = HW.dictcode

def dig_to_xml_specific(x):
 """ changes particular to digitization"""  
 return x

def dig_to_xml_general(x):
 return x
 """ These changes likely apply to ALL digitizations"""
 # xml requires that an ampersand be represented by &amp; entity
 x = x.replace('&','&amp;')
 # remove broken bar.  In xxx.txt, this usu. indicates a headword end
 x = x.replace(u'¦',' ')
 # bold, italic, and Sanskrit markup converted to xml forms.
%if dictlo in ['ben','ccs','mci','stc','bhs','gra','pe','gst','ieg','mwe','pgn','pui','vei','pd','mw72','snp','bor','krm','inm','skd','bop','vcp']:
 # These are not applicable to vcp, but do no harm
%endif
 return x

def dig_to_xml(xin):
 x = xin
 x = dig_to_xml_general(x)
 x = dig_to_xml_specific(x)
 return x

def dbgout(dbg,s):
 if not dbg:
  return
 filedbg = "temp_make_xml_dbg.txt"
 fout = codecs.open(filedbg,"a","utf-8")
 fout.write(s + '\n')
 fout.close()
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

def construct_xmlstring(datalines,hwrec):
 dbg = False
 datalines1 = []
 # 1. h (head)
 h = construct_xmlhead(hwrec)
 dbgout(dbg,"head: %s" % h)
 #2. construct tail
 tail = construct_xmltail(hwrec)
 dbgout(dbg,"tail: %s" % tail)
 #3. construct body
 """ sample of datalines
<k1>kawaka-klI<meanings>kaRWaka,sEnya,parvatanitamba
<k1>kaRwaka-klI<meanings>romaharza,sUcyagra,kzudravErin
kawakaM kaRWake sEnye nitambe parvatasya ca .
kaRwakaM romaharze syAt sUcyagre kzudravEriRi .. 3 ..

<H1><h><key1>kawaka</key1><key2>kawaka</key2></h>
 <body>
<lb/><s>kawaka-klI</s> meanings <s>kaRWaka,sEnya,parvatanitamba</s> 
<lb/><s>kaRwaka-klI</s> meanings <s>romaharza,sUcyagra,kzudravErin</s> 
<lb/><s>kawakaM kaRWake sEnye nitambe parvatasya ca .</s> 
<lb/><s>kaRwakaM romaharze syAt sUcyagre kzudravEriRi .. 3 ..</s>
</body>
<tail><L>3</L><pc>140</pc></tail></H1>
 """
 # paratition datalines into hwdetails and entrydetails
 hwdetails = []
 entrydetails = []
 for i,x in enumerate(datalines):
  if x.startswith('<'):
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
  m = re.search(r'<k1>(.*?)<meanings>(.*?)$',x)
  if m == None:  # error condition
   y = '<!-- ERROR wrong form: %s -->' %x
   hwdetails1.append(y)
  else:
   hw = m.group(1)
   meaning = m.group(2)
   y1 = '<hw><s>%s</s></hw>' % hw
   y2 = '<meaning><s>%s</s></meaning>' % meaning
   y = '%s%s' % (y1,y2)
   z = '<hwdetail>%s</hwdetail>' % y
   hwdetails1.append(z)
 # string form
 hwdetails_str = ''.join(hwdetails1)
 # construct body0, by combining hwdetails and entrydetails
 bodya = '<hwdetails>' + hwdetails_str + '</hwdetails>'
 bodyb = '<entrydetails>' + entrydetails_str +'</entrydetails>'
 body = bodya + bodyb
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
  if ihwrec > 1000000: # dbg
   print("debug stopping")
   break
  datalines = get_datalines(hwrec,inlines)
  # construct output
  xmlstring = construct_xmlstring(datalines,hwrec)
  # xmlstring is a string, which should be well-formed xml
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
 filein1 = sys.argv[2] #xxxhw2.txt
 fileout = sys.argv[3] # xxx.xml
 make_xml(filein,filein1,fileout)
