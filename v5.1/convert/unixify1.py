"""unixify1.py  Convert all line endings to '\n'
  write results to output file, if outputfile provided as an argument.
   03-18-2017
"""
import sys,re,codecs

if __name__ == "__main__":
 filename = sys.argv[1]
 if len(sys.argv) == 3:
  fileout = sys.argv[2]
 else:
  fileout = filename # rewrite input file
 with codecs.open(filename,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')

