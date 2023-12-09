kosha-dev/v5.1/convert
11-16-2023
Conversion of this version to be part of the cologne dictionaries.


# this directory
cd /c/xampp/htdocs/kosha-dev/v5.1/convert/
--------------------------------------------------------------------
# Make local versions of csl-pywork, csl-websanlexicon, csl-orig
#  remove temporary and files which are obviously irrelevant in conversion
--------------------------------------------------------------------
#  cologne directory
# current directory: convert
0. mkdir cologne
1. csl-pywork
cp -r /c/xampp/htdocs/cologne/csl-pywork/ cologne/
cd cologne/csl-pywork
rm -r -f .git  # remove git
# remove everything but csl-pywork/v02 (manual)
cd /c/xampp/htdocs/kosha-dev/v5.1/convert/

2. csl-websanlexicon
cp -r /c/xampp/htdocs/cologne/csl-pywork/ cologne/
cd cologne/csl-pywork
rm -r -f .git  # remove git
# remove everything but csl-websanlexicon/v02 (manual)

3. csl-orig
# we don't copy all the other dictionaries !
cd /c/xampp/htdocs/kosha-dev/v5.1/convert/
mkdir cologne/csl-orig
mkdir cologne/csl-orig/v02
mkdir cologne/csl-orig/v02/abch
cp ../csl-orig/abch/abch.txt cologne/csl-orig/v02/abch/
cp ../csl-orig/abch/abch_hwextra.txt cologne/csl-orig/v02/abch/
cp ../csl-orig/abch/abch-meta2.txt cologne/csl-orig/v02/abch/
cp ../csl-orig/abch/abchheader.xml cologne/csl-orig/v02/abch/

--------------------------------------------------------------------
Make copy of current v5.1 versions of the repos under 'kosh'
--------------------------------------------------------------------
cd /c/xampp/htdocs/kosha-dev/v5.1/convert/
mkdir kosh
1. csl-orig
mkdir kosh/csl-orig
mkdir kosh/csl-orig/v02
cp -r ../csl-orig/abch kosh/csl-orig/v02/

2. csl-pywork
mkdir kosh/csl-pywork
cp -r ../csl-pywork kosh/csl-pywork/v02/

3. csl-websanlexicon
mkdir kosh/csl-websanlexicon
cp -r ../csl-websanlexicon kosh/csl-websanlexicon/v02/
../csl-pywork ../csl-pywork/v02

--------------------------------------------------------------------
comparison of directories kosh and cologne
--------------------------------------------------------------------
----- From bing chat
python bing_are_dirs_equal.py kosh cologne
ans=False   (the directories are different).
This is not useful.
-----

cd /c/xampp/htdocs/kosha-dev/v5.1/convert/
python dircmp_v0.py kosh cologne

This prints a 'report' (to stdout)
Better, but needs some tinkering to be more useful
------
Make local version of Python filecmp class.

my version of python library filecmp:  myfilecmp.py

cp /c/Users/jimfu/AppData/Local/Programs/Python/Python39/Lib/filecmp.py myfilecmp.py

python dircmp.py kosh,kosh cologne,cologne dircmp_0.txt
# 97 records written to dircmp_0.txt

-----------------------------------------------------------------
begin revisions
-----------------------------------------------------------------
mkdir revise
mkdir revise/old
mkdir revise/new
----------------------------------------------------------------
diff kosh/csl-pywork/v02 cologne/csl-pywork/v02
  Identical files : generate_pywork.sh, readme.md, readme_dtd.txt, readme_selective.md, redo_xampp_selective.sh, xmlchk_xampp.sh
  Differing files :
  dictparms.py revised
  generate.py  revised
  generate_dict.sh revised
  generate_orig.sh, inventory.txt, inventory_orig.txt, redo_cologne_all.sh, redo_xampp_all.sh

  diff kosh/csl-websanlexicon/v02 cologne/csl-websanlexicon/v02
  Only in kosh/csl-websanlexicon/v02 :
    apidev_copy.sh ?
  Identical files : generate.py
  Differing files :
    apidev_readme.md ?
    dictparms.py revised
    generate_web.sh revised
    inventory.txt  no revision required
    redo_cologne_all.sh
    redo_xampp_all.sh
  Common subdirectories : distinctfiles, makotemplates

   diff kosh/csl-websanlexicon/v02/distinctfiles cologne/csl-websanlexicon/v02/distinctfiles
   Only in kosh/csl-websanlexicon/v02/distinctfiles : abch, anhk
   Only in cologne/csl-websanlexicon/v02/distinctfiles : acc, ae, ap, ap90, armh, 
------------
# csl-pywork/v02/dictparms.py
cp cologne/csl-pywork/v02/dictparms.py revise/old/
cp cologne/csl-pywork/v02/dictparms.py revise/new/

