import math
def geo2cart(lat, lon, lat0, lon0):
    x = (lon - lon0)    #* mdeglon(lon0)
    y = (lat - lat0)    #* mdeglat(lat0)
    return x, y


def mdeglon(lat0):
    lat0rad = math.radians(lat0)
    L = 111415.13 * math.cos(lat0rad) - 94.55 * math.cos(3.0*lat0rad) - 0.12* math.cos(5.0*lat0rad)
    return L

def mdeglat(lat0):
    lat0rad = math.radians(lat0)
    L = 111132.09 - 566.05* math.cos(2.0*lat0rad) + 1.20 * math.cos(4.0*lat0rad) - 0.002* math.cos(6.0*lat0rad)
    return L

if __name__ == '__main__':
    lat0 = float(input('reference latitude: '))
    long0 = float(input('reference longitude'))
    
    print(mdeglat(lat0), mdeglon(lat0))

    x = float(input(' latitude: '))
    y = float(input(' longitude'))

    print(geo2cart(x, y , lat0, long0))