dict=$1
cd prep/$dict
sh redo.sh
cd ../../   # back to kosha-dev/v4
echo "pwd:"
pwd
cd csl-pywork
sh generate_dict.sh $dict ../apps/$dict

