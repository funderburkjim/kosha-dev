echo "BEGIN: downloads/redo_txt.sh"
if [ -f acphtxt.zip ]
 then
 echo "remove old acphtxt.zip"
 rm acphtxt.zip
fi
if [ -f txt ]
 then
  rm -r txt
fi
mkdir txt
echo "copying files from ../pywork to txt/"
cp ../orig/acph.txt txt/
cp ../pywork/acph-meta2.txt txt/
cp ../pywork/acphheader.xml txt/

echo "create new acphtxt.zip"
zip -rq acphtxt.zip txt
# clean up. Remove txt directory
rm -r txt
