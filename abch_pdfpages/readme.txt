aBiDAnacintAmaRi of hemacandra
pdf source:
https://archive.org/download/abhidhanasangrahapanditsivadattadurgaprasadakasinathpandurangparabnirnayasagar_613_y/Abhidhana%20Sangraha%20Pandit%20Sivadatta%20Durga%20Prasada%20Kasinath%20Pandurang%20Parab%20Nirnaya%20Sagar.pdf

online display link
 https://archive.org/details/abhidhanasangrahapanditsivadattadurgaprasadakasinathpandurangparabnirnayasagar_613_y/page/n136/mode/1up

Rename pdf download:
 OLD name: "Abhidhana Sangraha Pandit Sivadatta Durga Prasada Kasinath Pandurang Parab Nirnaya Sagar.pdf"
 NEW name: archive.pdf
 
Ref: https://github.com/funderburkjim/kosha-dev/issues/12
  Page 135 onwards.

=========================================================================
archive_pages directory
open archive.pdf in Adobe Acrobat 9.0
Document/Extract Pages
Extract Pages from 1 to 315, Extract Pages As Separate Files.

Extract individual pages as pdf files in archive_pages directory.
File names are 'archive 1.pdf', ..., 'archive 315.pdf'.

=========================================================================
Relevant pages for ABCH
Page  description
----  -----------
135   title (Roman alphabet)
136   almost blank
137   title (Devanagari)
138   blank
139   hemacandraH 1
140   hemacandraH 2
141   hemacandraH 3
142   hemacandraH 4
143   hemacandraH 5
144   hemacandraH 6
145   Preface, page 1
146   Preface, page 2
147   Preface, page 3
148   Preface, page 4
; devakARqaH
149   5  # L=1 in abch.txt
150   6
...
; martyakARqaH
161   17
...
180   36
; tiryakkARqaH
181   37
...

196   52
; narakakARqaH
; sAmAnyakARqaH
197   53
...
201   57
202   58
; the end (of abch.txt)
===========
203 pariSizWaH page 1   

============================================================
create a script to
a. copy (and rename) files from archive_pages directory to pdfpages directory.
b. create pdffiles.txt

python make_renum.py renum.sh pdffiles.txt

Then run the script, to create pdfpages directory.
sh renum.sh

