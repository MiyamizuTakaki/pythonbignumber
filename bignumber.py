def bignumber(sqare,x,y):
    sqxx = []
    for sqares in sqare:
        for line in range(1,y):
            for linex in range(0,y-line):
                if sqares[linex] < sqares[linex+1]:
                    temp = sqares[linex]
                    sqares[linex] = sqares[linex+1]
                    sqares[linex] = temp
        sqxx.append(sqares[0])
    for line in range(1,x):
        if sqxx[line-1] < sqxx[line]:
            temp = sqxx[line - 1]
            sqxx[line - 1] = sqxx[line]
            sqxx[line] = temp
    p = sqxx[0]
    return p