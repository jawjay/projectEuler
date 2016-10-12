from itertools import permutations
import math


class lexPerm:
    def __init__(self,goal,lets = 'abcdefghijklm' ):
        self.lets = lets
        
        self.ind = 0
        self.N = len(self.lets)
        self.at = 1
        self.goal = goal
        self.changes = [0]*self.N
    
    def getNums(self):
        ind = 0
        fact_at = self.N
        mf = math.factorial(self.N)
        changes = [0]*self.N
        while self.at != self.goal:
            if mf+self.at>self.goal:
                ind+=1
                fact_at-=1
                mf = math.factorial(fact_at)
                continue
            changes[ind]+=1
            self.at += mf
        return changes
    def getPerm(self):
        c = self.getNums()
        per = list(self.lets)
        out = ''
        for index,changes in enumerate(c[1:]):
            # print(per)
            # print(index,changes)
            out += per[changes]
            per = per[:changes]+per[changes+1:]
            # per[index],per[index+changes] = per[index+changes],per[index]
        return (out+per[0])
def euler024(N):

    l = 'abcdefghijklm'

    x = lexPerm(N)
    # print(x.getPerm())
    return x.getPerm()
    # l = 'abcdefghijklm'
    # l = ['1','2','3','4','5']

# l = 'abcdef'
# print(euler024(1000000))

# euler024(2)
# euler024(3)
# euler024(4)
# euler024(5)
# euler024(6)
# euler024(7)
# perms = [''.join(p) for p in permutations(l)]
# print(perms)
# first_dict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
# for p,i in enumerate(sorted(perms)[:]):
#     # print l
#     print p+1,i,euler024(p+1)
    # print '\n'
# print(first_dict)

