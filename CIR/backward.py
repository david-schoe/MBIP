import sys
import numpy as np
from A import rrefsolve

from PIL import Image, ImageDraw
from matplotlib.figure import Figure
import forward as f

SN = 0;

N = int(f.NS);
B = int(f.PPS*SN);
F = int(f.PPS/f.NS);

y = np.zeros(N);
x = np.zeros(N);
for n in range(0,N):
	y[n] = f.y[B+n*F];
	x[n] = f.x[B+n*F];

theta = np.arctan(y/x);
Y = lambda n,theta : np.cos(2*np.pi*n*theta/f.P);
R = np.power(x*x+y*y,0.5);
RR = R-f.R_0;

Y_M = np.zeros((N,N),dtype=np.double);
#Y_M = np.zeros((N,N));
for m in range(0,N):
	for n in range(0,N):
		Y_M[m][n] = Y(n,theta[m]);

SS = rrefsolve(Y_M,RR);
#SS = np.linalg.solve(Y_M,RR)
print (SS);
