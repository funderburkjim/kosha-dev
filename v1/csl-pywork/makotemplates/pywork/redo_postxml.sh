# 
# 0. copy xxxheader.xml from pywork to web
echo "BEGIN pywork/redo_postxml.sh"
pwd
echo "cp ${dictlo}header.xml ../web/"
cp ${dictlo}header.xml ../web/
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
%if dictlo in []:
 cd ${dictlo}ab
 sh redo.sh
 cd ../ # back to pywork
%endif
# literary source.
%if dictlo in []:
 cd ${dictlo}auth
 sh redo.sh
 cd ../ # back to pywork
%endif
