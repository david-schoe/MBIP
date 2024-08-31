#!/bin/bash

SPEC="$(cat .sn0)"
mkdir "${SPEC}s"

FI="${DOT}/$(cat .sn).$(cat ext)"
FO="${SPEC}%d.png"

cd "${SPEC}s" && ffmpeg -i $FI $FO && cd ..

for spec in $(ls "${SPEC}s"); do
	echo "${DOT}/${SPEC}s/${spec}" >> unsorted
done

sort -V unsorted > bld_specs

