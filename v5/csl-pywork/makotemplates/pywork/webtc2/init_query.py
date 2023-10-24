# coding=utf-8
""" init_query.py 
 Reads/Writes utf-8
 Jul 6, 2018:  A conversion to Python of init_query.php.
 Python2 syntax.
 init_query.php was not properly handling extended ascii characters.
// create query_dump.txt from xml file (generic)
// modified to included embedded sanskrit, which is converted to slp
 Mar 21, 2023  sort xml records by key1
"""
from __future__ import print_function
import sys, re,codecs

def sort_lines(lines):
 slp_from = "aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh"
 slp_to =   "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw"
 slp_from_to = str.maketrans(slp_from,slp_to)
 # filter, and generate sortkey
 rows = []
 for line in lines:
  if not line.startswith('<H'):
   # skip othere xml lines
   continue
  m = re.search(r'<key1>(.*?)</key1>.*<L>(.*?)</L>',line)
  if not m:
   print('ERROR: Could not find key1,lnum from line: %s' %line)
   exit(1)
  key1 = m.group(1)
  lnum = m.group(2)
  keysort = key1.translate(slp_from_to)  
  row = (keysort,key1,lnum,line)
  rows.append(row)
 # sort the rows
 rows1 = sorted(rows,key = lambda row: row[0])
 if False: # dbg print the sorted records
  fileout = 'temp_sqlite.txt'
  print('debug written to',fileout)
  with codecs.open(fileout,"w","utf-8") as f:
   for irow,row in enumerate(rows1):
    if (irow in [0,1]):
     f.write('%s %s %s %s\n' % row)
    else:
     f.write('%s %s %s\n' %(irow,row[0],row[1]))
 # return the sorted lines   
 newlines = [row[3] for row in rows1]
 return newlines

def make(filein,fileout):
 fpout = codecs.open(fileout,"w","utf-8")

 n=0;
 prevkey='';
 lnum1=0;
 nfound=0;
 nfound1=0;
 prevkey="";
 key='';
 keydata="";

 # 03-21-2023  sort the lines of input xml file
 # compare pywork/sqlite/sqlite.py
 with codecs.open(filein,"r","utf-8") as f:
  lines = [line.rstrip('\r\n') for line in f]
 lines_sorted = sort_lines(lines)
   
 for line in lines_sorted:
  line = line.rstrip('\r\n')

  m = (re.search(r'^<H.*?<key1>(.*?)</key1>.*<body>(.*?)</body>.*<L.*?>(.*?)</L>',line))
  if m:
   n = n + 1
   key=m.group(1)
   body = m.group(2)
   L=m.group(3)
   data1 = query_line(body)
   data2 = query_sanskrit(body)
   #data2 = "" # currently, no good way to distinguish Sanskrit words.
   ## if prevkey is empty, start a new keydata
   ## else if a new key, output keydata
   ## else append data1 to keydata
   if (prevkey == "") :
     prevkey = key
     keydata = data1
     keysanskrit = data2
   elif (prevkey == key):
     keydata += " :: %s" % data1
     keysanskrit += " :: %s" % data2
   else:
     fpout.write('%s :: %s\t%s\n' %(prevkey,keysanskrit,keydata))
     nfound1 = nfound1 + 1
     prevkey = key
     keydata = data1
     keysanskrit = data2

 # print last one
 fpout.write('%s :: %s\t%s\n' %(prevkey,keysanskrit,keydata))
 fpout.write("prevkey :: keysanskrit\tkeydata\n")
 fpout.close()

 print(n,"records read from",filein)
 print(nfound1,"records written to",fileout)

def query_line(x):
 # see construction in make_xml.php for some details

 # (b) English can appear in italics
 #x = preg_replace('|\{%.*?%\}|','',x)
 #x = preg_replace('|\{@.*?@\}|','',x)

 # (c) Remove markup
 x =re.sub(r'<s>.*?</s>','',x) # remove embedded SLP sanskrit
 x = re.sub('<.*?>',' ',x)
 #x = preg_replace('|\{#.*?#\}|','',x) # A few sanskrit letters coded as HK
 

 # (d) Remove punctuation
 x = re.sub('\[Page.*?\]','',x)
 x = re.sub('[~_;., ?()\[\]]+',' ',x)
 # (e) downcase
 x = x.lower()
 
 # (f) replace AS codes (remove the number)
 x = re.sub("[0-9]","",x)
 return x

def query_sanskrit(x):
 sanwords = []
 # Get all the <s>x</s> words
 # The subroutine modifies sanwords
 parts = re.split(r'(<s>.*?</s>)',x)
 for part in parts:
  m = re.search('^<s>(.*?)</s>$',part)
  if m:
   subpart = m.group(1)
   subwords = query_sanskrit_helper1(subpart)
   sanwords = sanwords + subwords
 ans = ' '.join(sanwords)
 return ans

def query_sanskrit_helper1(s):
 # remove xml markup
 s = re.sub(r'<([^> ]*).*?>.*?</\1>',' ',s)
 s = re.sub('<.*?>',' ',s)
 # remove extended ascii, which is coded as html entity: &...;
 #s = re.sub('|&.*?;|',' ',s)
 # remove slp accent chars, if present
 s = re.sub(r'[/\\~^]','',s)
 words = re.split("[^a-zA-Z|']",s)
 return words


if __name__=="__main__":
 filein = sys.argv[1] # xxx.xml
 fileout = sys.argv[2] # query_dump
 make(filein,fileout)
