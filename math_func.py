
import math

def sub(X,Y):
    return [b-a for a,b in zip(X,Y)]

def cross(X,Y):
    return [X[1]*Y[2]-X[2]*Y[1] , X[0]*Y[2]-X[2]*Y[0] , X[0]*Y[1]-Y[0]*X[1]]

def dot(X,Y):
    return sum([a*b for a,b in zip(X,Y)])

def centroid(vertices):
    return [sum([a,b,c])/len(vertices[0]) for a,b,c in zip(vertices[0],vertices[1],vertices[2])]

def angle3D(X,Y):
    return math.acos(sum([a*b for a,b in zip(X,Y)])/(Vector3Mod(X)*Vector3Mod(Y)))

def distance(X,Y):
    return (sum([(a-b)**2 for a,b in zip(X,Y)]))**0.5

def Vector3Mod(vector):
    return (sum([component**2 for component in vector]))**0.5

def distanceIntersectionPoint(origin,vector,d):
    k = (d/(sum([component**2 for component in vector]))**0.5)
    return [p+(k*d) for p,d in zip(origin,vector)]

def zAxis(object,cam):
    return ((sum([a**2 for a in object[:2]])**0.5)/(sum([(a-b)**2 for a,b in zip(object,cam)])**0.5))

def normal(tris):
    return cross(sub(tris[0],tris[1]),sub(tris[0],tris[2]))

def shade(sun,vertices):
    return (angle3D(sun,normal(vertices))/(3.14*0.9)+0.1)
