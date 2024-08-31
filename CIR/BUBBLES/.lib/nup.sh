#!/bin/bash

b=-1; c=$(cat "${DOT}/.$1c"); while [ $c -gt 0 ]; do
        if [ $b -eq -1 ]; then
                echo $((c+b)) >"${DOT}/${OBJ}/.$1c"
        fi
        b=$((c-1)); ln "${DOT}/.$1$c" "${DOT}/${OBJ}/.$1$b"
        c=$((c-1))
done


ln "${DOT}/.$10" "${DOT}/${OBJ}/.$1"
