#!/bin/bash

echo "updating .mf$1 using .pn$1 ..."
cp .pn$1 pn$1
cp .mfb$1 mf$1


a=($(head -n 1 pn$1))
N=${#a[@]}

while [ $N -gt 0 ]; do


	sed -i 1d pn$1
	F=${a[0]}
	B=${a[0]%.*}
	E=${a[0]##*.}


	if [ $E = $F ]; then
		E=
	fi


	sed -i "26s/$/ ${F}/" mf$1

	D=${a[@]:1}


	echo -e "\n${F}: ../.${F}ctrl ${D}" >> mf$1
	echo -ne "\\techo \"" >> mf$1
	for d in $D; do
		echo -n "\$(DOT)/${d}\n" >> mf$1
	done
	echo -ne "\$(DOT)/${F}\" > ../.${F}i\n" >> mf$1


	echo -e "\tif [ \$\${GATE} -eq 1 ]; then \\" >> mf$1
	echo -e "\t\techo term > ../.${F}i; \\" >> mf$1
	echo -e "\t\trm ../.${F}ctrl ../.${F}i; \\" >> mf$1
	echo -e "\tfi\n" >> mf$1


	echo -e "../.${F}ctrl: .lib/plib/${B}_${E}bd.py" >> mf$1
	echo -e "\tDOT=\$\${DOTDOT}; \\" >> mf$1
	echo -e "\t./.lib/${F}fire.sh\n" >> mf$1
	echo -e "\t\$(eval GATE=1)" >> mf$1


	echo -e "#!/bin/bash\n\n\n" > .lib/${F}fire.sh
	chmod +x .lib/${F}fire.sh
	echo "export PYTHONPATH=$(pwd)/.lib/plib" >> .lib/${F}fire.sh
	echo "mkfifo \"\${DOT}/.${F}i\" 2>/dev/null" >> .lib/${F}fire.sh
	echo "py -m ${B}_${E}bd \${DOT}/.${F}i &" >> .lib/${F}fire.sh
	echo "echo \$! > \${DOT}/.${F}ctrl" >> .lib/${F}fire.sh


	echo -e "#!/bin/bash\n\n\n" > .lib/${F}kill.sh
	chmod +x .lib/${F}kill.sh
	echo "echo term > \${DOT}/.${F}i" >> .lib/${F}kill.sh
	echo "rm \${DOT}/.${F}i \${DOT}/.${F}ctrl" >> .lib/${F}kill.sh


	a=($(head -n 1 pn$1))
	N=${#a[@]}


done
cp mf$1 .mf$1
rm pn$1 mf$1
