echo "BEGIN: downloads/redo_xml.sh"
if [ -f abchxml.zip ]
 then
 echo "remove old abchxml.zip"
 rm abchxml.zip
fi
if [ -f xml ]
 then
  rm -r xml
fi
mkdir xml
echo "copying files from ../pywork to xml/"
cp ../pywork/abch.dtd xml/
cp ../pywork/abch.xml xml/
cp ../pywork/abch-meta2.txt xml/
cp ../pywork/abchheader.xml xml/

echo "create new abchxml.zip"
zip -rq abchxml.zip xml
# clean up. Remove xml directory
rm -r xml
