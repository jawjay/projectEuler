import math

def euler034(N):
    pass
    facts = [math.factorial(x) for x in range(10)]

    for i in range(100000):
        if i == int(sum((facts[int(x)] for x in list(str(i))))):
            print i


euler034(1)