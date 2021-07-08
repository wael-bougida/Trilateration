import time 

Ranges1, Ranges2, Ranges3 = [], [], []

for i in reversed(range(5, 12, 1)):
    Ranges1.append(i)
    print(Ranges1)

for i in reversed(range(5, 12, 1)):
    Ranges2.append(i)
    print(Ranges2)

for i in range(5, 12, 1):
    Ranges3.append(i)
    print(Ranges3)


with open('Distances1', 'w') as D1: 
    for data in Ranges1: 
        D1.write('%s \n' %data)
        time.sleep(10)



with open('Distances2', 'w') as D2: 
    for data in Ranges2: 
        D2.write('%s \n' %data)
        time.sleep(10)



with open('Distances3', 'w') as D3: 
    for data in Ranges3: 
        D3.write('%s \n' %data)
        time.sleep(10)
















