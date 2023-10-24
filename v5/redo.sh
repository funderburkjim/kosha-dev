dict=$1
cd prep/$dict
sh redo.sh
cd ../../   # back to kosha-dev/v4
echo "pwd:"
pwd
echo "copy prep/$dict/$dict.txt to csl-orig/$dict/$dict.txt"
cp prep/$dict/$dict.txt csl-orig/$dict/$dict.txt
echo "Reconstruct app for $dict"
cd csl-pywork
sh generate_dict.sh $dict ../apps/$dict

