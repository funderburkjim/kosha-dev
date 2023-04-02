# coding=utf-8
"""convert_to_xml1.py
Usage - python3 xml_to_xml1.py xxx.xml xxx1.xml

Author - Dhaval Patel. March 26, 2023

Convert xxx.xml to xxx1.xml.
This is a unique problem relevant to anekArthaka and samAnArthaka koshas.
There are multiple headwords per verse.
One should be able to access the verse through any of these headwords.
There may be 20-30 headwords in a verse too.
Currently, xxx.xml writes the verse with each of those 20-30 headwords.

Ideally, it should be kept separate, to keep the file size compact.

xxx1.xml is the compressed version of xxx.xml (without duplication)
"""
from __future__ import print_function
import xml.etree.ElementTree as ET
import sys, re,codecs

if __name__ == "__main__":
	filein = sys.argv[1]
	fileout = sys.argv[2]
	fin = codecs.open(filein, 'r', 'utf-8')
	fout = codecs.open(fileout, 'w', 'utf-8')
	verses = []
	for lin in fin:
		lin = lin.rstrip('\r\n')
		if lin.startswith('<H'):
			# <entrydetails><entrydetail><s>sUrye veDasi vAyO kaH kaM suKe mastake jale .</s></entrydetail><entrydetail><s>anuzwubyaSasoH Sloko lokastu Buvane jane .. 1 ..</s></entrydetail></entrydetails></body><tail><L>1</L>
			# to
			# </body><tail><L>1</L>
			# and store the following in separate xml tag
			# <eds><L>1</L>sUrye veDasi vAyO kaH kaM suKe mastake jale .<br/>anuzwubyaSasoH Sloko lokastu Buvane jane .. 1 ..</eds>
			m = re.search('<entrydetails>(.*?)</entrydetails></body><tail><L>(.*?)</L>', lin)
			verse = m.group(1)
			verse = verse.replace('<entrydetails>', '<eds>')
			verse = verse.replace('</entrydetails>', '</eds>')
			verse = verse.replace('<entrydetail>', '')
			verse = verse.replace('</entrydetail>', '')
			verse = verse.replace('</s><s>', '<br/>')
			verse = verse.replace('<s>', '')
			verse = verse.replace('</s>', '')
			lnum = m.group(2)
			if (lnum, verse) not in verses:
				verses.append((lnum, verse))
			# Change the line containing <h> tag
			lin = re.sub('<entrydetails>.*?</entrydetails>', '', lin)
			# <body><hwdetails><hwdetail><hw><s>ka-puM</s></hw><meaning><s>sUrya,veDas</s></meaning></hwdetail><hwdetail><hw><s>ka-klI</s></hw><meaning><s>suKa,mastaka,jala</s></meaning></hwdetail></hwdetails></body>
			# to
			# <body><hds><hd><hw>ka-puM</hw><m>sUrya,veDas</m></hd><hd><hw>ka-klI</hw><m>suKa,mastaka,jala</m></hd></hds></body>
			lin = lin.replace('<hwdetails>', '<hds>')
			lin = lin.replace('</hwdetails>', '</hds>')
			lin = lin.replace('<hwdetail>', '<hd>')
			lin = lin.replace('</hwdetail>', '</hd>')
			lin = lin.replace('<meaning>', '<m>')
			lin = lin.replace('</meaning>', '</m>')
			lin = lin.replace('<s>', '')
			lin = lin.replace('</s>', '')
			fout.write(lin + '\n')
		elif lin.startswith('</'):
			fout.write('</H1details>' + '\n')
			fout.write('<versedetails>' + '\n')
			for (lnum, verse) in verses:
				fout.write('<vd><L>' + lnum + '</L><v>' + verse + '</v></vd>\n')
			fout.write('</versedetails>\n')
			fout.write(lin + '\n')
		elif re.match('<[a-z]', lin):
			fout.write(lin + '\n')
			fout.write('<H1details>' + '\n')
		else:
			fout.write(lin + '\n')		
	fin.close()
	fout.close()
