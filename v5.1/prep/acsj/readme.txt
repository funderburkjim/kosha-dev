अभिधानचिन्तामणिशिलोञ्छ  by जिनदेव
# --------------
# The base version is acsj1.txt from Dhaval
sh redo.sh # generates acsj.txt from acsj1.txt
# this is what it does
# convert acsj1.txt to slp1 version acsj.txt
python convert.py deva,slp1 acsj1.txt acsj.txt
# check invertability
python convert.py slp1,deva acsj.txt temp_acsj1.txt
diff acsj1.txt temp_acsj1.txt
# should be no difference
rm temp_acsj1.txt

# --------------
Notes on further steps:
# assume v4 as current directory
mkdir csl-orig/acsj
cp prep/acsj/acsj.txt csl-orig/acsj/acsj.txt
touch csl-orig/acsj/acsj-meta2.txt
touch csl-orig/acsj/acsj_hwextra.txt
touch csl-orig/acsj/acsjheader.xml  # note this to be modified later

edit csl-pywork/dictparms.py
 # add info for acsj
edit csl-pywork/inventory.txt
 # add info for acsj
edit csl-pywork/redo_xampp_all.sh
edit csl-pywork/redo_cologne_all.sh

edit csl-websanlexicon/dictparms.py
 # add info for acsj
mkdir csl-websanlexicon/distinctfiles/acsj
mkdir csl-websanlexicon/distinctfiles/acsj/web
mkdir csl-websanlexicon/distinctfiles/acsj/web/webtc
echo "0001:pg_0001.pdf" >  csl-websanlexicon/distinctfiles/acsj/web/webtc/pdffiles.txt

edit csl-pywork/makotemplates/pywork/hw.py
 add init_keys for acsj

edit csl-pywork/makotemplates/pywork/redo_xml.sh
  SKIP acsj1.xml
edit csl-pywork/makotemplates/pywork/make_xml.py
 construct_xmlstring_1 (for anhk)
 construct_xmlstring_2 (for acsj)

edit csl-pywork/makotemplates/web/webtc/dispitem.php
  For specific requirement like creating synonym-gender block as in ABCH.
edit csl-pywork/makotemplates/web/webtc/getword_data.php
  For $L instead of $lnum

gender-frequency list
python gender_list.py acsj.txt gender_list.txt

