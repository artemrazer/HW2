N = 1100
eps = complex(1. + 1j)
for i in range (N):
	eps = eps / 2.
	one_plus_eps = 1. + eps
	print (i, 'EPS = ', eps , 'ONE PLUS EPS = ', one_plus_eps)
