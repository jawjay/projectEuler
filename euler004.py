# # Find largFind the largest palindrome made from the product of two 3-digit numbers which is less than N

# 	# Max will be 999*999
# 	# min will be 100* 100

# #T = int(raw_input().strip())

# def isPalindrome(num):
# 	return str(num)==str(num)[::-1]


# def getNextSmallestPal(num):
# 	'''
# 	unfinished
# 	'''
# 	nstr = str(num)
# 	l = len(nstr)
# 	if l%2==0: #even digits

# 		N = int ( nstr[:l/2]+nstr[:l/2][::-1])
# 		at_left,at_right = l/2-1,l/2 # the number at these indicies whould be equal
# 		while N > num:
# 			nstr = str(N)
# 			num_ at = int(nstr[at_left])
# 			if num_at != 0:
# 				num_at -= 1
# 				nstr[at_left] = str(num_at)
# 				nstr[at_right] = str(num_at)
# 				N = int(nstr)
# 			else:

		

# # need to jump down from palindromes
# def findMaxPal(n,min = 100,max = 999):
# 	maxPal = 0
# 	upper = 999
# 	while upper >99: # need upper bound greater than 3 digits
# 		lower = 999
# 		while lower >99:
# 			P = upper * lower
# 			if P > maxPal and isPalindrome(P)and P < n:
# 				maxPal = P
# 			lower -= 1
# 		upper -= 1

# 	return maxPal


# T = 2
# ns = [101110,800000] #101101,793397
# for t in range(T):
# 	#N = int(raw_input().strip())
# 	N = ns[t]

# 	# need to loop through palindrom numbers

# 	print findMaxPal(N)

def euler004(N):
	ots = []
	for a in range(999, 100, -1):
		for b in range(a, 100, -1):
			s = str(a * b)
			if s == s[::-1]:
				ots.append(a*b)
	return max(ots)

print(euler004(1))
