import sys
import numpy as np
from A import plot_png

R_0 = 4;
NS = 8;
PPS = 10;
P = 2*np.pi;

theta = np.linspace(0,2*np.pi,PPS*NS);

A = lambda n : 1;
Y = lambda n,theta : np.cos(2*np.pi*n*theta/P);
R_n = lambda n,theta : A(n) * Y(n,theta);


R = R_0;

for n in range(3,34):
	R = R + R_n(n,theta);


x = R*np.cos(theta);
y = R*np.sin(theta);

plot_png(x,y,"test.png");

