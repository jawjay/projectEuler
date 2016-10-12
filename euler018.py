def euler018(N):
    pass
    # dynamic programming 
    #  recursively check each level
    # each number has its index and the next 
    def maxTri(tri,i,a):
        if i == len(tri):
            return 0
        return tri[i][a] + max(maxTri(tri,i+1,a),maxTri(tri,i+1,a+1))
    return maxTri(N,0,0)


t = [[3],[7,4],[2,4,6],[8,5,9,3]]

a = euler018(t)
print(a)

