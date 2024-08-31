#!/bin/bash
on=$(cat .nobjn)
od="$(cat .on0)${on}"
echo $on >> .objn
echo $od >> .objd
echo $((on+1)) > .nobjn
