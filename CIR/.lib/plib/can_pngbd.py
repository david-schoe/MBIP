import sys
import os
import cv2 as cv
import numpy as np
import time
min_area = 200;

while (1):

							# Open the fifo that is passed as an argument variable on the command line

	i = os.open(sys.argv[1], os.O_RDONLY);


							# Attempt to read from the fifo (will be unable to read until the fifo has been
							# opened for writing by another process (typically the calling process) )
	buf = os.read(i,256);


							# Convert the binary "buf" into a string

	frm = buf.decode('utf-8').split('\n')[0];

							# The string is the directory of interest (a frame)... so begin image processing from here on



							# Open the image in the frame, invert the image (make black pixels white and vice-versa) using a thresholding value.

	img = cv.imread(f"{frm}/img.png",cv.IMREAD_GRAYSCALE);
	_,thr = cv.threshold(img,80,255,cv.THRESH_BINARY_INV);


							# Find each individual contour in the image, ensure its area is greater than min_area, then place the contour inside of fill

	fil = np.zeros((img.shape),np.uint8);
	contours,_ = cv.findContours(thr,cv.RETR_LIST,cv.CHAIN_APPROX_NONE);

	for cont in contours:
		if cv.contourArea(cont) > min_area:
			cv.drawContours(fil,[cont],0,255,-1);


							# Perform Canny edge detection on fill

	can = cv.Canny(fil,0,1);


							# Store the images that were created

	cv.imwrite(f"{frm}/thr.png",thr);
	cv.imwrite(f"{frm}/fil.png",fil);
	cv.imwrite(f"{frm}/can.png",can);


							# Close the fifo. This is done to ensure that a call to "os.read" in the next iteration will cause this process
							# to enter an idle state of waiting for the calling process to open the fifo for writing. Essentially, it ensures that this
							# "infinite while loop" doesn't devour the CPU.

	os.close(i);


							# This sends the name of the directory (frame) to the next "python build daemon" (another process which behaves
							# similar to this) if there is one.

	if len(sys.argv) == 3:
		o = os.open(sys.argv[2], os.O_WRONLY);
		os.write(o, frm.encode('ascii'));
		os.close(o);
