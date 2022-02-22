def bignumber(sqare,x,y):
    sqxx = []
    for sqares in sqare:
        for line in range(1,x):
            for linex in range(0,x-line):
                if sqares[linex] > sqares[linex+1]:
                    temp = sqares[linex]
                    sqares[linex] = sqares[linex+1]
                    sqares[linex+1] = temp
        sqxx.append(sqares[y-1])
    for line in range(1,y):
        if sqxx[line-1] < sqxx[line]:
            temp = sqxx[line - 1]
            sqxx[line - 1] = sqxx[line]
            sqxx[line] = temp
    p = sqxx[0]
    return p