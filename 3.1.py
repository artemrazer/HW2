N = 1100
eps = float(1.)
for i in range (N):
	eps = eps / 2.
	one_plus_eps = 1. + eps
	print (i, 'eps = ', eps , 'one plus eps = ', one_plus_eps)
