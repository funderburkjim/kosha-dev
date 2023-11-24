echo "BEGIN: downloads/redo_txt.sh"
if [ -f abchtxt.zip ]
 then
 echo "remove old abchtxt.zip"
 rm abchtxt.zip
fi
if [ -f txt ]
 then
  rm -r txt
fi
mkdir txt
echo "copying files from ../pywork to txt/"
cp ../orig/abch.txt txt/
cp ../pywork/abch-meta2.txt txt/
cp ../pywork/abchheader.xml txt/

echo "create new abchtxt.zip"
zip -rq abchtxt.zip txt
# clean up. Remove txt directory
rm -r txt
