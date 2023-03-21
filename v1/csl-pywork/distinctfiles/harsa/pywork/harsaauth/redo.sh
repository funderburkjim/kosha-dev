echo "harsaauthtooltips.sqlite"
sqlite3 harsaauthtooltips.sqlite < tooltips.sql
chmod 0755 harsaauthtooltips.sqlite  # needed?
echo "copy harsaauthtooltips.sqlite to web/sqlite"
cp harsaauthtooltips.sqlite ../../web/sqlite/
