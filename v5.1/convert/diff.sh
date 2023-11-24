file=$1
tmp=kosh/${file}
echo "tmp = $tmp"

cmd="diff kosh/$file cologne/$file"
echo "cmd = $cmd"

$cmd 