# revise/new/dictparms.py # edited version
# add "abch" to alldictparms
cp revise/new/dictparms.py cologne/csl-pywork/v02/
------------
csl-pywork/v02/generate.py
cp cologne/csl-pywork/v02/generate.py revise/old/
cp cologne/csl-pywork/v02/generate.py revise/new/

# revise/new/generate.py # edited version
# try-except error catcher for copyfile
cp revise/new/generate.py cologne/csl-pywork/v02/
------------
generate_dict.sh
cp cologne/csl-pywork/v02/generate_dict.sh revise/old/
cp cologne/csl-pywork/v02/generate_dict.sh revise/new/

diff kosh/csl-pywork/v02/generate_dict.sh revise/new/generate_dict.sh
# revise/new/generate_dict.sh # edited version
# a. additional 'echo' statements
# b. uncomment 'downloads' section

cp revise/new/generate_dict.sh cologne/csl-pywork/v02/

--------------
dictparms.py

# csl-websanlexicon/v02/dictparms.py
cp cologne/csl-websanlexicon/v02/dictparms.py revise/old/web_dictparms.py
cp cologne/csl-websanlexicon/v02/dictparms.py revise/new/web_dictparms.py

# revise/new/web_dictparms.py # edited version
# add "abch" to alldictparms
cp revise/new/web_dictparms.py cologne/csl-websanlexicon/v02/dictparms.py

--------------
generate_web.sh

# csl-websanlexicon/v02/generate_web.sh
cp cologne/csl-websanlexicon/v02/generate_web.sh revise/old/web_generate_web.sh
cp cologne/csl-websanlexicon/v02/generate_web.sh revise/new/web_generate_web.sh

# revise/new/web_generate_web.sh # edited version
# minor change to an echo.
cp revise/new/web_generate_web.sh cologne/csl-websanlexicon/v02/generate_web.sh


---------------------
csl-websanlexicon/v02/distinctfiles/abch/web/webtc/pdffiles.txt
This file not in dircmp_0

mkdir cologne/csl-websanlexicon/v02/distinctfiles/abch/
mkdir cologne/csl-websanlexicon/v02/distinctfiles/abch/web
mkdir cologne/csl-websanlexicon/v02/distinctfiles/abch/web/webtc
cp kosh/csl-websanlexicon/v02/distinctfiles/abch/web/webtc/pdffiles.txt revise/old/pdffiles.txt
cp kosh/csl-websanlexicon/v02/distinctfiles/abch/web/webtc/pdffiles.txt revise/new/pdffiles.txt
cp revise/new/pdffiles.txt cologne/csl-websanlexicon/v02/distinctfiles/abch/web/webtc/pdffiles.txt

-------------------------
hwparse.py
csl-pywork/v02/makotemplates/pywork/hwparse.py

cp cologne/csl-pywork/v02/makotemplates/pywork/hwparse.py revise/old/hwparse.py
cp cologne/csl-pywork/v02/makotemplates/pywork/hwparse.py revise/new/hwparse.py

# diff kosh/csl-pywork/v02/makotemplates/pywork/hwparse.py revise/new/hwparse.py
# quite different.

cp revise/new/hwparse.py cologne/csl-pywork/v02/makotemplates/pywork/hwparse.py

-------------------------
hw.py
csl-pywork/v02/makotemplates/pywork/hw.py

cp cologne/csl-pywork/v02/makotemplates/pywork/hw.py revise/old/hw.py
cp cologne/csl-pywork/v02/makotemplates/pywork/hw.py revise/new/hw.py

diff kosh/csl-pywork/v02/makotemplates/pywork/hw.py revise/new/hw.py
# quite different.

cp revise/new/hw.py cologne/csl-pywork/v02/makotemplates/pywork/hw.py

-------------------------
hw0.py
csl-pywork/v02/makotemplates/pywork/hw0.py

cp cologne/csl-pywork/v02/makotemplates/pywork/hw0.py revise/old/hw0.py
cp cologne/csl-pywork/v02/makotemplates/pywork/hw0.py revise/new/hw0.py

diff kosh/csl-pywork/v02/makotemplates/pywork/hw0.py revise/new/hw0.py | wc -l
# 94 --- many diffs.
# differences due to line-endings, which are 'windows' style in cologne
# revise cologne line endings 
python unixify1.py revise/old/hw0.py revise/new/hw0.py
# check no more diffs
diff kosh/csl-pywork/v02/makotemplates/pywork/hw0.py revise/new/hw0.py | wc -l
# 0 no more differences

cp revise/new/hw0.py cologne/csl-pywork/v02/makotemplates/pywork/hw0.py

