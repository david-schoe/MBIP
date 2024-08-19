import sys
import numpy as np
import scipy.special as sp
from A import rrefsolve

from PIL import Image, ImageDraw
from matplotlib.figure import Figure
import forward as f

N = 6;
B = 3;
py = np.zeros(N);
px = np.zeros(N);
for n in range(0,N):
	py[n] = np.real(f.py[B+n]);
	px[n] = np.real(f.px[B+n]);

theta = np.zeros(N);
phi = np.arctan(px/py)
Y = lambda n,m,theta,phi : sp.sph_harm(m,n,theta,phi);
R = np.array(py/np.cos(phi));
RR = R-f.R_0;

Y_M = np.zeros((N,N),dtype=np.longdouble);
#Y_M = np.zeros((N,N));
for m in range(0,N):
	for n in range(0,N):
		Y_M[m][n] = np.real(Y(n,f.m,theta[m],phi[m]));

SS = rrefsolve(Y_M,RR);
#SS = np.linalg.solve(Y_M,RR)
print (SS);
