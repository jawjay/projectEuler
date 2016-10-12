import random
def euler027(N):
    pass


def FermatPrimalityTest(number):
    ''' if number != 1 '''
    if (number > 1):
        ''' repeat the test few times '''
        for time in range(3):
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            
            ''' Test if a^(n-1) = 1 mod n '''
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        
        return True
    else:
        ''' case number == 1 '''
        return False 
mx = 0

lb = -1000
ub = 1000
ot = [(0,0,0)]
for a in range(lb,ub):
    if a%2==0:
        continue
    for b in range(lb,ub):
        if not FermatPrimalityTest(b):
            continue
        i = 0
        while FermatPrimalityTest(i**2+a*i+b):
            i+=1
        ot = max(ot,(i,a,b))
print((ot))