-------------------------
hw2.py
csl-pywork/v02/makotemplates/pywork/hw2.py

cp cologne/csl-pywork/v02/makotemplates/pywork/hw2.py revise/old/hw2.py
cp cologne/csl-pywork/v02/makotemplates/pywork/hw2.py revise/new/hw2.py

diff kosh/csl-pywork/v02/makotemplates/pywork/hw2.py revise/new/hw2.py | wc -l
# 94 --- many diffs.
# differences due to line-endings, which are 'windows' style in cologne
# revise cologne line endings 
python unixify1.py revise/old/hw2.py revise/new/hw2.py
# check no more diffs
diff kosh/csl-pywork/v02/makotemplates/pywork/hw2.py revise/new/hw2.py | wc -l
# 0 no more differences

cp revise/new/hw2.py cologne/csl-pywork/v02/makotemplates/pywork/hw2.py

-------------------------
redo_hw.sh
csl-pywork/v02/makotemplates/pywork/redo_hw.sh

cp cologne/csl-pywork/v02/makotemplates/pywork/redo_hw.sh revise/old/redo_hw.sh
cp cologne/csl-pywork/v02/makotemplates/pywork/redo_hw.sh revise/new/redo_hw.sh

diff kosh/csl-pywork/v02/makotemplates/pywork/redo_hw.sh revise/new/redo_hw.sh | wc -l
# 38 --- many diffs.
# several minor mods to revise/new/redo_hw.sh.
# Still one difference.
diff kosh/csl-pywork/v02/makotemplates/pywork/redo_hw.sh revise/new/redo_hw.sh > tempdiff_redo_hw.txt
27,31c27,31
< #%if dictlo == 'mw':
< #echo "construct mwkeys.sqlite"
< #cd mwkeys
< #sh redo.sh
< #%endif
---
> %if dictlo == 'mw':
> echo "construct mwkeys.sqlite"
> cd mwkeys
> sh redo.sh
> %endif


cp revise/new/redo_hw.sh cologne/csl-pywork/v02/makotemplates/pywork/redo_hw.sh

********************************************************************
headwords are made now.
Next step xml.
********************************************************************
-------------------------
redo_xml.sh
csl-pywork/v02/makotemplates/pywork/redo_xml.sh

cp cologne/csl-pywork/v02/makotemplates/pywork/redo_xml.sh revise/old/redo_xml.sh
cp cologne/csl-pywork/v02/makotemplates/pywork/redo_xml.sh revise/new/redo_xml.sh

diff kosh/csl-pywork/v02/makotemplates/pywork/redo_xml.sh revise/new/redo_xml.sh | wc -l
# 31

# examine the diffs. Minor mods to revise/new/redo_xml.sh
diff kosh/csl-pywork/v02/makotemplates/pywork/redo_xml.sh revise/new/redo_xml.sh > tempdiff_redo_xml.sh.txt

cp revise/new/redo_xml.sh cologne/csl-pywork/v02/makotemplates/pywork/redo_xml.sh

-------------------------
redo_postxml.sh
csl-pywork/v02/makotemplates/pywork/redo_postxml.sh

cp cologne/csl-pywork/v02/makotemplates/pywork/redo_postxml.sh revise/old/redo_postxml.sh
cp cologne/csl-pywork/v02/makotemplates/pywork/redo_postxml.sh revise/new/redo_postxml.sh

diff kosh/csl-pywork/v02/makotemplates/pywork/redo_postxml.sh revise/new/redo_postxml.sh | wc -l
# 30

# examine the diffs. Minor mods to revise/new/redo_postxml.sh
diff kosh/csl-pywork/v02/makotemplates/pywork/redo_postxml.sh revise/new/redo_postxml.sh > tempdiff_redo_postxml.sh.txt
# some tasks remain in the cologne version, which were avoided in the
# kosha version.

cp revise/new/redo_postxml.sh cologne/csl-pywork/v02/makotemplates/pywork/redo_postxml.sh

-------------------------
make_xml.py
csl-pywork/v02/makotemplates/pywork/make_xml.py

cp cologne/csl-pywork/v02/makotemplates/pywork/make_xml.py revise/old/make_xml.py
cp cologne/csl-pywork/v02/makotemplates/pywork/make_xml.py revise/new/make_xml.py

diff kosh/csl-pywork/v02/makotemplates/pywork/make_xml.py revise/new/make_xml.py | wc -l
# 1057

# major revision of make_xml.py for abch
# 1. abch uses copnstruct_xmlstring_2
# 1a. anhk uses construct_xmlstring_1 (not currently used)

# examine the diffs. Minor mods to revise/new/make_xml.py
diff kosh/csl-pywork/v02/makotemplates/pywork/make_xml.py revise/new/make_xml.py > tempdiff_make_xml.py.txt
# some tasks remain in the cologne version, which were avoided in the
# kosha version.

