

def isPalindrome(s):
    return s ==s[::-1]
def euler036(N):
    sm = 0
    for i in range(N):
        if isPalindrome(str(i)):
            # print i
            # print bin(i)[2:]
            if isPalindrome(bin(i)[2:]):
                sm += i
    print sm
euler036(1000000)