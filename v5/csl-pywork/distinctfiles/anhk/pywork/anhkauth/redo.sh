echo "anhkauthtooltips.sqlite"
sqlite3 anhkauthtooltips.sqlite < tooltips.sql
chmod 0755 anhkauthtooltips.sqlite  # needed?
echo "copy anhkauthtooltips.sqlite to web/sqlite"
cp anhkauthtooltips.sqlite ../../web/sqlite/
