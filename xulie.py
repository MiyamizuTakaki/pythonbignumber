def xulie(sqare,x,y):
    for sqares in sqare:
        for line in range(1, y):
            for linex in range(0, y - line):
                if sqares[linex] > sqares[linex + 1]:
                    temp = sqares[linex]
                    sqares[linex] = sqares[linex + 1]
                    sqares[linex] = temp
        print(sqares)