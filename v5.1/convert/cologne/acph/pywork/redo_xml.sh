echo "BEGIN redo_xml.sh"

echo "construct acph.xml..."
python3 make_xml.py ../orig/acph.txt acphhw.txt acph.xml # > redoxml_log.txt
echo "xmllint on acph.xml..."
xmllint --noout --valid acph.xml
echo "acph.sqlite..."
#  construct things that depend on xxx.xml
sh redo_postxml.sh
echo "END redo_xml.sh"
