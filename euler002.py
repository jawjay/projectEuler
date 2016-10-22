

# sum of even fibonacci numbers up to T
#T = int(raw_input().strip())
T = 1
ns = [10,100]
for i in range(T):

	#N = int(raw_input().strip())
	N = 4000000

	x1 = 1
	x2 = 2
	sm = 0
	while x2 < (N-1):
		x1,x2 = x2,x2+x1
		if x1%2==0:
			sm = sm+x1 

	print(sm)

