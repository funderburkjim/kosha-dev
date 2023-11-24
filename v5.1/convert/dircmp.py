# coding=utf-8
""" dircmp.py
 
"""
from __future__ import print_function
import myfilecmp as filecmp
import sys,re,codecs
# import os.path,time
# from shutil import copyfile

outarr_keys = {'diff':3,
               'Only in':4,
               'Identical files :':2,
               'Differing files :':2,
               'Common subdirectories :':2}

def check_outarr_keys(outarr):
 nkey = 0 # number of keys that occur
 nprob = 0 # number of 
 for out in outarr:
  key = out[0]
  lout = len(out)
  if key not in outarr_keys:
   print('ERROR 1: key not found\n',out)
   exit(1)
  outlen = outarr_keys[key]
  if outlen != lout:
   print('ERROR 2: key wrong length. Expected %s, got %s' % (outlen,lout))
   exit(1)
 print('check_outarr_keys: All as expected')

def filter_outarr_diff(out,dir1,dir1a,dir2,dir2a):
 out1 = []
 out1.append(out[0]) # diff
 d1 = out[1]
 d1a = d1.replace(dir1,dir1a)
 d1a = d1a.replace('\\','/')
 out1.append(d1a)
 d2 = out[2]
 d2a = d2.replace(dir2,dir2a)
 d2a = d2a.replace('\\','/')
 out1.append(d2a)
 return out1

def fileskip(arr):
 # arr is list of filenames.
 ans = []
 for x in arr:
  if x.startswith('temp'):
   pass
  elif x.endswith('~'):
   pass # Emacs backup file
  elif x.startswith('_'):
   pass # e.g. __pycache__
  else:
   ans.append(x)
 return ans

def filter_outarr_only(out,dir1,dir1a,dir2,dir2a):
 out1 = []
 out1.append(out[0]) # Only in
 d1 = out[1]
 d1a = d1.replace(dir1,dir1a)
 d1b = d1a.replace(dir2,dir2a)
 d1b = d1b.replace('\\','/')
 out1.append(d1b)
 assert out[2] == ':'
 out1.append(out[2])  # ':'
 filelist = out[3]  # an array of strings
 out1a = fileskip(filelist)
 # change '\' to '/' in the filenames. Peculiar to windows os?
 out1b = [x.replace('\\','/') for x in out1a]
 out1.append(out1b)
 return out1
 
def filter_outarr(outarr,dir1,dir1a,dir2,dir2a):
 ans = []
 for out in outarr:
  if out[0] == 'diff':
   out1 = filter_outarr_diff(out,dir1,dir1a,dir2,dir2a)
   ans.append(out1)
  elif out[0] == 'Only in':
   out1 = filter_outarr_only(out,dir1,dir1a,dir2,dir2a)
   ans.append(out1)
  else:
   ans.append(out)
 return ans

def adjust_outarr1(outarr,dir1,dir1a,dir2,dir2a):
 check_outarr_keys(outarr)
 outarr1 = filter_outarr(outarr,dir1,dir1a,dir2,dir2a)
 ans = [] # list of strings
 for iout,out in enumerate(outarr1):
  outa = []
  for a in out:
   typea = type(a)
   if typea == str:
    outa.append(a)
   elif typea == list:
    b = ', '.join(a)
    outa.append(b)
   else:
    print('unknown type %s in\n' % a, out)
    exit(1)
  outstr = ' '.join(outa)
  key = outa[0]
  if key == 'diff':
   if iout != 0:
    ans.append('')
   temp = re.findall('/',outa[1])
   indent = len(temp)
   indentstr = ' '*indent
  outstr = indentstr + outstr
  ans.append(outstr)
 return ans

def adjust_outarr1_v0(outarr,dir1,dir1a,dir2,dir2a):
 check_outarr_keys(outarr)
 outarr1 = filter_outarr(outarr,dir1,dir1a,dir2,dir2a)
 ans = [] # list of strings
 for out in outarr1:
  outa = []
  for a in out:
   typea = type(a)
   if typea == str:
    outa.append(a)
   elif typea == list:
    b = ', '.join(a)
    outa.append(b)
   else:
    print('unknown type %s in\n' % a, out)
    exit(1)
  outstr = ' '.join(outa)
  ans.append(outstr)
 return ans

def write_outarr(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"records written to",fileout)
 
if __name__=="__main__":
 dir1,dir1a = sys.argv[1].split(',')  # first directory
 dir2,dir2a = sys.argv[2].split(',')  # second directory
 fileout = sys.argv[3] # comparison info
 dcmp = filecmp.dircmp(dir1, dir2)
 dcmp.report_full_closure()
 outarr = dcmp.outarr
 outarr1 = adjust_outarr1(outarr,dir1,dir1a,dir2,dir2a)
 write_outarr(fileout,outarr1)

  
        
 
