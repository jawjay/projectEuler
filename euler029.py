def euler029(N):
    return len(set((a**b for a in range(2,N+1) for b in range(2,N+1))))


print(euler029(100))
