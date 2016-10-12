# largest prime factor of given number N

#T = int(raw_input().strip())
T = 2
ns = [18,25]
for t in range(T):
	#N = int(raw_input().strip())
	N = ns[t]

	i = 2
	while i * i <= N:
		while N%i==0 and N!=i:
			N /= i 
		i += 1
	print N 