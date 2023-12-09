echo "remaking anhkab.sqlite"
rm anhkab.sqlite
sqlite3 anhkab.sqlite < anhkab.sql
echo "finished remaking anhkab.sqlite"
chmod 0755 anhkab.sqlite
