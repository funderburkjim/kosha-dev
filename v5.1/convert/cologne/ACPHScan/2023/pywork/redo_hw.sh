echo "BEGIN redo_hw.sh"
echo "construct xxxhw.txt"
echo "BEGIN hw.py"
python3 hw.py ../orig/acph.txt hwextra/acph_hwextra.txt acphhw.txt
echo "END hw.py"
echo ""
echo "BEGIN hw2.py"
python3 hw2.py acphhw.txt acphhw2.txt
echo "END hw2.py"

echo "BEGIN hw0.py"
python3 hw0.py acphhw.txt acphhw0.txt
echo "END hw0.py"

# both hw2.txt and hw0.txt are easily constructed from hw.txt
# not clear, therefore, that either hw2.txt or hw0.txt is needed directly
# We would need to change the 'awork/sanhw1.py' program. 
# To avoid this change might be sufficient reason to keep hw2.txt and hw0.txt
#echo "construct xxxhw2.txt"
#echo "construct xxxhw0.txt"
echo "END  redo_hw.sh"
