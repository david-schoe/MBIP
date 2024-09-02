#!/bin/bash



export PYTHONPATH=/home/davey_schoe/Research/PY/MBIP/CIR/BUBBLES/.lib/plib
mkfifo "${DOT}/.Mi" 2>/dev/null
py -m "M_bd" "${DOT}/.Mi" &
echo $! > "${DOT}/.Mctrl"
wait -f $(cat ${DOT}/.Mctrl)
rm ${DOT}/.Mi ${DOT}/.Mctrl