cp revise/new/make_xml.py cologne/csl-pywork/v02/makotemplates/pywork/make_xml.py

sh redo_abch_cologne.sh
diff ../apps/abch/pywork/abch.xml cologne/abch/pywork/abch.xml | wc -l
# 0   revised cologne gives v5.1 version of abch.xml !!


-------------------------
one.dtd
csl-pywork/v02/makotemplates/pywork/one.dtd

cp cologne/csl-pywork/v02/makotemplates/pywork/one.dtd revise/old/one.dtd
cp cologne/csl-pywork/v02/makotemplates/pywork/one.dtd revise/new/one.dtd

diff kosh/csl-pywork/v02/makotemplates/pywork/one.dtd revise/new/one.dtd | wc -l
# 191
# modify revise/new/one.dtd

# examine the diffs. Minor mods to revise/new/one.dtd

cp revise/new/one.dtd cologne/csl-pywork/v02/makotemplates/pywork/one.dtd

sh redo_abch_cologne.sh
python /c/xampp/htdocs/cologne/xmlvalidate.py cologne/abch/pywork/abch.xml cologne/abch/pywork/abch.dtd
# ok

-------------------------
one.dtd
csl-pywork/v02/inventory.txt

cp cologne/csl-pywork/v02/inventory.txt revise/old/inventory.txt
cp cologne/csl-pywork/v02/inventory.txt revise/new/inventory.txt

diff kosh/csl-pywork/v02/inventory.txt revise/new/inventory.txt | wc -l
# 116
# modify revise/new/inventory.txt
diff kosh/csl-pywork/v02/inventory.txt revise/new/inventory.txt > tempdiff_inventory.txt
# most diffs are due to commenting out. Not sure of significance
# make sqlite.py a template

# examine the diffs. Minor mods to revise/new/inventory.txt

cp revise/new/inventory.txt cologne/csl-pywork/v02/inventory.txt

sh redo_abch_cologne.sh
python /c/xampp/htdocs/cologne/xmlvalidate.py cologne/abch/pywork/abch.xml cologne/abch/pywork/abch.dtd
# ok

-------------------------
sqlite.py
csl-pywork/v02/makotemplates/pywork/sqlite/sqlite.py

cp cologne/csl-pywork/v02/makotemplates/pywork/sqlite/sqlite.py revise/old/sqlite.py
cp cologne/csl-pywork/v02/makotemplates/pywork/sqlite/sqlite.py revise/new/sqlite.py

diff kosh/csl-pywork/v02/makotemplates/pywork/sqlite/sqlite.py revise/new/sqlite.py | wc -l
# 284  many differences to examine

diff kosh/csl-pywork/v02/makotemplates/pywork/sqlite/sqlite.py revise/new/sqlite.py > tempdiff_sqlite.py.txt

# some diffs due to line-end
python unixify1.py revise/old/sqlite.py revise/new/sqlite.py
diff kosh/csl-pywork/v02/makotemplates/pywork/sqlite/sqlite.py revise/new/sqlite.py | wc -l
# 68   remaining differences

# a. lnum parameter NOT unique for abch
# b. sort_lines function for abch

cp revise/new/sqlite.py cologne/csl-pywork/v02/makotemplates/pywork/sqlite/sqlite.py
Using windows fc.exe in cmd shell:
cd C:\xampp\htdocs\kosha-dev\v5.1\
C:\xampp\htdocs\kosha-dev\v5.1\convert>fc.exe  /b ..\apps\abch\web\sqlite\abch.sqlite cologne\abch\web\sqlite\abch.sqlite
Comparing files ..\APPS\ABCH\WEB\SQLITE\abch.sqlite and COLOGNE\ABCH\WEB\SQLITE\ABCH.SQLITE
FC: no differences encountered

So, the sqlite files are identical

**********************************************************************************
convert websanlexicon displays
  diff kosh/csl-websanlexicon/v02 cologne/csl-websanlexicon/v02
  Only in kosh/csl-websanlexicon/v02 : apidev_copy.sh
  Identical files : generate.py
  Differing files : apidev_readme.md, dictparms.py, generate_web.sh, inventory.txt, redo_cologne_all.sh, redo_xampp_all.sh
  Common subdirectories : distinctfiles, makotemplates
**********************************************************************************
dictparms.py and generate_web.sh have already been examined above.
--------------
apidev_readme.md

# csl-websanlexicon/v02/apidev_readme.md
cp cologne/csl-websanlexicon/v02/apidev_readme.md revise/old/web_apidev_readme.md
cp cologne/csl-websanlexicon/v02/apidev_readme.md revise/new/web_apidev_readme.md

