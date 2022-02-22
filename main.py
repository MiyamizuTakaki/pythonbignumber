import random
from bignumber import *
from xulie import *
spare_1010 = []
x = []
z = 4
q = 4
for number1 in range(0,z):
    for number in range(0,z):
        x.append(random.randint(0,20))
    spare_1010.append(x)
    x = []
x = bignumber(spare_1010,z,q)
print("This is a big number "+str(x))
xulie(spare_1010,z,q)
