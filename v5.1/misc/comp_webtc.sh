dir2="/c/xampp/htdocs/kosha-dev/v5/apps/abch/web/webtc"
dir1="/c/xampp/htdocs/kosha-dev/v5/csl-websanlexicon/makotemplates/web/webtc"
cd $dir2
files=`ls *.php`

for file in $files
 do
 echo "$file"	    
 file1="${dir1}/${file}"
 file2="$dir2/$file"
 echo "*************************************************************"
 echo "diff for $file"
 diff="diff $file1 $file2"
 ndiff=`$diff | wc -l`
 if [ $ndiff == 0 ]
 then
     echo "no diff"
 else
     echo "ndiff=$ndiff"
     echo $diff
     $diff
 fi
 
done

    
