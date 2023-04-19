echo "BEGIN convert abch1.txt to slp1 version abch.txt"
python convert.py deva,slp1 abch1.txt abch.txt
# check invertability
python convert.py slp1,deva abch.txt temp_abch1.txt
diff abch1.txt temp_abch1.txt
# should be no difference
rm temp_abch1.txt
echo "END convert abch1.txt to slp1 version abch.txt"

