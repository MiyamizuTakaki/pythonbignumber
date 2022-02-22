from bignumber import *
from xulie import *
from sqare import sqare
##set ranks
x =10
y =10
##set ranks and maxvaule
for vet in range(0,2):
    sz = sqare(x,y,70)
    spare_1010 = sz.create()
    bigchoose = bignumber(spare_1010,x,y)
    print("This is "+str(vet+1))
    print("This is a big number "+str(bigchoose))
    xulie(spare_1010,x,y)
    print("\n\n\n\n")
