import numpy as np

def jacobi(A,b,n):

	xg = np.ones(len(b));
	xs = np.zeros(len(b));

	N = n;
	n = 0;

	while n < N:

		for i in range(0,len(b)):

			xs[i] = b[i];

			for j in range(0,len(b)):

				if i == j:
					continue;

				xs[i] = (xs[i] - xg[j]*A[i][j])/A[i][i];

		n+=1;
		xg = xs;

	return xs



def rrefsolve(A,b):

	if A.shape[0] != A.shape[1] or A.shape[0] != b.shape[0]:
		print ("Error: A must be an (n,n) numpy array and b a (n,) numpy array")
		return
	b = np.array([b]);
	N = A.shape[0];
	n = 0;
	A = np.concatenate((A,b.T),axis=1);

	while n<N:
		den = A[n][n];
		if den == 0:
			n+=1;
			continue;
		for i in range(0,N):
			if i==n:
				continue;
			num = A[i][n];
			for j in range(0,N+1):
				A[i][j] = A[n][j]*num/den - A[i][j];
		n+=1
	S = np.zeros(N,dtype=np.double)
	for n in range (0,N):
		S[n] = A[n][N]/A[n][n];
	return S;
