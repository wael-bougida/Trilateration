import numpy as np
 
def trilaterate3D(distances):
    p1=np.array(distances[0][:3])
    p2=np.array(distances[1][:3])
    p3=np.array(distances[2][:3])       
    p4=np.array(distances[3][:3])

    print(p1, p2, p3, p4)

    r1=distances[0][-1]
    r2=distances[1][-1]
    r3=distances[2][-1]
    r4=distances[3][-1]

    print(r1, r2, r3, r4)

    e_x=(p2-p1)/np.linalg.norm(p2-p1)

    print(e_x)

    i=np.dot(e_x,(p3-p1))

    e_y=(p3-p1-(i*e_x))/(np.linalg.norm(p3-p1-(i*e_x)))
    e_z=np.cross(e_x,e_y)

    d=np.linalg.norm(p2-p1)
    j=np.dot(e_y,(p3-p1))

    x=((r1**2)-(r2**2)+(d**2))/(2*d)
    y=(((r1**2)-(r3**2)+(i**2)+(j**2))/(2*j))-((i/j)*(x))

    z1=np.sqrt(r1**2-x**2-y**2)
    z2=np.sqrt(r1**2-x**2-y**2)*(-1)

    ans1=p1+(x*e_x)+(y*e_y)+(z1*e_z)
    ans2=p1+(x*e_x)+(y*e_y)+(z2*e_z)

    dist1=np.linalg.norm(p4-ans1)
    dist2=np.linalg.norm(p4-ans2)


    if np.abs(r4-dist1)<np.abs(r4-dist2):
        return ans1
    else: 
        return ans2


print(trilaterate3D(distances=np.array([10 ,10, 15])))