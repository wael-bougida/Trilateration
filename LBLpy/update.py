from trilat import * 

def read_file():
    with open('Distances1', 'r') as D:
        var = D.readlines()
    return var


initial = read_file()
print(initial)

def update(initial):
    while True: 
        current = read_file()
        if initial != current: 
            for line in current: 
                if line not in initial: 
                    D1.insert(0, line)
                    print(D1)
            initial = current   


if __name__ == '__main__':
    update(initial)