
#Find the sum of all the multiples of 3 or 5 below N.

# use arithmetic sum formula 
# https://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html

# T = int(raw_input().strip()) # number of N's
# for i in range(T):
# 	# for each N we need sum3 + sum5 -sum15

# 	N = int(raw_input().strip())

# 	n3 = N/3
# 	a3 = 0
# 	d3 = 3
# 	sum3 = (n3)*(6+(n3-1)*3)>>1
# 	# print ( "sum 3: ",sum3)

# 	n5 = N/5
# 	a5 = 0
# 	d5 = 5
# 	sum5 = (n5)*(10+(n5-1)*5)>>1
	
# 	# print("n5: ",n5,"a5: ",a5,"d5: ",d5)
# 	# print ( "sum 5: ",sum5)

# 	n15 = N/15
# 	a15 = 0
# 	d15 = 15
# 	sum15 = (n15)*(30+(n15-1)*15)>>1	

# 	# print ( "sum 15: ",sum15)

# 	print sum3+sum5-sum15

print(sum(set(x for x in range(2,1000) if x%3==0 or x%5==0)))