import numpy as np
import os


class study:

	def __init__(self,bt,ft,pl):		# takes arguments of bubble tupple (bt), frame tupple (ft), and property list (pl)
						# eg.	bt = (-1,)		-->	all bubbles available
						# eg.	bt = (0,)		-->	just bub_0000
						# eg.	bt = (4,6,9,3)		-->	bub_0004, bub_0006, bub_0009, and bub_0003

						# eg.	ft = (-1,)		-->	all frames available
						# eg.	ft = (0,)		-->	just bub_0000
						# eg.	ft = (4,6,9,3)		-->	bub_0004, bub_0006, bub_0009, and bub_0003

						# eg.	pl = [("fft",-1,)]		-->	all values for fft
						# eg.	pl = [("fft",-1,),("m",4,)]	-->	all values for fft and the fourth value for m
						# eg.	pl = [("fft",1,6)]		-->	values 1-5 for fft


		self.cwd = os.getcwd();
		self.bfps = np.loadtxt(f"{self.cwd}/.bfp",dtype=str);


		self.bt = bt;
		self.ft = ft;
		self.pl = pl;
		self.b = [];

		if bt[0] == -1:
			for bfp in self.bfps:
				self.ffps = np.loadtxt(f"{bfp}/.ffp",dtype=str);
				self.b.append(bub(self,ffps,ft,pl));
		else:
			for i in bt:
				ffps = np.loadtxt(f"{self.bfps[i]}/.ffp",dtype=str);
				self.b.append(bub(self,ffps,ft,pl));

		self.b = np.array(self.b,dtype=object);

	def plot(self,x,y):

		import matplotlib.pyplot as plt
		fig,ax = plt.subplots();
		ax.plot(x,y);
		plt.show();


	def plot_png(self,x,y,name):
		from matplotlib.figure import Figure
		fig = Figure();
		ax = fig.add_subplot();
		ax.set_axis_off();
		ax.set_aspect('equal');
		ax.plot(x,y);
		fig.savefig(name);




class bub:
	def __init__(self,s,ffps,ft,pl):
		self.f = [];
		if ft[0] == -1:
			for ffp in ffps:
				self.f.append(frm(ffp,pl));
		else:
			for i in ft:
				self.f.append(frm(ffps[i],pl));
		self.f = np.array(self.f,dtype=object);
class frm:
	def __init__(self,ffp,pl):
		self.p = dict.fromkeys([pt[0] for pt in pl]);
		for pt in pl:
			if pt[0] == "fft":
				dt = np.complex_;
			else:
				dt = np.float64;
			if pt[1] == -1:
				self.p[pt[0]] = np.loadtxt(f"{ffp}/{pt[0]}",dtype=dt);
			elif len(pt) == 2:
				self.p[pt[0]] = np.loadtxt(f"{ffp}/{pt[0]}",skiprows=pt[1],max_rows=1,dtype=dt);
			else:
				self.p[pt[0]] = [];
				for i in range(1,len(pt)):
					self.p[pt[0]].append(np.loadtxt(f"{ffp}/{pt[0]}",skip_rows=pt[i],max_rows=1,dtype=dt));
			self.p[pt[0]] = np.array(self.p[pt[0]]);
