# coding=utf-8
""" bing_are_dir_trees_equal.py

"""
from __future__ import print_function
import filecmp
import sys,re,codecs
import os.path,time
from shutil import copyfile

def are_dir_trees_equal(dir1, dir2):
 dirs_cmp = filecmp.dircmp(dir1, dir2)
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

if __name__=="__main__":
 dir1 = sys.argv[1] # first directory
 dir2 = sys.argv[2] # second directory
 ans = are_dir_trees_equal(dir1, dir2)
 print('ans=%s' % ans)
 
 
