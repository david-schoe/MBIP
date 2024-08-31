#!/bin/bash


function move() {
	echo $3 >> objnN
	echo $2 >> objdN
	mv $1 $2 2>/dev/null
	if [ $? -eq 0 ]; then
		echo "Moving $1 to $2  ..." 1>&2
	else
		echo "Did not move $1"
	fi }
n=0;

for obj in $(cat .objd); do
	str=("$obj" "$(cat .on0)$n")
	move ${str[0]} ${str[1]} $n
	n=$((n+1))
done

mv objnN .objn 2>/dev/null
mv objdN .objd 2>/dev/null
echo $n > .nobjn
