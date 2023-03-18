Harṣakīrti's Anekārthanāmamālā
# --------------
# redo.sh generates harsa.txt
# convert anhk1.txt to slp1 version harsa.txt
python convert.py deva,slp1 anhk1.txt harsa.txt
# check invertability
python convert.py slp1,deva harsa.txt temp_anhk1.txt
diff anhk1.txt temp_anhk1.txt
# should be no difference
rm temp_anhk1.txt

# --------------
