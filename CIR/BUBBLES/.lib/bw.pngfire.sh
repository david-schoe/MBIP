#!/bin/bash



export PYTHONPATH=/home/davey_schoe/Research/PY/MBIP/CIR/BUBBLES/.lib/plib
mkfifo "${DOT}/.bw.pngi" 2>/dev/null
py -m bw_pngbd ${DOT}/.bw.pngi &
echo $! > ${DOT}/.bw.pngctrl
