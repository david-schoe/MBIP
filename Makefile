###
																###
###			A CHEAP WAY TO CONFIGURE THE BUILD ... ... ... USER MUST HAVE NUMPY AND PILLOW
																###
###
																###




export DOT=$(shell pwd)

all: /bin/py /bin/ffmpeg ./CIR/BUBBLES/VIDS ./CIR/BUBBLES/Makefile

/bin/py: /bin/python3
	ln -s /bin/python3 py

/bin/python3:
	apt-get install python3

/bin/ffmpeg:
	apt-get install ffmpeg

./CIR/BUBBLES/VIDS:
	cp -r ./CIR/BUBBLES/.VIDS  ./CIR/BUBBLES/VIDS

./CIR/BUBBLES/Makefile:
	cp  ./CIR/BUBBLES/.mf  ./CIR/BUBBLES/Makefile
