echo "BEGIN convert acsj1.txt to version acsj.txt"
echo "acsj0.txt intermediate slp1 version"
# check invertability
python convert.py deva,slp1 acsj1.txt acsj0.txt
python convert.py slp1,deva acsj0.txt temp_acsj1.txt
diff acsj1.txt temp_acsj1.txt > tempdiff.txt
wc -l tempdiff.txt
# should be no difference
# Additional changes
python addinfo.py acsj0.txt acsj.txt
echo "END convert acsj1.txt to version acsj.txt"

