import random
arrayOfVals = [0]
for x in range(300):
    arrayOfVals.append(random.randrange(0,20))
for x in range(250):
    arrayOfVals.append(random.randrange(20,60))
for x in range(180):
    arrayOfVals.append(random.randrange(60,100))
for x in range(70):
    arrayOfVals.append(random.randrange(100,140))
for x in range(50):
    arrayOfVals.append(random.randrange(140,180))
for x in range(30):
    arrayOfVals.append(random.randrange(180,199))
print(arrayOfVals)