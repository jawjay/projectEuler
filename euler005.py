#Smallest Multiple
	#What is the smallest positive number that is evenly divisible(divisible with no remainder) 
	#by all of the numbers from 1 to N
#T = int(raw_input().strip())

ns = [3,10]
T = int(raw_input().strip())
for i in range(T):# one for each number
    
   N = int(raw_input().strip())
    # N = ns[i] 
    nums = range(1,N+1)[::-1]
    searching = True
    n = N
    while searching:
        if sum( (n%x for x in nums))== 0:
        	searching = False
        else:
        	n+= N
    print n