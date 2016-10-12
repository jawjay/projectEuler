from collections import deque
def multSum(K):
    """ Returns product of all numbers in list"""
    N = 1
    for i in K:
        N*=i
    return N
def getDiag(grid):
    mx = 0
    for i in range(0,17):
        l1 = range(20)[i:]
        l2 = range(20)[:20-i]
        l3 = range(20)[::-1][i:]
        l4 = range(20)[::-1][:i]
        # print "l1,l2: ",zip(l1,l2)
        # print "l2,l1: ",zip(l2,l1)
        # print "l1[::-1],l2: ",zip(l3,l4)
        # print "l1,l2[::-1]: ",zip(l4,l3)
        # print "\n\n"
        mx = max(mx,getMax([grid[x][y] for (x,y) in zip(l1,l2)]))
        mx = max(mx,getMax([grid[x][y] for (x,y) in zip(l2,l1)]))
        mx = max(mx,getMax([grid[x][y] for (x,y) in zip(l3,l4)]))
        mx = max(mx,getMax([grid[x][y] for (x,y) in zip(l4,l3)]))

    return mx
def getMax(lst,sz = 4):
    mx = 0
    at = deque([0]+lst[:sz-1])
    for i in lst[sz-1:]:
        # print "i:%d"%i
        at.popleft()
        at.append(i)
        mx = max(mx,multSum(at))
        #print "Sum: %d"%multSum(at)
    return mx

def euler011(grid):
    """    Use a stack for on/off and keep track of max rows then cols then diag    """
    mx = 0
    for row in range(20):
        # search each row
        # print getMax(grid[:][row])
        # print getMax(grid[row][:])
        mx = max(mx,getMax(grid[:][row]))
        mx = max(mx,getMax(grid[row][:]))
        #need down diagonal

    dmax = getDiag(grid)
    mx = max(mx,dmax)

    return mx
# print getMax([1,1,8,9,3,-1,-1,9,182,1,12,134,2],4)
a = [[y for y in range(20*x,20*(x+1))] for x in range(20)]
b = euler011(a)

print(b)

def test():
    for i in range(10):
        l3 = range(10)[::-1][i:]
        l4 = range(10)[::-1][:i]



test()






