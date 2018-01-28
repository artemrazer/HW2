N = 350
under = float(1e0)
over = float(1e0)
for i in range (N):
	under = under / 10.
	over = over * 10.
	print (i, 'UNDER = ', under,'OVER = ', over)
