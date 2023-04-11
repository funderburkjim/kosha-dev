# coding=utf-8
"""convert_to_xml1.py
Usage - python3 xml1_to_xml.py xxx1.xml xxx2.xml

Author - Dhaval Patel. April 02, 2023

Convert xxx1.xml to xxx.xml.
Revert the changes made from xxx1.xml.
Store the result in xxx2.xml.
Ideally, xxx.xml and xxx2.xml should be identical.
"""
from __future__ import print_function
import sys, re,codecs


def reverse_verse(verse):
	verse = verse.replace('<br/>', '</s></entrydetail><entrydetail><s>')
	verse = '<entrydetails><entrydetail><s>' + verse + '</s></entrydetail></entrydetails>'
	return verse


if __name__ == "__main__":
	filein = sys.argv[1]
	fileout = sys.argv[2]
	fin = codecs.open(filein, 'r', 'utf-8')
	fout = codecs.open(fileout, 'w', 'utf-8')
	# First pass to get verses
	# Store verses with 'L' as key and verse as value.
	verses = {}
	start = False
	for lin in fin:
		lin = lin.rstrip('\r\n')
		if lin.startswith('<versedetails>'):
			start = True
		if start:
			m = re.search('<vd><L>(.*?)</L><v>(.*?)</v></vd>', lin)
			if m:
				lnum = m.group(1)
				verse = m.group(2)
				verse = reverse_verse(verse)
				verses[lnum] = verse
	fin.close()
	# Second pass to supply verses based on 'L'
	# <H1><h><key1>ka</key1><key2>ka</key2></h><body><hds><hd><hw>ka-puM</hw><m>sUrya,veDas</m></hd><hd><hw>ka-klI</hw><m>suKa,mastaka,jala</m></hd></hds></body><tail><L>1</L><pc>140</pc></tail></H1>
	# to
	# <H1><h><key1>ka</key1><key2>ka</key2></h><body><hwdetails><hwdetail><hw><s>ka-puM</s></hw><meaning><s>sUrya,veDas</s></meaning></hwdetail><hwdetail><hw><s>ka-klI</s></hw><meaning><s>suKa,mastaka,jala</s></meaning></hwdetail></hwdetails><entrydetails><entrydetail><s>sUrye veDasi vAyO kaH kaM suKe mastake jale .</s></entrydetail><entrydetail><s>anuzwubyaSasoH Sloko lokastu Buvane jane .. 1 ..</s></entrydetail></entrydetails></body><tail><L>1</L><pc>140</pc></tail></H1>
	fin = codecs.open(filein, 'r', 'utf-8')
	start = False
	end = False
	for lin in fin:
		lin = lin.rstrip('\r\n')
		lin = lin.replace('anhk1.dtd','anhk.dtd')
		if lin.startswith('<H1details>'):
			start = True
			continue
		if lin.startswith('</H1details>'):
			start = False
			continue
		if lin.startswith('<versedetails>'):
			continue
		if lin.startswith('</versedetails>'):
			continue
		if lin.startswith('<vd>'):
			continue
		if start:
			m = re.search('<L>(.*?)</L>', lin)
			if m:
				lnum = m.group(1)
				verse = verses[lnum]
			lin = lin.replace('<hds>', '<hwdetails>')
			lin = lin.replace('</hds>', '</hwdetails>')
			lin = lin.replace('<hd>', '<hwdetail>')
			lin = lin.replace('</hd>', '</hwdetail>')
			lin = lin.replace('<m>', '<meaning>')
			lin = lin.replace('</m>', '</meaning>')
			lin = re.sub('<hw>(.*?)</hw>', '<hw><s>\g<1></s></hw>', lin)
			lin = re.sub('<meaning>(.*?)</meaning>', '<meaning><s>\g<1></s></meaning>', lin)
			lin = re.sub('</hwdetails></body><tail><L>', '</hwdetails>' + verse + '</body><tail><L>', lin)
		fout.write(lin + '\n')
		
	fin.close()
	fout.close()

