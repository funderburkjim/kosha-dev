अभिधानचिन्तामणि  by हेमचन्द्राचार्य
# --------------
# The base version is acph1.txt from Dhaval
sh redo.sh # generates acph.txt from acph1.txt
# this is what it does
# convert acph1.txt to slp1 version acph.txt
python convert.py deva,slp1 acph1.txt acph.txt
# check invertability
python convert.py slp1,deva acph.txt temp_acph1.txt
diff acph1.txt temp_acph1.txt
# should be no difference
rm temp_acph1.txt

# --------------
Notes on further steps:
# assume v4 as current directory
mkdir csl-orig/acph
cp prep/acph/acph.txt csl-orig/acph/acph.txt
touch csl-orig/acph/acph-meta2.txt
touch csl-orig/acph/acph_hwextra.txt
touch csl-orig/acph/acphheader.xml  # note this to be modified later

edit csl-pywork/dictparms.py
 # add info for acph
edit csl-pywork/inventory.txt
 # add info for acph
edit csl-pywork/redo_xampp_all.sh
edit csl-pywork/redo_cologne_all.sh

edit csl-websanlexicon/dictparms.py
 # add info for acph
mkdir csl-websanlexicon/distinctfiles/acph
mkdir csl-websanlexicon/distinctfiles/acph/web
mkdir csl-websanlexicon/distinctfiles/acph/web/webtc
echo "0001:pg_0001.pdf" >  csl-websanlexicon/distinctfiles/acph/web/webtc/pdffiles.txt

edit csl-pywork/makotemplates/pywork/hw.py
 add init_keys for acph

edit csl-pywork/makotemplates/pywork/redo_xml.sh
  SKIP acph1.xml
edit csl-pywork/makotemplates/pywork/make_xml.py
 construct_xmlstring_1 (for anhk)
 construct_xmlstring_2 (for acph)

gender-frequency list
python gender_list.py acph.txt gender_list.txt

