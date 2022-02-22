import random
class sqare():
    def __init__(self,x,y,maxvl=20):
        self.x =x
        self.y =y
        self.maxvl = maxvl
    def create(self):
        spare_1010 = []
        z = []
        for number1 in range(0, self.y):
            for number in range(0, self.x):
                z.append(random.randint(0, self.maxvl))
            spare_1010.append(z)
            z = []
        return spare_1010