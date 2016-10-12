def euler030(N):

    digits = list('0123456789')
    fifths = [i**5 for i in range(10)]
    ot = 0
    for i in range(2,999999):
        if str(i)==str(sum((int(x)**5 for x in list(str(i))))):
            # print(i)
            ot+= i
    print(ot)
    return 0
    pass

euler030(4)

for i in range(10):
    print(i,i**4)
