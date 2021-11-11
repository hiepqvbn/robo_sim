import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from math import sin,cos
from manipulator1 import manipulator1
import glb_

T=10
dispt = 0.05
duration=0

tau=np.array(
        [
            [0], [0]
        ]
    )
q=np.array(
    [
        [-1.9708], [0.2]
    ]
)
qdot=np.array(
    [
        [0], [0]
    ]
)

q_=[]

# plt.figure(figsize=(1,1))
fig = plt.figure()
ax = fig.add_subplot(111)


ims=[]

for t in range(0,int(T/glb_.dt)):
    q_.append(q)
    q1, q1d = manipulator1(q, qdot, tau)
    q=q1
    qdot=q1d
    duration=duration+glb_.dt
    if duration>dispt:
        im1=plt.plot([0,glb_.l1*cos(q[0][0])],[0,glb_.l1*sin(q[0][0])],'ro-')
        im2=plt.plot([glb_.l1*cos(q[0][0]),glb_.l1*cos(q[0][0]) + glb_.l2*cos(q[0][0] + q[1][0])],[glb_.l1*sin(q[0][0]),glb_.l1*sin(q[0][0]) + glb_.l2*sin(q[0][0] + q[1][0])],'bo-')
        ims.append(im1+im2)
        duration=0


plt.xlim([-3, 3])
plt.ylim([-3, 3])
ax.set_aspect('equal', adjustable='box')
ani = animation.ArtistAnimation(fig, ims, interval=50)
f = r"animation.gif" 
writergif = animation.PillowWriter(fps=30) 
ani.save(f, writer=writergif)
plt.show()