diff kosh/csl-websanlexicon/v02/apidev_readme.md revise/new/web_apidev_readme.md | wc -l
# 34
diff -w kosh/csl-websanlexicon/v02/apidev_readme.md revise/new/web_apidev_readme.md | wc -l
# 0

So, just line-break diffs.
python unixify1.py revise/old/web_apidev_readme.md revise/new/web_apidev_readme.md
diff kosh/csl-websanlexicon/v02/apidev_readme.md revise/new/web_apidev_readme.md | wc -l
# 0


cp revise/new/web_apidev_readme.md cologne/csl-websanlexicon/v02/apidev_readme.md

--------------
inventory.txt  START
# csl-websanlexicon/v02/inventory.txt
cp cologne/csl-websanlexicon/v02/inventory.txt revise/old/web_inventory.txt
cp cologne/csl-websanlexicon/v02/inventory.txt revise/new/web_inventory.txt

diff kosh/csl-websanlexicon/v02/inventory.txt revise/new/web_inventory.txt | wc -l
# 39

So, just line-break diffs.
python unixify1.py revise/old/web_inventory.txt revise/new/web_inventory.txt
diff kosh/csl-websanlexicon/v02/inventory.txt revise/new/web_inventory.txt > tempdiff_web_inventory.txt
# the differences are all extra lines appearing in revise/new/web_inventory.
# No changes made to revise/new/web_inventory.

cp revise/new/web_inventory.txt cologne/csl-websanlexicon/v02/inventory.txt

--------------
redo_cologne_all.sh

# csl-websanlexicon/v02/redo_cologne_all.sh
cp cologne/csl-websanlexicon/v02/redo_cologne_all.sh revise/old/web_redo_cologne_all.sh
cp cologne/csl-websanlexicon/v02/redo_cologne_all.sh revise/new/web_redo_cologne_all.sh

diff kosh/csl-websanlexicon/v02/redo_cologne_all.sh revise/new/web_redo_cologne_all.sh | wc -l
# 43
# kosh version is empty.
# add 'sh generate_web.sh abch  ../../ABCHScan/2023/' to web_redo_cologne_all.sh

cp revise/new/web_redo_cologne_all.sh cologne/csl-websanlexicon/v02/redo_cologne_all.sh

--------------
redo_xampp_all.sh

# csl-websanlexicon/v02/redo_xampp_all.sh
cp cologne/csl-websanlexicon/v02/redo_xampp_all.sh revise/old/web_redo_xampp_all.sh
cp cologne/csl-websanlexicon/v02/redo_xampp_all.sh revise/new/web_redo_xampp_all.sh

Add 'sh generate_web.sh abch  ../../abch' to revise/new/web_redo_xampp_all.sh.

cp revise/new/web_redo_xampp_all.sh cologne/csl-websanlexicon/v02/redo_xampp_all.sh

-------------
csl-websanlexicon/v02/makotemplates/web/index.php

cp cologne/csl-websanlexicon/v02/makotemplates/web/index.php revise/old/web_index.php
cp cologne/csl-websanlexicon/v02/makotemplates/web/index.php revise/new/web_index.php

diff kosh/csl-websanlexicon/v02/makotemplates/web/index.php revise/new/web_index.php | wc -l
# 20
diff kosh/csl-websanlexicon/v02/makotemplates/web/index.php revise/new/web_index.php > tempdiff_web_index.php.txt

# some differences to resolve later?
cp revise/new/web_index.php cologne/csl-websanlexicon/v02/makotemplates/web/index.php

-------------
csl-websanlexicon/v02/makotemplates/web/readme.txt

cp cologne/csl-websanlexicon/v02/makotemplates/web/readme.txt revise/old/web_readme.txt
cp cologne/csl-websanlexicon/v02/makotemplates/web/readme.txt revise/new/web_readme.txt

diff kosh/csl-websanlexicon/v02/makotemplates/web/readme.txt revise/new/web_readme.txt | wc -l
# 142
diff -w kosh/csl-websanlexicon/v02/makotemplates/web/readme.txt revise/new/web_readme.txt | wc -l
# 0
So differences probably due to line-ending
Make line-endings unix-style

python unixify1.py revise/old/web_readme.txt revise/new/web_readme.txt
# check
diff kosh/csl-websanlexicon/v02/makotemplates/web/readme.txt revise/new/web_readme.txt | wc -l
# 0

cp revise/new/web_readme.txt cologne/csl-websanlexicon/v02/makotemplates/web/readme.txt

-------------
csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/slp1_deva1.xml

cp cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/slp1_deva1.xml revise/old/slp1_deva1.xml
cp cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/slp1_deva1.xml revise/new/slp1_deva1.xml

