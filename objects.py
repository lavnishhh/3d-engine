import math
from math_func import *
class Cube:
    def __init__(self, a, x, y, z):
        self.a = a
        self.x=x
        self.y=y
        self.z=z
        self.position=[self.x,self.y,self.z]
        self.tris=[]

        self.tris.append([[x,y,z],[x+a,y,z+a],[x+a,y,z]]) #left-lower
        self.tris.append([[x,y,z],[x,y,z+a],[x+a,y,z+a]]) #left-upper

        self.tris.append([[x,y,z],[x,y+a,z+a],[x,y+a,z]]) #forward-upper
        self.tris.append([[x,y,z],[x,y,z+a],[x,y+a,z+a]]) #forward-lower

        self.tris.append([[x,y,z],[x+a,y+a,z],[x+a,y,z]]) #down-forward
        self.tris.append([[x,y,z],[x,y+a,z],[x+a,y+a,z]]) #down-backward

        self.tris.append([[x+a,y+a,z+a],[x+a,y,z+a],[x+a,y,z]]) #back-upper
        self.tris.append([[x+a,y+a,z+a],[x+a,y,z],[x+a,y+a,z]]) #back-lower

        self.tris.append([[x+a,y+a,z+a],[x,y+a,z+a],[x,y+a,z]]) #right-upper
        self.tris.append([[x+a,y+a,z+a],[x,y+a,z],[x+a,y+a,z]]) #right-lower

        self.tris.append([[x+a,y+a,z+a],[x,y,z+a],[x+a,y,z+a]]) #top-forward
        self.tris.append([[x+a,y+a,z+a],[x,y+a,z+a],[x,y,z+a]]) #top-backward
        
class Sphere:
    def __init__(self, r, x, y, z, h_dimension,v_dimension) -> None:
        self.r=r
        self.x=x
        self.y=y
        self.z=z
        self.position=[self.x,self.y,self.z]
        self.h=h_dimension
        self.v=v_dimension
        self.tris=[]
        temp=[]
        for dh in range(0,2*self.h+1):
            t=[]
            for dv in range(0,2*self.v+1):
                x1 = x + (r*math.sin(math.pi*dv/v_dimension)*math.cos(math.pi*dh/h_dimension))
                y1 = y + (r*math.sin(math.pi*dv/v_dimension)*math.sin(math.pi*dh/h_dimension))
                z1 = z + (r*math.cos(math.pi*dv/v_dimension))
                t.append([x1,y1,z1])
            temp.append(t)
        for vring in range(0,len(temp)-1):
            for h in range(1,len(temp[vring])-1):
                vert=[]
                vert.append(temp[vring][h])
                vert.append(temp[vring+1][h])
                vert.append(temp[vring+1][h+1])
                self.tris.append(vert)

                vert=[]
                vert.append(temp[vring][h])
                vert.append(temp[vring+1][h+1])
                vert.append(temp[vring][h+1])
                self.tris.append(vert)

        self.temp=temp