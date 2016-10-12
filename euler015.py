def countPath(x,y):
    """recursive function to count paths based on x,y point"""
    if x ==0 or y ==0:
        return 1
    return countPath(x-1,y)+countPath(x,y-1)
    pass



print(countPath(3,2))