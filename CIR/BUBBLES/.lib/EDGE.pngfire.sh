#!/bin/bash



export PYTHONPATH=/home/davey_schoe/Research/PY/MBIP/CIR/BUBBLES/.lib/plib
mkfifo "${DOT}/.EDGE.pngi" 2>/dev/null
py -m "EDGE_pngbd" "${DOT}/.EDGE.pngi" &
echo $! > "${DOT}/.EDGE.pngctrl"
wait -f $(cat ${DOT}/.EDGE.pngctrl)
rm ${DOT}/.EDGE.pngi ${DOT}/.EDGE.pngctrl
