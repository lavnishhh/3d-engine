import math
import pandas as pd
from math_func import *
class Cube:
    def __init__(self, a, x, y, z):
        self.a = a
        self.x=x
        self.y=y
        self.z=z
        self.position=[self.x,self.y,self.z]
        self.tris=[]

        self.tris.append([[x,y,z],[x+a,y,z+a],[x+a,y,z]]) #ld
        self.tris.append([[x,y,z],[x,y,z+a],[x+a,y,z+a]]) #lu

        self.tris.append([[x,y,z],[x,y+a,z+a],[x,y+a,z]]) #fd
        self.tris.append([[x,y,z],[x,y,z+a],[x,y+a,z+a]]) #fu

        self.tris.append([[x,y,z],[x+a,y+a,z],[x+a,y,z]]) #df
        self.tris.append([[x,y,z],[x,y+a,z],[x+a,y+a,z]]) #db

        self.tris.append([[x+a,y+a,z+a],[x+a,y,z+a],[x+a,y,z]]) #bu
        self.tris.append([[x+a,y+a,z+a],[x+a,y,z],[x+a,y+a,z]]) #bd

        self.tris.append([[x+a,y+a,z+a],[x,y+a,z+a],[x,y+a,z]]) #ru
        self.tris.append([[x+a,y+a,z+a],[x,y+a,z],[x+a,y+a,z]])

        self.tris.append([[x+a,y+a,z+a],[x,y,z+a],[x+a,y,z+a]]) #top
        self.tris.append([[x+a,y+a,z+a],[x,y+a,z+a],[x,y,z+a]])
        
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
#world=Sphere(10,0,0,0,10,10)

#print(world.tris)
