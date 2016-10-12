nms = ['ALEX','LUIS','JAMES','BRIAN','PAMELA']


def euler022(names,pr):

    class nameDic:
        def __init__(self,names):
            self.b = {lx:list(map(lambda x: ord(x)-64,lx)) for lx in sorted(names)}
            for i,x in enumerate(sorted(self.b)):
                self.b[x] = sum(self.b[x])*(i+1)
        def getSum(self,name):
            return self.b[name]
    nd = nameDic(names)

    # print(sum((nd.getSum(x) for x in names)))
    for p in pr:
        print(nd.getSum(p))

euler022(nms,['PAMELA'])

#ord - 64

