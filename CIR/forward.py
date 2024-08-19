import sys
import numpy as np

from PIL import Image, ImageDraw
from matplotlib.figure import Figure

R_0 = 1;
NS = 8;
PPS = 50
P = 2*np.pi;

theta = np.linspace(0,2*np.pi,PPS*NS);

A = lambda n : 1/n;
Y = lambda n,theta : np.cos(2*np.pi*n*theta/P);
R_n = lambda n,theta : A(n) * Y(n,theta);


R = R_0;

for n in range(5,6):
	R = R + R_n(n,theta);

x = R*np.cos(theta);
y = R*np.sin(theta);

fig = Figure();
ax = fig.add_subplot();
ax.set_axis_off();
ax.set_aspect('equal');
ax.plot(x,y);
fig.savefig("test.png");
