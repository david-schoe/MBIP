#!/bin/bash

i=
./.lib/mup.sh $i
i=0
c=$(cat .mfc)
while [ $i -lt $((c+1)) ]; do
	./.lib/mup.sh $i
	i=$((i+1))
done
