echo "BEGIN: downloads/redo_web1.sh"
if [ -f acphweb1.zip ]
 then
 echo "remove old acphweb1.zip"
 rm acphweb1.zip
fi
cd ../
zip  -rq downloads/acphweb1.zip web -x *pdfpages*
cd downloads
