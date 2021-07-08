import time
import math
from update import * 
Dis1 = []
Dis2 = []
Dis3 = []


print('Hello')

for n in range(11, 5, 1):
    Dis1.append(float(n))
    #time.sleep(3)
    print('Dis1')
    print(Dis1)

for k in range(11, 5, 1):
    Dis2.append(float(k))
    #time.sleep(3)
    # print('Dis2')
    print(Dis2)

for i in range(5, 11, 1):
    Dis3.append(float(i))
    #time.sleep(3)
    #print('Dis3')
    print(Dis3)

with open('Distances1', 'w') as Dist1:

    time.sleep(3)
    Dist1.writelines(str(Dis1))
    Dist1.close()

#update()


with open('Distances2', 'w') as Dist2:
    time.sleep(3)
    Dist2.writelines(str(Dis2))
    Dist2.close()

with open('Distances3', 'w') as Dist3:
    time.sleep(3)
    Dist3.write(str(Dis3))
    Dist3.close()

