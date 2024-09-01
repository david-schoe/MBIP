mkdir "${SPEC}S"

FI="${DOT}/$(cat .sn).$(cat ext)"
FO="${SPEC}%d.png"

cd "${SPEC}S" && ffmpeg -i $FI $FO && cd ..
