"""hw.py  ejf,dhaval 2023-03-17
   inputs:
     orig/xxx.txt
     NO hwextra/xxx_hwextra.txt
   output: xxxhw.txt
"""
from __future__ import print_function
import re
import sys,codecs
# next parses key-value pairs coded as <key>val<key1>val1...

from parseheadline import parseheadline

class Hwmeta(object):
 # class variables for efficiency
 # The structure of the 'meta' line
 # Assume meta line within xxx.txt is a sequence of key-value pairs
 # coded as
 # <key>val
%if dictlo == 'mw':
 keysall_list = ['L','pc','k1','k2','h','e']  # standard order
%elif dictlo in ['harsa']:
 keysall_list = ['L','pc']
%else:
 keysall_list = ['L','pc','k1','k2','h']  # standard order
%endif
 # hom is optional
 keysneeded = set(keysall_list).difference(set(['h']))
 # significance of 'e' unclear. Ignore
 keysall = set(keysall_list)
 def __init__(self,line):
  line = line.rstrip('\r\n')
  d = parseheadline(line)
  # check for validity of keys
  keys = set(d.keys())
  if not(self.keysneeded.issubset(keys)):
   # error
   print("Hwmeta init error",line.encode('utf-8'))
   print("keysneeded=",self.keysneeded)
   print("keys=",keys)
   exit(1)
  self.d = d  
  # convert dictionary to object attributes (except for 'e' = extra)
  self.pc = d['pc']
  self.L = d['L']
  #self.key1 = d['k1']
  #self.key2 = d['k2']
  #self.h = None
  #if 'h' in d:
  # self.h = d['h']

def get_k1(s):
 parts = s.split('-')
 if len(parts) > 2:
  print('WARNING: more than one gender',s)
 return parts[0]

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into an Hwmeta object
  self.meta = Hwmeta(self.metaline)
  self.L = self.meta.L
  self.pc = self.meta.pc
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  self.keys = self.init_keys()  # array of headwords
  L = self.meta.L
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  
 def init_keys(self):
  a = []
  d = {}  # used to check duplicates
  for line in self.datalines:
   m = re.search(r'<k1>(.*?)<meanings>(.*?)$',line)
   if m == None:
    continue
   k1 = get_k1(m.group(1))
   meanings_str = m.group(2)
   meaning_items = meanings_str.split(',')
   meanings_k1 = [get_k1(item) for item in meaning_items]
   if k1 not in d:
     a.append(k1)
     d[k1] = True
   for k1m in meanings_k1:
    if k1m not in d:
     a.append(k1m)
     d[k1m] = True
  return a

def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs
  

def write_entries(entries,fileout):
 """ hwrecs is a list of dictionaries
   whose keys are a subset of the keys appearing in HWextra records
 """
 outarr = []
 for entry in entries:
  L = entry.L
  pc = entry.pc
  ln1 = entry.linenum1
  ln2 = entry.linenum2
  for key in entry.keys:
   k1 = key
   k2 = k1
   out = '<L>%s<pc>%s<k1>%s<k2>%s<ln1>%s<ln2>%s' % (L,pc,k1,k2,ln1,ln2)
   outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out + '\n')

 print(len(outarr),"lines written to",fileout)

if __name__ == "__main__":
 filedig = sys.argv[1]
 fileextra = sys.argv[2]
 fileout = sys.argv[3]
 print("BEGIN hw.py init_entries")
 entries = init_entries(filedig)
 print("END hw.py init_entries\n")
 # generate list of key-value
 #print("BEGIN hwrecs_normal")
 #hwrecs_normal = init_hwrecs_normal(entries)
 #hwrecs_normal = [entry_to_hwrec(entry) for entry in entries]
 #print("END hwrecs_normal\n")
 print ("BEGIN write_entries")
 write_entries(entries,fileout)
 print("END write_entries")
