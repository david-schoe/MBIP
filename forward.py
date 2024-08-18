import sys
import numpy as np
import scipy.special as sp

from PIL import Image, ImageDraw
from matplotlib.figure import Figure

R_0 = 0;
m = 0;
theta = np.zeros(100);
phi = np.linspace(0,np.pi,100);

A = lambda n : 1/n/n;
Y = lambda n,m,theta,phi : sp.sph_harm(m,n,theta,phi);
R_n = lambda n,theta,phi : A(n) * Y(n,m,theta,phi);


R = R_0;

for n in range(2,3):
	R = R + R_n(n,theta,phi);

px = R*np.sin(phi);
py = R*np.cos(phi);
nx = np.flip(-px);
ny = np.flip(py);
x = np.concatenate((px,nx));
y = np.concatenate((py,ny));

fig = Figure();
ax = fig.add_subplot();
ax.set_axis_off();
ax.set_aspect('equal');
ax.plot(x,y);
fig.savefig("test.png");


