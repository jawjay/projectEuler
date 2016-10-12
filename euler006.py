T = int(raw_input().strip())
for t in range(T):
	N = int(raw_input().strip())
	print sum(range(N+1))**2 - sum(x*x for x in range(N+1) )
