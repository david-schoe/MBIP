#!/bin/bash

cp Makefile .mf
echo ${DOT}
tar -cf "/tmp/BU/bu_dot.tar" "${DOT}" #2> /dev/null
if [ $? -eq 0 ]; then
        echo "Backing ${DOT} to /tmp/BU/bu_root.tar ..." 1>&2
else
	echo "Failed to backup root directory ... clean cancelled ..." 1>&2
	exit
fi

for file in $(ls); do
        rm -r "${file}" 2> /dev/null
	if [ $? -eq 0 ]; then
                echo "Removing ${file} ..." 1>&2
	else
		echo "Failed to remove ${file} ..." 1>&2
	fi
	((n++))
done
rm -r .objn .objd .nobjn 2> /dev/null