diff kosh/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/slp1_deva1.xml revise/new/slp1_deva1.xml | wc -l
# 12
diff kosh/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/slp1_deva1.xml revise/new/slp1_deva1.xml > tempdiff_slp1_deva1.xml
    139,141c139,141
    < <e n='122'> <s>INIT,SKT</s> <in>\</in> <out>\u0952</out>  <next>SKT</next></e>
    < <!-- udAtta accent (per pwg): ua8eb -->
    < <e n='123'> <s>INIT,SKT</s> <in>/</in> <out>\ua8eb</out>  <next>SKT</next></e>
    ---
    > <e n='122'> <s>INIT,SKT</s> <in>\</in> <out>\u0952</out> <next>INIT</next> </e>
    > <!-- udAtta accent : ua8eb -->
    > <e n='123'> <s>INIT,SKT</s> <in>/</in> <out>\ua8eb</out>  <next>INIT</next> </e>
    143c143
    < <e n='124'> <s>INIT,SKT</s> <in>^</in> <out>\u0951</out> <next>SKT</next> </e>
    ---
    > <e n='124'> <s>INIT,SKT</s> <in>^</in> <out>\u0951</out> <next>INIT</next> </e>
Note: Not sure about this.
Making no change now.

cp revise/new/slp1_deva1.xml cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/slp1_deva1.xml

--------------------------
csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php

cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php revise/old/basicadjust.php
cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php revise/new/basicadjust.php

diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php revise/new/basicadjust.php | wc -l
# 1611  lot's of differences!
diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php revise/new/basicadjust.php > tempdiff_basicadjust.php

Manual adjustment. Not too complicated.

cp revise/new/basicadjust.php cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php

--------------------------
csl-websanlexicon/v02/makotemplates/web/webtc/basicdisplay.php

cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicdisplay.php revise/old/basicdisplay.php
cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicdisplay.php revise/new/basicdisplay.php

diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/basicdisplay.php revise/new/basicdisplay.php | wc -l
# 1246  lot's of differences!

diff -w kosh/csl-websanlexicon/v02/makotemplates/web/webtc/basicdisplay.php revise/new/basicdisplay.php | wc -l
# 762 --

Let's get the line-endings unix style

python unixify1.py revise/old/basicdisplay.php revise/new/basicdisplay.php

diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/basicdisplay.php revise/new/basicdisplay.php > tempdiff_basicdisplay.php

Manual adjustment. 

cp revise/new/basicdisplay.php cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicdisplay.php

--------------------------
csl-websanlexicon/v02/makotemplates/web/webtc/dictinfo.php

cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/dictinfo.php revise/old/web_dictinfo.php
cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/dictinfo.php revise/new/web_dictinfo.php

diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/dictinfo.php revise/new/web_dictinfo.php | wc -l
# 84



diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/dictinfo.php revise/new/web_dictinfo.php > tempdiff_web_dictinfo.php

Differences due to change in location of Cologne scanned imges  ($cologne_pdfpages_urls)
No changes.

cp revise/new/web_dictinfo.php cologne/csl-websanlexicon/v02/makotemplates/web/webtc/dictinfo.php

--------------------------
csl-websanlexicon/v02/makotemplates/web/webtc/dispitem.php

cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/dispitem.php revise/old/web_dispitem.php
cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/dispitem.php revise/new/web_dispitem.php

diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/dispitem.php revise/new/web_dispitem.php | wc -l
# 26


diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/dispitem.php revise/new/web_dispitem.php > tempdiff_web_dispitem.php

# manual changes

cp revise/new/web_dispitem.php cologne/csl-websanlexicon/v02/makotemplates/web/webtc/dispitem.php

--------------------------
csl-websanlexicon/v02/makotemplates/web/webtc/font.css

cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/font.css revise/old/web_font.css
cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/font.css revise/new/web_font.css

diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/font.css revise/new/web_font.css | wc -l
# 26


diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/font.css revise/new/web_font.css > tempdiff_web_font.css
# 5
# No changes needed.

cp revise/new/web_font.css cologne/csl-websanlexicon/v02/makotemplates/web/webtc/font.css

--------------------------
csl-websanlexicon/v02/makotemplates/web/webtc/getword_data.php

cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/getword_data.php revise/old/web_getword_data.php
cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/getword_data.php revise/new/web_getword_data.php

diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/getword_data.php revise/new/web_getword_data.php | wc -l
# 23


diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/getword_data.php revise/new/web_getword_data.php > tempdiff_web_getword_data.php

# changes made

cp revise/new/web_getword_data.php cologne/csl-websanlexicon/v02/makotemplates/web/webtc/getword_data.php

--------------------------
csl-websanlexicon/v02/makotemplates/web/webtc/parm.php

cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/parm.php revise/old/web_parm.php
cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc/parm.php revise/new/web_parm.php

diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/parm.php revise/new/web_parm.php | wc -l
# 2


diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc/parm.php revise/new/web_parm.php > tempdiff_web_parm.php

# No change made.

cp revise/new/web_parm.php cologne/csl-websanlexicon/v02/makotemplates/web/webtc/parm.php

--------------------------
csl-websanlexicon/v02/makotemplates/web/webtc1/main.js

cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc1/main.js revise/old/webtc1_main.js
cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc1/main.js revise/new/webtc1_main.js

diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc1/main.js revise/new/webtc1_main.js | wc -l
# 23


diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc1/main.js revise/new/webtc1_main.js > tempdiff_webtc1_main.js

# No change made.

cp revise/new/webtc1_main.js cologne/csl-websanlexicon/v02/makotemplates/web/webtc1/main.js

--------------------------
csl-websanlexicon/v02/makotemplates/web/webtc2/querymodel.php

cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc2/querymodel.php revise/old/webtc2_querymodel.php
cp cologne/csl-websanlexicon/v02/makotemplates/web/webtc2/querymodel.php revise/new/webtc2_querymodel.php

diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc2/querymodel.php revise/new/webtc2_querymodel.php | wc -l
# 8


diff kosh/csl-websanlexicon/v02/makotemplates/web/webtc2/querymodel.php revise/new/webtc2_querymodel.php > tempdiff_webtc2_querymodel.php

# No change made.  Difference in prefix/suffix regexp.

cp revise/new/webtc2_querymodel.php cologne/csl-websanlexicon/v02/makotemplates/web/webtc2/querymodel.php

*******************************************************************************
11-21-2023
Conversion changes have been made.
Generate local display using 'cologne'
Compare kosha-dev display with 'cologne' display.
python /c/xampp/htdocs/cologne/xmlvalidate.py cologne/abch/pywork/abch.xml cologne/abch/pywork/abch.dtd
# ok

URLS:
http://localhost/kosha-dev/v5.1/apps/abch/web/
http://localhost/kosha-dev/v5.1/convert/cologne/abch/web/
Notes:
1. WorldCat reference link on http://localhost/kosha-dev/v5.1/convert/cologne/abch/web/index.php
2. dbg stmts in basicadjust, basicdisplay  webtc/dbg_apidev.txt getword_data.php

cp revise/new/basicadjust.php cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
cp revise/new/basicdisplay.php cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicdisplay.php
cp revise/new/web_getword_data.php cologne/csl-websanlexicon/v02/makotemplates/web/webtc/getword_data.php
sh redo_abch_cologne.sh
python /c/xampp/htdocs/cologne/xmlvalidate.py cologne/abch/pywork/abch.xml cologne/abch/pywork/abch.dtd
*********************************************************************

install to xampp.
This involves
* copying from revise/new/X to local repositories csl-orig, csl-pywork, and csl-websanlexicon
* copying from csl-websanlexicon to csl-apidev

Also remaking not only abch, but other dictionaries (to be sure no problem anywhere)
Construct script install_cologne.sh, then run it.
  This copies all the changed files, mostly from revise/new/ directory, to htdocs/cologne/...

------------------------
cd /c/xampp/htdocs/kosha-dev/v5.1/convert # this directory

RECREATE using local /c/xampp/htdocs/kosha-dev/v5.1/convert
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# put abch into redo_xampp_all.sh
sh generate_dict.sh abch  ../../abch
# redo_cologne_all.sh  NOTE: 2023
sh generate_dict.sh abch  ../../ABCHScan/2023/
sh xmlchk_xampp.sh abch
# ok

# try local displays at url localhost/cologne/abch/web/
# ok so far


# recreate local versions of a few other dictionaries
#  check they are working as normal in csl-pywork/v02
sh generate_dict.sh mw  ../../tempmw_abch

Found an error:
File "C:\xampp\htdocs\cologne\tempmw_abch\pywork\sqlite\sqlite.py", line 94, in <module>
    line = line0.rstrip('\r\n')
NameError: name 'line0' is not defined

Revised /c/xampp/htdocs/cologne/csl-pywork/v02/makotemplates/pywork/sqlite/sqlite.py
Now mw seems to be fine.
rm -r ../../tempmw_abch  # remove test version
-----------------------------
# try pw
sh generate_dict.sh pw  ../../temppw_abch

# Seems ok.
 rm -r ../../temppw_abch  # remove test version

-----------------------------
# try pwg
sh generate_dict.sh pwg  ../../temppwg_abch

# Seems ok.
 rm -r ../../temppwg_abch  # remove test version

-----------------------------
# try gra
sh generate_dict.sh gra  ../../tempgra_abch

# Seems ok.
 rm -r ../../tempgra_abch  # remove test version

