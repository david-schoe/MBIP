import sys
import os
import cv2 as cv
import numpy as np


while (1):

	# Open the fifo that is passed as an argument variable on the command line

	i = os.open(sys.argv[1], os.O_RDONLY);

	# Attempt to read from the fifo ( will be unable to read until the fifo has been opened for writing by another process ( typically the calling process ) )

	buf = os.read(i,256);


	# Convert the binary "buf" into a string

	frm = buf.decode('utf-8').split('\n')[0];

	# The string is the directory of interest ( a frame )... so begin image processing from here on



	# Open the "can" image in the frame

	can = cv.imread(f"{frm}/can.png",cv.IMREAD_GRAYSCALE);
	vis = cv.imread(f"{frm}/img.png");

	rowi,coli = np.indices(np.shape(can));

#	rowo = np.flatten(np.bitwise_and(rowi,can));
#	colo = np.bitwise_and(coli,can);

#	rowo = rowo.astype(int);
#	colo = colo.astype(int);

#	rc = np.uint8(np.round(np.sum(rowo)/len(rowo)));
#	cc = np.uint8(np.round(np.sum(colo)/len(colo)));

#	x = rowo - rc;
#	y = cc - colo;








	mask = can != 0;
	rowo = rowi[mask];
	colo = coli[mask];

	rc = np.uint8(np.round(np.sum(rowo)/len(rowo)));
	cc = np.uint8(np.round(np.sum(colo)/len(colo)));

	x = rowo - rc;
	y = cc - colo;

	rad = (x**2 + y**2)**.5;
	rada = np.sum(rad)/len(rad);
	radd = rad-rada;
	phi = np.arctan2(y,x);

	sort = np.argsort(phi);

	rad = rad[sort];
	radd = radd[sort];
	phi = phi[sort];
	fft = np.fft.fft(radd);
	n = np.indices(np.shape(fft))[0];


	for i in range(-1,2):
		for j in range(-1,2):
			mask[rc+i][cc+j] = True;

	vis[mask] = (0,255,0);
	cv.imwrite(f"{frm}/vis.png",vis);
	np.savetxt(f"{frm}/rad",rad,fmt='%.18f');
	np.savetxt(f"{frm}/phi",phi,fmt='%.18f');
	np.savetxt(f"{frm}/fft",fft,fmt='%.18f');
	np.savetxt(f"{frm}/n",n,fmt='%d');



	# Close the fifo. This is done to ensure that a call to "os.read" in the next iteration will cause this process to enter an idle state of waiting for the calling
	# process to open the fifo for writing. Essentially, it ensures that this "infinite while loop" doesn't devour the CPU.

	os.close(i);


	# This sends the name of the directory ( frame ) to the next "python build daemon" ( another process which behaves similar to this ) if there is one.

	if len(sys.argv) == 3:
		o = os.open(sys.argv[2], os.O_WRONLY);
		os.write(o, frm.encode('ascii'));
		os.close(o);
