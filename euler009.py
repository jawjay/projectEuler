def e9(N):
	mx = -1
	# for m in range(N/4):
	# 	for n in range(N/4):
	# 		a = m**2-n**2
	# 		b = 2*m*n
	# 		c = m**2+n**2
	# 		if (a**2+b**2)==c**2 and a!=0 and b!=0:
	# 			print("(%d,%d,%d)"%(a,b,c))
	# 			if a+b+c == N:
	# 				mx = a+b+c


	# for a in range(N):
	# 	for b in range(N-a):
	# 		c = N-a-b
	# 		if a**2+b**2 ==c**2:
	# 			print(a,b,c)
	# 			if a+b+c==N:
	# 				mx = a*b*c

	for n in range(1,N/2+1):
		for m in range(n+1,N/2+1):
			if m*(m+n) == N/2:
				mx = (m**2-n**2)*2*m*n*(m**2+n**2)
	return mx

print e9(12)