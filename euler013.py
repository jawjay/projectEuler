

dig = ['37107287533902102798797998220837590246510135740250',
'46376937677490009712648124896970078050417018260538',
'74324986199524741059474233309513058123726617309629',
'91942213363574161572522430563301811072406154908250',
'23067588207539346171171980310421047513778063246676']



def euler013(dig):
    pass

    # together = list(zip(dig[0],dig[1],dig[2],dig[3],dig[4]))
 

    together = (list(zip(*dig)))
    


    output = [0]*55 # use this to hold output
    start_index = 5
    index = 54

    # for i in together[::-1]:
    #     print(i)

    for i in (together)[::-1]:
        num = int(sum(map(lambda x:int(x),i))+output[index])
        output[index] = int(num % 10)# number to include at this level
        output[index-1] +=int(num % 100/10) # number to include at level one over
        output[index-2] += int(num%1000/100) # number to include two places over
        index -= 1


    start = [y for y,x in enumerate(output) if x >0][0]

    # print(start)
    print(''.join(map(lambda x: str(x),output[start:start+10])))
# print(output)


def euler013_2(dig):
    together = [ int(di[:14]) for di in dig]
    print(str(sum(together))[:10])
euler013_2(dig)
