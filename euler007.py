# def isprime(n):
#     """Returns True if n is prime."""
#     if n == 2:
#         return True
#     if n == 3:
#         return True
#     if n % 2 == 0:
#         return False
#     if n % 3 == 0:
#         return False
#     i = 5
#     w = 2

#     while i * i <= n:
#         if n % i == 0:
#             return False

#         i += w
#         w = 6 - w

#     return True

# T = int(raw_input().strip())
# # T = 2
# for t in range(T):
#     N = int(raw_input().strip())
#     # N = 6
#     sumP = 1
#     num = 1
#     while sumP< N:
#         if isprime(num):
#             sumP+=1
#         num+=2
#     print num

# prime_list = lambda x:[i for i in xrange(2, x+1) if all([i%x for x in xrange(2, int(i**0.5+1))])  ][10000]

# print prime_list(120000)

