# kosha-dev
Develop xml and html for anekArthaka and samAnArthaka Sanskrit dictionaries

## v0 version
```
# generate the dictionary displays, using dictionary code 'harsa'
# the apps directory is not tracked by git.
cd v0/csl-pywork/
sh generate_dict.sh harsa  ../apps/harsa
# Access the displays via browser, e.g. at url
http://localhost/kosha-dev/v0/apps/harsa/web/
```

## v1 version
Addresses problems:
* list display order #5
* missing meanings #6
* advanced search order #7
```
# generate the dictionary displays, using dictionary code 'harsa'
# the apps directory is not tracked by git.
cd v1/csl-pywork/
sh generate_dict.sh harsa  ../apps/harsa
# Access the displays via browser, e.g. at url
http://localhost/kosha-dev/v1/apps/harsa/web/
```

## v2 version
```
 provides anhk.xml and anhk1.xml.
   anhk.xml is form assumed by CDSL displays.
   anhk1.xml is alternate format useful to Dhaval.
   conversion between the two is programmatic and shows they are equivalent.
```
## v3 version
```
  Change dictionary name to ANHK.
  Refer https://github.com/sanskrit-lexicon/COLOGNE/issues/405
```
## v4 version
Add dictionary abch (Abhidhānacintāmaṇi of Hemacandrācārya)

Primary file source is v4/prep/abch/abch1.txt  (Devanagari).

To reconstruct the app
### assume in directory v4  of repository
sh redo.sh abch
```
this script does the following:
# a. construct abch.txt (slp1). This form is basis for other steps
cd prep/abch
sh redo.sh
# b. abch.txt from prep to csl-orig/abch
cp prep/abch.txt csl-orig/abch/
# c. Reconstruct displays in v4/apps/abch/web/
cd ../../   # back to kosha-dev/v4
cd csl-pywork
sh generate_dict_sh abch ../apps/abch
```
