#-*- coding:utf-8 -*-
"""additional info added to abch
"""
from __future__ import print_function
import sys, re,codecs

def info_1(lines):
 """
  Re 'entrydetails' -- 
 """
 newlines = [] # returned
 nchg = 0 # number of lines changed
 metaline = None
 prev_verse = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   newlines.append(line)
  elif line.startswith('<LEND>'):
   metaline = None
   newlines.append(line)
   # check that previous line ends with '.</s>'
   if not lines[iline-1].endswith('.</s>'):
    print('WARNING',lines[iline-1])
  elif metaline == None:
   # Not in an entry
   newlines.append(line)
   # We are in an entry
  elif not line.startswith('<s>'):
   newlines.append(line)
  else:
   # line starts with '<s>' - an entrydetail line
   m = re.search(r'[.][.] ([0-9]+) [.][.]</s>$',line)
   if m != None:
    prev_verse = int(m.group(1))
    newlines.append(line)
   else:
    ## partial verse
    nextline = lines[iline + 1]
    if nextline.startswith('<LEND>'):
     # the last line of entry
     next_verse = prev_verse + 1
     end = ' .</s>'
     if not line.endswith(end):
      # multi-line verse, e.g. at <L>48
      newlines.append
     else:
      newend = ' (%s) .</s>' % next_verse
      newline = line.replace(end, newend)
      newlines.append(newline)
      nchg = nchg + 1
    else:
     newlines.append(line)
 print(nchg,"changes in info_1")
 return newlines

def info_2(lines):
 """
  page break in entry.  
  This does not work properly to generate a new 'page' link.
  Must coordinate with make_xml.py.
  Currently, it just introduces a blank line
 """
 newlines = [] # returned
 nchg = 0 # number of lines changed
 metaline = None
 prev_verse = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   newlines.append(line)
  elif line.startswith('<LEND>'):
   metaline = None
   newlines.append(line)
  elif metaline == None:
   # Not in an entry
   newlines.append(line)
  elif line.startswith(';'):
   # in an entry
   # 15 lines in entries are of form ;p{nnnn}  (page break)
   # print('check meta',iline+1,line) 
   m = re.search(r'^;p{([0-9]+)}$',line)
   if m == None:
    print('info_2 unexpected',line)
    newlines.append(line)
   else:
    ipage = int(m.group(1))
    #newline = '' # '<pb>%s</pb>' % ipage  Blank line is incomplete solution
    newline = line # no change in this revision
    newlines.append(newline)
    nchg = nchg + 1
  else:
   # other kinds of lines
   newlines.append(line)
 print(nchg,"changes in info_2")
 return newlines

if __name__=="__main__": 
 filein = sys.argv[1] #  xxx.txt input file
 fileout = sys.argv[2] # result of conversion
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 newlines = info_1(lines)
 newlines = info_2(newlines) # page break - not implemented
 with codecs.open(fileout,'w','utf-8') as f:
  for line in newlines:
   f.write(line+'\n')
