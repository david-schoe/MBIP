import sys
import numpy as np
import scipy.special as sp

from PIL import Image, ImageDraw
from matplotlib.figure import Figure

R_0 = 1;
m = 0;
NS = 8;
PPS = 100
theta = np.zeros(PPS*NS);
phi = np.linspace(0,np.pi,PPS*NS);

A = lambda n : 1;
Y = lambda n,m,theta,phi : sp.sph_harm(m,n,theta,phi);
R_n = lambda n,theta,phi : A(n) * Y(n,m,theta,phi);


R = R_0;

for n in range(3,4):
	R = R + R_n(n,theta,phi);

px = R*np.sin(phi);
py = R*np.cos(phi);
nx = np.flip(-px);
ny = np.flip(py);
x = np.real(np.concatenate((px,nx)));
y = np.real(np.concatenate((py,ny)));

fig = Figure();
ax = fig.add_subplot();
#ax.set_axis_off();
ax.set_aspect('equal');
ax.plot(x,y);
fig.savefig("test.png");
