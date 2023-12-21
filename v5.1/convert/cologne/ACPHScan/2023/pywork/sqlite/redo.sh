sqlitedb="acph.sqlite"
xml="../acph.xml"
echo "remaking $sqlitedb from $xml with python..."
python3 sqlite.py $xml $sqlitedb
echo "moving $sqlitedb to web/sqlite/"
mv acph.sqlite ../../web/sqlite/
