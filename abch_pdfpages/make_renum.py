import sys,re,codecs
import os



def write_script(fileout,frontnames,bodynames):
 outarr = []
 fromdir = 'archive_pages'
 todir = 'pdfpages'
 outarr.append('rm -r %s' % todir)
 outarr.append('mkdir %s' % todir)
 allnames = frontnames + bodynames
 for infilename,outfilename,outpage in allnames:
  frompath = '%s/%s' % (fromdir,infilename)
  topath = '%s/%s' % (todir,outfilename)
  outarr.append("cp '%s' %s" % (frompath,topath))
 outarr.append('echo "copy %s files from %s to %s"' %(len(allnames),fromdir,todir))
 #  
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"lines written to script",fileout)

def write_pdffiles(fileout,frontnames,bodynames):
 outarr = []
 #fromdir = 'archive_pages'
 #todir = 'pdfpages'
 #outarr.append('rm -r %s' % todir)
 #outarr.append('mkdir %s' % todir)
 allnames = frontnames + bodynames
 for infilename,outfilename,outpage in allnames:
  outarr.append('%s:%s' % (outpage,outfilename))
 #  
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"lines written to",fileout)

def frontmap():
 ans = [] 
 nout = 0
 for archivepage in range(135,149):  # 135,...,148
  infilename = 'archive %s.pdf' % archivepage
  nout = nout + 1
  outfilename = 'f%02d.pdf' % nout
  outpage = 'f%02d' % nout
  ans.append((infilename,outfilename,outpage))
 return ans

def bodymap():
 ans = [] 
 nout = 4
 for archivepage in range(149,203): # 140,...,202
  infilename = 'archive %s.pdf' % archivepage
  nout = nout + 1
  outfilename = 'pg%02d.pdf' % nout
  outpage = '%02d' % nout  
  ans.append((infilename,outfilename,outpage))
 return ans
if __name__ == "__main__":
 filescript = sys.argv[1]  # script name
 filepdf = sys.argv[2] # pdffiles.txt
 frontnames = frontmap()
 bodynames = bodymap()
 write_script(filescript,frontnames,bodynames)
 write_pdffiles(filepdf,frontnames,bodynames)
 exit(1)
 shfiles = []
 for vol in ['extract']:
  filenames = os.listdir('%s'% vol)
  #volfiles.append(filenames)
  print(vol,len(filenames))
  shfile = makesh(vol,filenames)

  shfiles.append((vol,shfile))
 write_script(fileout,shfiles)
 
