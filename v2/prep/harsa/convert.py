#-*- coding:utf-8 -*-
"""convert.py   convert files from other transcodings to slp1
   assume format of ankh1.txt (see readme)
"""
from __future__ import print_function
import sys, re,codecs
import transcoder
transcoder.transcoder_set_dir('transcoder')

def convert(line,tranin,tranout,iline):
 if line.startswith(';'):
  return line # comment
 if re.search(r'^ *$',line): # empty line
  return line
 if line.startswith(('<L>','<LEND>')):
  return line
 # transcode everything except xml-style tags of form <X>
 dbg = False
 parts = re.split(r'(<[^>]+>)',line)
 if dbg:
  print('OLD: ',line)
  print('line=',line)
  print('parts=',parts)
 newparts = []
 for part in parts:
  if part.startswith('<'):
   ## tag not changed
   newpart = part
  else:
   newpart = transcoder.transcoder_processString(part,tranin,tranout)
  newparts.append(newpart)
  if dbg:
   print('debug:')
   print('%s   ==>  %s' %(part,newpart))
 newline = ''.join(newparts)
 if dbg:
  print('NEW: ',newline)
  print('dbg exit')
  exit(1)
 return newline

def parse_option(option):
 # option = deva,slp1  or slp1,deva
 options = ['deva,slp1' , 'slp1,deva']
 if option not in options:
  print('convert option error',option)
  print('Allowed options = ',' OR ' . join(options))
  exit(1)
 tranin,tranout = option.split(',')
 return tranin,tranout
if __name__=="__main__": 
 option = sys.argv[1]
 tranin,tranout = parse_option(option)
 filein = sys.argv[2] #  xxx.txt file to be converted
 fileout = sys.argv[3] # result of conversion
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 with codecs.open(fileout,'w','utf-8') as f:
  for iline,line in enumerate(lines):
   out = convert(line,tranin,tranout,iline)
   f.write(out+'\n')
