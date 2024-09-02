#!/bin/bash



export PYTHONPATH=/home/davey_schoe/Research/PY/MBIP/CIR/BUBBLES/.lib/plib
mkfifo "${DOT}/.CONT.pngi" 2>/dev/null
py -m "CONT_pngbd" "${DOT}/.CONT.pngi" &
echo $! > "${DOT}/.CONT.pngctrl"
wait -f $(cat ${DOT}/.CONT.pngctrl)
rm ${DOT}/.CONT.pngi ${DOT}/.CONT.pngctrl
