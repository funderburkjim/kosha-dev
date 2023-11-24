echo "BEGIN: downloads/redo_web1.sh"
if [ -f abchweb1.zip ]
 then
 echo "remove old abchweb1.zip"
 rm abchweb1.zip
fi
cd ../
zip  -rq downloads/abchweb1.zip web -x *pdfpages*
cd downloads
