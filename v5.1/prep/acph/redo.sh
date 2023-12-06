echo "BEGIN convert acph1.txt to version acph.txt"
echo "acph0.txt intermediate slp1 version"
python convert.py deva,slp1 acph1.txt acph0.txt
# check invertability
python convert.py slp1,deva acph0.txt temp_acph1.txt
diff acph1.txt temp_acph1.txt > tempdiff.txt
wc -l tempdiff.txt
# should be no difference
# Additional changes
python addinfo.py acph0.txt acph.txt
echo "END convert acph1.txt to version acph.txt"

