#!/bin/bash

rmc=0

for r in ${RM[@]}; do
	tar -cf "/tmp/BU/bu_$(cat .on0)$r.tar" "./$(cat .on0)$r" 2> /dev/null
	rm -r "./$(cat .on0)${r}" 2> /dev/null
	if [ $? -eq 0 ]; then
		echo "Removing $(cat .on0)$r ..." 1>&2
	else
		echo "Failure ..." 1>&2
		continue
	fi
	echo "/$r/d;" 1>> srl
done
sed -i "$(cat srl 2>/dev/null)" .objn 2>/dev/null
sed -i "$(cat srl 2>/dev/null)" .objd 2>/dev/null
rm srl 2>/dev/null

