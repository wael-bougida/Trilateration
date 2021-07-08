import serial as sr
from time import localtime, strftime
#port = serial.Serial(COM73, 9600)
#port.write(%LQUWM.COMD 0x30 0x38)


def listen(port):
    COMNUM = 73
    #global ser
    ser = sr.Serial()
    ser.baudrate = 9600 
    ser.port = port #73 #port 
    ser.write('%LQUWM.COMD 0x30 0x38')
    #sleep(1)
    while(True):
        a = ser.readline()
        print(a)
        with open('ranges.txt', 'a', encoding='utf-8') as r:
            r.write(strftime('%d %b %Y %H%M%S: ', localtime()))
            r.write(a.decode())
    


#matrix data = np.genfromtxt('data file')
#ranges = matrix_data[:, "column number"]


if __name__ == '__main__':
    listen(input('please enter port name:'))


    