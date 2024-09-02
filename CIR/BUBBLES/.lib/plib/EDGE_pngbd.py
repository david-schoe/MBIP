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
		im = Image.open(strl[0]).convert("L")
		ime = im.filter(ImageFilter.FIND_EDGES)
		ime.save(strl[1]);
