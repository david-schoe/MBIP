#!/bin/bash



export PYTHONPATH=/home/davey_schoe/Research/PY/MBIP/CIR/BUBBLES/.lib/plib
mkfifo "${DOT}/.cont.pngi" 2>/dev/null
py -m cont_pngbd ${DOT}/.cont.pngi &
echo $! > ${DOT}/.cont.pngctrl