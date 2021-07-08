import  matplotlib.pyplot as plt



D1 = []
D2 = []
D3 = []


#with open('Distances1', 'r') as R1:
#    for line in R1:
#        D1.insert(0, line)
#        print(D1)
#R1 = open('Distances1', 'r')
#R2 = open('Distances2', 'r')
#R3 = open('Distances3', 'r')

#with open('Distances2', 'r') as R2:
#    for line in R2:
#        D2.insert(0, line)
#        print(D2)
#    
#
#with open('Distances3', 'r') as R3:
#    for line in R3:
#        D3.insert(0, line)
#        print(D3)
    

##update files then D[0], take only first index
## if 

def trilat(x1, y1, x2,y2, x3, y3):
    while True:
        with open('Distances1', 'r') as R1:
            for line in R1:
                D1.insert(0, line)
        #print(D1)
        with open('Distances2', 'r') as R2:
            for line in R2:
                D2.insert(0, line)
        with open('Distances3', 'r') as R3:
           for line in R3:
               D3.insert(0, line)


        d1 = float(D1[0])
        d2 = float(D2[0])
        d3 = float(D3[0])

        A = 2*x2 - 2*x1
        B = 2*y2 - 2*y1
        C = d1**2 - d2**2 - x1**2 + x2**2 - y1**2 + y2**2
        D = 2*x3 - 2*x2
        E = 2*y3 - 2*y2
        F = d2**2 - d3**2 - x2**2 + x3**2 - y2**2 + y3**2
        try:
            x = (C*E - F*B) / (E*A - B*D)
            y = (C*D - A*F) / (B*D - A*E)
        except ZeroDivisionError: 
            x = (C*E - F*B) / (E*A - B*D)+0.025
            y = (C*D - A*F) / (B*D - A*E)+0.025

        return x,y

if __name__ == '__main__':
    print('Please enter input data')
    x1=int(input('x1: '))
    x2=int(input('x2: '))
    x3=int(input('x3: '))
    y1=int(input('y1: '))
    y2=int(input('y2: '))
    y3=int(input('y3: '))
    A, B = trilat(x1, y1, x2, y2, x3, y3)
    print(A, B)
    plt.plot([x1, x2, x3], [y1, y2, y3] ,'ro')
    plt.plot(A, B, color='blue',)
    plt.axis([0, 20, 0, 20])
    plt.show()




