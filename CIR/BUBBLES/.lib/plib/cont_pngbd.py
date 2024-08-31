import sys
import os
from PIL import Image, ImageFilter
i = os.open(sys.argv[1], os.O_RDONLY);
while (1):
	buf = os.read(i,256);
	if len(buf) > 0:
		strl = buf.decode('utf-8').splitlines();
		if strl[0] == "term":
			break
		with Image.open(strl[0]) as im:
			imc = im.filter(ImageFilter.CONTOUR)
			imc.save(strl[1]);
