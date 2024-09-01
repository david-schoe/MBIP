#!/bin/bash

export SPEC="$(cat .sn0)"

./.lib/${SPEC}.sh

for spec in $(ls "${SPEC}S"); do
	echo "${DOT}/${SPEC}S/${spec}" >> unsorted
done

sort -V unsorted > bld_specs
rm unsorted
