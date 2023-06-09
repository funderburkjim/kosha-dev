echo "BEGIN redo_xml.sh"

echo "construct ${dictlo}.xml..."
python3 make_xml.py ../orig/${dictlo}.txt ${dictlo}hw.txt ${dictlo}.xml # > redoxml_log.txt

echo "construct ${dictlo}.xml..."
python3 make_xml.py ../orig/${dictlo}.txt ${dictlo}hw.txt ${dictlo}.xml # > redoxml_log.txt
echo "construct ${dictlo}1.xml..."
python3 xml_to_xml1.py ${dictlo}.xml ${dictlo}1.xml
echo "construct ${dictlo}2.xml..."
python3 xml1_to_xml.py ${dictlo}1.xml temp_${dictlo}2.xml
echo "Diff if any between ${dictlo}.xml and temp_${dictlo}2.xml"
echo "Ideally, there should only no difference"
diff ${dictlo}.xml temp_${dictlo}2.xml
echo "[END OF diff]"
echo ""

echo "\nxmllint on ${dictlo}.xml..."
echo "SKIPPING xmllint validity check"
# xmllint --noout --valid ${dictlo}.xml
echo "\n${dictlo}.sqlite..."
#  construct things that depend on xxx.xml
sh redo_postxml.sh
echo "END redo_xml.sh"