-----------------------------
# try skd
sh generate_dict.sh skd  ../../tempskd_abch

# Seems ok.
 rm -r ../../tempskd_abch  # remove test version

-----------------------------
# try lrv
sh generate_dict.sh lrv  ../../templrv_abch

# Seems ok.
 rm -r ../../templrv_abch  # remove test version

------------------------------
cp -r ../prep/abch /c/xampp/htdocs/cologne/csl-orig/v02/abch/prep
# Dhaval considers abch1.txt the 'primary' version.
# prep/redo.sh in prep converts abch1.txt to the primary version abch.txt for cdsl system
# currently redo.sh constructs prep/temp_abch.txt.
#   we may want to modify script to further copy this to ../abch.txt 

------------------------------------------------------
# several additional steps for simple-search to get
# simple-search hwnorm1c.sqlite
# repository hwnorm1
cd /c/xampp/htdocs/cologne/hwnorm1
# edit sanhw1/sanhw1.py
# 1. add "ABCH":"2023" to dictyear
# 2. add "ABCH" to san_san_dicts

# Then, follow instructions of hwnorm1/sanhw1/readme.txt, namely

cd sanhw1
sh redo.sh
mv hwnorm1c.sqlite ../../csl-apidev/simple-search/hwnorm1/

# push hwnorm1 repository to github
# hownorm1c.txt, sanhw1.py, sanhw1.txt are modified
git add .
git commit -m "ABCH: Ref: https://github.com/funderburkjim/kosha-dev/issues/23"
git push
#  3 files changed, 25054 insertions(+), 22983 deletions(-)

------------------------------
11-24-2023 csl-apidev

1.  copy basicadjust, basicdisplay from csl-websanlexicon to csl-apidev
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh apidev_copy.sh

cd /c/xampp/htdocs/kosha-dev/v5.1/convert/
2. add ABCH to csl-apidev/sample/dictnames.js
  for simple-search
3. add ABCH to csl-apidev/dictinfo.php
------------------------------
# push to Github
cd /c/xampp/htdocs/cologne/csl-orig/v02
git pull # as precaution
git add .
git commit -m "ABCH: Ref: https://github.com/funderburkjim/kosha-dev/issues/23"
git push

cd /c/xampp/htdocs/cologne/csl-pywork/v02
git pull # as precaution
git add .
git commit -m "ABCH: Ref: https://github.com/funderburkjim/kosha-dev/issues/23"
# 16 files changed, 571 insertions(+), 122 deletions(-)
git push

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
git pull # as precaution
git add .
git commit -m "ABCH: Ref: https://github.com/funderburkjim/kosha-dev/issues/23"
# 10 files changed, 342 insertions(+), 108 deletions(-)
git push

cd /c/xampp/htdocs/cologne/csl-apidev
git pull # as precaution
git add .
git commit -m "ABCH: Ref: https://github.com/funderburkjim/kosha-dev/issues/23"
# 3 files changed, 224 insertions(+), 92 deletions(-)
git push

----------------------------------
pull to cologne
# ssh connection to cologne server
# cd to scans directory
cd csl-orig
git pull
# 16 files changed, 27048 insertions(+)

cd ../csl-pywork
git pull
# 16 files changed, 571 insertions(+), 122 deletions(-)

cd ../csl-websanlexicon
git pull
#  10 files changed, 342 insertions(+), 108 deletions(-)

# generate display(s)
cd ../csl-pywork/v02
grep 'abch' redo_cologne_all.sh

sh generate_dict.sh abch  ../../ABCHScan/2023/
# check display(s)
https://sanskrit-lexicon.uni-koeln.de/scans/ABCHScan/2023/web/

#simple-search
cd ../../csl-apidev
git pull
#  3 files changed, 224 insertions(+), 92 deletions(-)

# push this repo to github
cd /c/xampp/htdocs/kosha-dev/v5.1/convert/
git add .
git commit -m "convert dev version 5.1 to cdsl
Ref: https://github.com/funderburkjim/kosha-dev/issues/23"
git push

THIS ENDS THE DOCUMENTATION BY JIM FOR ABCH DICTIONARY
----------------------------------

# The following are some hecks for future dictionaries.
# For updating only the required part of csl-pywork and csl-websanlexicon in kosha-dev/v5.1/convert/cologne folder.
Update sanskrit-lexicon/csl-pywork repo. (Manual)
Open Meld and compare the differences in sanskrit-lexicon/csl-pywork/v02 and convert/csl-pywork/v02
Whenever there is difference, Meld will show with blue or green colour. Shift on the "Right Arrow" on the top to copy the latest one to the convert/csl-pywork/v02 folder.
Do the same for csl-websanlexicon and csl-orig repositories.
