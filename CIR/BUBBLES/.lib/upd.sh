#!/bin/bash


cp .pn0 l0
cp .pn0 l1

N=$(wc -l < l0)

n=0;
while [ $n -lt $N ]; do
	p=($(head -n 1 l0))
	./.lib/${p}fire.sh &
	sed -i 1d l0
	n=$((n+1))
done

for obj in $(cat .objd); do
	echo "updating $obj ..."
	echo $obj
	make -C $obj
done;

n=0;
while [ $n -lt $N ]; do
	p=($(head -n 1 l1))
	echo term > .${p}i
	sed -i 1d l1
	n=$((n+1))
done
rm l0 l1

