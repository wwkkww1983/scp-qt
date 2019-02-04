LINE="$1"
files=`grep -r "$LINE" . | cut -f1 -d: | uniq`
f=()
for i in $files; do
	f+=("$i")
	echo $i
done
vim ${f[@]}
