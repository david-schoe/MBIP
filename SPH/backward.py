import sys
import numpy as np
import scipy.special as sp
from A import rrefsolve

from PIL import Image, ImageDraw
from matplotlib.figure import Figure
import forward as f

SN = 2;

N = int(f.NS);
B = int(f.PPS*SN);
F = int(f.PPS/f.NS);

py = np.zeros(N);
px = np.zeros(N);
for n in range(0,N):
	py[n] = np.real(f.py[B+n*F]);
	px[n] = np.real(f.px[B+n*F]);

theta = np.zeros(N);
phi = np.arctan(px/py)
Y = lambda n,m,theta,phi : sp.sph_harm(m,n,theta,phi);
R = np.array(py/np.cos(phi));
RR = R-f.R_0;

Y_M = np.zeros((N,N),dtype=np.double);
#Y_M = np.zeros((N,N));
for m in range(0,N):
	for n in range(0,N):
		Y_M[m][n] = np.real(Y(n,f.m,theta[m],phi[m]));

SS = rrefsolve(Y_M,RR);
#SS = np.linalg.solve(Y_M,RR)
print (SS);
