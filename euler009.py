def e9(N):
	for a in range(1,N-1):
		for b in range(a+1,N-1):
			if a+b>=N:break
			c = N-a-b
			if a*a+b*b==c*c:
				print(a*b*c)

print(e9(1000))