import cv2
import numpy as np
import keyboard
#self written modules
from math_func import *
from objects import *

cam_pos=[-100,0,10]
cam_rot=0
frame_length=512
frame_size=[1024,1024]
camera_distance=1024
vfov=frame_size[1]/camera_distance
hfov=frame_size[0]/camera_distance
sun=[0,0,10]
world=[Cube(10,0,0,0),Cube(10,0,10,10), Cube(10,100,10,10)]
while True:
    frame=np.ones(frame_size)
    for obj in world:
        for tri in obj.tris:
            if (dot(normal(tri),sub(centroid(tri),cam_pos))>0):
                lines=[]
                for points in tri:
                    x = round(((frame_size[0]*(points[1]-cam_pos[1]))/(hfov*distance(points[0:2],cam_pos[0:2])))+(frame_size[0]/2))
                    y = round(((frame_size[1]*(points[2]-cam_pos[2]))/(vfov*distance(points[0:2],cam_pos[0:2])))+(frame_size[1]/2))
                    lines.append([x,y])
                frame=cv2.fillConvexPoly(frame, np.array(lines,dtype=np.int32), color=(shade(sun,tri)))
    cv2.imshow('frame',frame)
    try:
        if keyboard.is_pressed('q'):
            break
        elif keyboard.is_pressed('w'):
            cam_pos[2]+=0.5
        elif keyboard.is_pressed('s'):
            cam_pos[2]-=0.5
        elif keyboard.is_pressed('r+a'):
            cam_pos[0]-=0.5
        elif keyboard.is_pressed('r+d'):
            cam_pos[0]+=0.5
        elif keyboard.is_pressed('a'):
            cam_pos[1]-=0.5
        elif keyboard.is_pressed('d'):
            cam_pos[1]+=0.5
    except:
        pass
    cv2.waitKey(1)
cv2.destroyAllWindows()
