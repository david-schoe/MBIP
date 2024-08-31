#!/bin/bash

export OBJ="$(tail -n 1 .objd)"

ext=${SPEC##*.}
nameext=${SPEC##*/}
name=${name##*.}


echo $ext > "${DOT}/${OBJ}/ext"
echo $nameext > "${DOT}/${OBJ}/name"
cp $SPEC "${DOT}/${OBJ}/$(cat .sn0).${ext}"
echo $DOT > "${DOT}/${OBJ}/.dotdot"

./.lib/nup.sh mf; ./.lib/nup.sh on; ./.lib/nup.sh sn; ./.lib/nup.sh pn

mv "${DOT}/${OBJ}/.mf" "${DOT}/${OBJ}/Makefile"
ln -s "${DOT}/.lib" "${DOT}/${OBJ}/.lib"

make -C $OBJ
