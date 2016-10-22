def euler005(N):
    print(sum(range(N+1))**2-sum((x*x for x in range(N+1))))
