import sys
import numpy as np
from A import rrefsolve,DCT,plot_png
from scipy.fft import fft
from PIL import Image, ImageDraw
from matplotlib.figure import Figure
import forward as f

SN = 0;

#N = int(f.NS);
#B = int(f.PPS*SN);
#F = int(f.PPS/f.NS);

N = f.PPS*f.NS;
B = 0;
F = 1;


y = np.zeros(N);
x = np.zeros(N);
for n in range(0,N):
	y[n] = f.y[B+n*F];
	x[n] = f.x[B+n*F];

theta = np.arctan2(y,x);
Y = lambda n,theta : np.cos(2*np.pi*n*theta/f.P);
R = np.power(x*x+y*y,0.5);
RR = R-f.R_0;

Y_M = np.zeros((N,N),dtype=np.double);
Y_M = np.zeros((N,N));
for m in range(0,N):
	for n in range(0,N):
		Y_M[m][n] = Y(n,theta[m]);

#SS = rrefsolve(Y_M,RR);
#SS = np.linalg.solve(Y_M,RR)
#print (SS);


SS = DCT(Y_M,RR,theta);
RRR = np.matmul(Y_M,SS.T) + f.R_0;
print (SS);
print (RRR);

x = RRR*np.cos(theta);
y = RRR*np.sin(theta);

plot_png(x,y,"test2.png");


SSS = 1/N * fft(RR);
print (SSS);
x
RRRR = np.matmul(Y_M,SSS.T) + f.R_0
print (RRRR);
print (f.R);

x = RRRR*np.cos(theta);
y = RRRR*np.sin(theta);

plot_png(x,y,"test3.png");

