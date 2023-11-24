# 
# 0. copy xxxheader.xml from pywork to web
echo "BEGIN pywork/redo_postxml.sh"
pwd
echo "cp abchheader.xml ../web/"
cp abchheader.xml ../web/
echo ""
# 1. Redo web/xxx.sqlite
echo "BEGIN sqlite"
cd sqlite
sh redo.sh
cd ../ # back in pywork
echo "END sqlite"
# 2. redo db (query_dump) for advanced search
cd webtc2
sh redo.sh
cd ../ # back to pywork
# For applicable dictionaries, update other web/sqlite databases
# abbreviations
# literary source.
# two extra links dbs for mw
