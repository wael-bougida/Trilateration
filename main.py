import serial as sr
from time import localtime, strftime


# port = serial.Serial(COM73, 9600)
# port.write(%LQUWM.COMD 0x30 0x38)


def listen(port):
    COMNUM = 73
    # global ser
    ser = sr.Serial()
    ser.baudrate = 9600
    ser.port = port  # 73 #port
    ser.write('~%LQUWM.COMD 0x31 0x37 4 4')
    # sleep(1)
    while True:
        a = ser.readline()
        print(a)
        with open('ranges.txt', 'a', encoding='ASCII') as r:
            r.write(strftime('%d %b %Y %H%M%S: ', localtime()))
            r.write(a.decode())


# matrix data = np.genfromtxt('data file')
# ranges = matrix_data[:, "column number"]

def wake(port):
    COMNUM = 73
    # global ser
    ser = sr.Serial()
    ser.baudrate = 9600
    ser.port = port  # 73 #port
    ser.write('~%LQUWM.COMD 0x30 0x38')


def rs232(port):
    COMNUM = 73
    # global ser
    ser = sr.Serial()
    ser.baudrate = 9600
    ser.port = port  # 73 #port
    ser.write('~%LQUWM.COMD56')
    while True:
        a = ser.readline()
        print(a)
        with open('test.txt', 'w', encoding='ASCII') as r:
            r.write(a.decode())



if __name__ == '__main__':
    wake(input('please enter port name:'))
    listen(input('please enter port name:'))
    rs232(input('please enter port name: '))



