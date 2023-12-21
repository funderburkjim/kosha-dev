echo "BEGIN: downloads/redo_xml.sh"
if [ -f acphxml.zip ]
 then
 echo "remove old acphxml.zip"
 rm acphxml.zip
fi
if [ -f xml ]
 then
  rm -r xml
fi
mkdir xml
echo "copying files from ../pywork to xml/"
cp ../pywork/acph.dtd xml/
cp ../pywork/acph.xml xml/
cp ../pywork/acph-meta2.txt xml/
cp ../pywork/acphheader.xml xml/

echo "create new acphxml.zip"
zip -rq acphxml.zip xml
# clean up. Remove xml directory
rm -r xml
