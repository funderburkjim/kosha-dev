echo "BEGIN convert anhk1.txt to slp1 version anhk.txt"
python convert.py deva,slp1 anhk1.txt anhk.txt
# check invertability
python convert.py slp1,deva anhk.txt temp_anhk1.txt
diff anhk1.txt temp_anhk1.txt
# should be no difference
rm temp_anhk1.txt
echo "END convert anhk1.txt to slp1 version anhk.txt"

