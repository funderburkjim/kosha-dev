echo "BEGIN redo_xml.sh"

echo "construct abch.xml..."
python3 make_xml.py ../orig/abch.txt abchhw.txt abch.xml # > redoxml_log.txt
echo "xmllint on abch.xml..."
xmllint --noout --valid abch.xml
echo "abch.sqlite..."
#  construct things that depend on xxx.xml
sh redo_postxml.sh
echo "END redo_xml.sh"
