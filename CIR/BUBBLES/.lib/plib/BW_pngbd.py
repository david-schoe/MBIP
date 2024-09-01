import sys
import os
import numpy as np
from PIL import Image, ImageFilter
i = os.open(sys.argv[1], os.O_RDONLY);
while (1):
	buf = os.read(i,256);
	if len(buf) > 0:
		strl = buf.decode('utf-8').splitlines();
		if strl[0] == "term":
			break


		# Load grayscale image
		img = Image.open(strl[0]).convert('L')  # 'L' for grayscale

		# Convert to numpy array
		arr = np.array(img)

		# Define threshold level (e.g., 127 for 50% brightness)
		threshold = 20

		# Apply thresholding
		binary_arr = np.where(arr > threshold, 255, 0)

		# Convert back to Pillow image
		binary_img = Image.fromarray(binary_arr.astype('uint8'))

		# Save the binary image
		binary_img.save(strl[1])
