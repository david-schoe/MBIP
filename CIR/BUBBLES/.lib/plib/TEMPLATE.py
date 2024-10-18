import sys
import os
import cv2 as cv
import numpy as np


while (1):

						# Open the fifo that is passed as an argument variable on the command line
	i = os.open(sys.argv[1], os.O_RDONLY);


						# Attempt to read from the fifo (will be unable to read until the fifo has been
						# opened for writing by another process (typically the calling process) )
	buf = os.read(i,256);


						# Convert the binary "buf" into a string
	strl = buf.decode('utf-8').splitlines();
						# The string is the directory of interest (a frame)... so begin image processing from here on



						# Open the <some_image_here> image in the frame
	<some_image_here> = cv.imread(f"{strl[0]}/<some_image_here>.png",cv.IMREAD_GRAYSCALE);



	## INSERT CODE HERE ##







						# Close the fifo. This is done to ensure that a call to "os.read" in the next iteration will cause this process
						# to enter an idle state of waiting for the calling process to open the fifo for writing. Essentially, it ensures that this
						# "infinite while loop" doesn't devour the CPU.
	os.close(i);


						# This sends the name of the directory (frame) to the next "python build daemon" (another process which behaves
						# similar to this) if there is one.
	if len(sys.argv) == 3:
		o = os.open(sys.argv[2], os.O_WRONLY);
		os.write(o, strl[0].encode('ascii'));
		os.close(o);
