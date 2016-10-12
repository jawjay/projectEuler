
def recurring_cycle(n, d):
    #This is from fermats last thereom?
    for t in range(1, d):
        if 1 == 10**t % d:
            return t
    return 0


def euler026(N):
    rc = [recurring_cycle(1,i) for i in range(1,N+1)]
    m =  max(rc)
    return    [i for i,j in enumerate(rc) if j == m][0]+1

print(euler026(1000))
