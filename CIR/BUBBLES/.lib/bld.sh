#!/bin/bash

cp .pn0 l0
cp .pn0 l1

N=$(wc -l < l0)

n=0;
while [ $n -lt $N ]; do
	p=($(head -n 1 l0))
	./.lib/${p}fire.sh
	sed 1d l0
	n=$((n+1))
done

for bld in $(cat bld_specs); do
	make obj SPEC="${bld}"
done;

n=0;
while [ $n -lt $N ]; do
	p=($(head -n 1 l1))
	./.lib/${p}kill.sh
	sed 1d l1
	n=$((n+1))
done

rm l0 l1

touch .timestamp
