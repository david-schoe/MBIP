###
																###
###			A CHEAP WAY TO CONFIGURE THE BUILD ... ... ... USER MUST HAVE NUMPY AND PILLOW
																###
###
																###




export DOT=$(shell pwd)

all: /bin/py /bin/ffmpeg

/bin/py: /bin/python3
	ln -s /bin/python3 py

/bin/python3:
	apt-get install python3

/bin/ffmpeg:
	apt-get install ffmpeg
