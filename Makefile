###
																###
###			A CHEAP WAY TO CONFIGURE THE BUILD ... ... ... USER MUST HAVE NUMPY AND CV2
																###
###
																###




export DOT=$(shell pwd)

all: /bin/py /bin/ffmpeg ./CIR/BUBBLES/vids ./CIR/BUBBLES/Makefile

/bin/py: /bin/python3
	ln -s /bin/python3 py

/bin/python3:
	apt-get install python3

/bin/ffmpeg:
	apt-get install ffmpeg

./CIR/BUBBLES/vids:
	cp -r ./CIR/.vids  ./CIR/vids

./CIR/BUBBLES/Makefile:
	cp  ./CIR/.mf  ./CIR/Makefile
