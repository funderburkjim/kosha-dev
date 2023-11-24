# coding=utf-8
""" bing_are_dir_trees_equal1.py
 Ref: dircomparison.py at stackoverflow
 https://stackoverflow.com/questions/31754449/diff-two-folders-using-python-having-same-set-of-subfolders-and-file-structure
"""
from __future__ import print_function
import filecmp
import sys,re,codecs
import os.path,time
from shutil import copyfile

def are_dir_trees_equal(dir1, dir2):
 if len(dirs_cmp.left_only) > 0 or len(dirs_cmp.right_only) > 0 or len(dirs_cmp.funny_files) > 0:
  return False
 (_, mismatch, errors) = filecmp.cmpfiles(dir1, dir2, dirs_cmp.common_files, shallow=False)
 if len(mismatch) > 0 or len(errors) > 0:
  return False
 for common_dir in dirs_cmp.common_dirs:
  new_dir1 = os.path.join(dir1, common_dir)
  new_dir2 = os.path.join(dir2, common_dir)
  if not are_dir_trees_equal(new_dir1, new_dir2):
   return False
 return True

def diffs_found(dcmp):
 #print('----------------------------------------------------------')
 if len(dcmp.left_only) > 0:
  print(dcmp.report_full_closure())
  return True
 elif len(dcmp.right_only) > 0:
  print(dcmp.report_full_closure())
  return True
 else:
  for sub_dcmp in dcmp.subdirs.values():
   if diffs_found(sub_dcmp):
     return True
 return False

if __name__=="__main__":
 dir1 = sys.argv[1] # first directory
 dir2 = sys.argv[2] # second directory
 #fileout = sys.argv[3] # comparison info
 #ignore = filecmp.DEFAULT_IGNORES.append('temp*')
 #dcmp = filecmp.dircmp(dir1, dir2,ignore  = ignore)
 dcmp = filecmp.dircmp(dir1, dir2)
 flag = diffs_found(dcmp)
 if flag:
  print("DIFFS FOUND")
 else:
  print("NO DIFFS FOUND")

        
 
