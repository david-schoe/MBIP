#!/bin/bash

cp .pn0 l0
cp .pn0 l1

N=$(grep . l0 | wc -l)
n=0;
while [ $n -lt $N ]; do
	p=($(head -n 1 l0))
	./.lib/${p}fire.sh &
	sed -i 1d l0
	n=$((n+1))
done
for spec in $(cat bld_specs); do
	make obj SPEC=$spec
done;

n=0;

while [ $n -lt $N ]; do
	p=($(head -n 1 l1))
	echo term > .${p}i
	sed -i 1d l1
	n=$((n+1))
done

rm l0 l1
touch .timestamp
