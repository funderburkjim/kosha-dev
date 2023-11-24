sqlitedb="abch.sqlite"
xml="../abch.xml"
echo "remaking $sqlitedb from $xml with python..."
python3 sqlite.py $xml $sqlitedb
echo "moving $sqlitedb to web/sqlite/"
mv abch.sqlite ../../web/sqlite/
