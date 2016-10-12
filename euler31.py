coins = [1,2,5,10,20,50,100,200]
def euler31(amt,coins):
    ot = 0
    if amt in coins:
        return 1
    for i in coins:
        if amt-i>0:
            ot+= euler31(amt-i,coins)
        if amt-i==0:
            ot+=1
    return ot



