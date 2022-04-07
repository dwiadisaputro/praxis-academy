!/bin/bash
for item in $(sudo find $1 -name *.java)
do
	if [ -f $item ]; then
	echo " Ada file Java pada direktori {$item}"
	fi
done
