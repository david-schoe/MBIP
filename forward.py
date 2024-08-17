qimport numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

R_0 = 0;
m = 0;
theta = np.zeros(100);
phi = np.linspace(np.pi,0,100);

A = lambda n : 1/n/n;
Y = lambda n,m,theta,phi : sp.sph_harm(m,n,theta,phi);
R_n = lambda n,theta,phi : A(n) * Y(n,m,theta,phi);


R = R_0;

for n in range(2,3):
	R = R + R_n(n,theta,phi);
print (R);
x = R*np.sin(phi);
y = R*np.cos(phi);
nx = -x;

plt.plot(x,y,nx,y);
plt.axis('equal');
plt.show();


