echo "BEGIN convert abch1.txt to version abch.txt"
echo "abch0.txt intermediate slp1 version"
python convert.py deva,slp1 abch1.txt abch0.txt
# check invertability
python convert.py slp1,deva abch0.txt temp_abch1.txt
diff abch1.txt temp_abch1.txt > tempdiff.txt
wc -l tempdiff.txt
# should be no difference
# Additional changes
python addinfo.py abch0.txt abch.txt
echo "END convert abch1.txt to version abch.txt"

