import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from math import sin,cos
from manipulator1 import manipulator1
from PID_controller import PID
import glb_

T=15
dispt = 0.05
duration=0

q_goal=np.array(
    [
        [1.0708], [-0.6]
    ]
)

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

# g=[0, 0]
# def onclick(event):
#     # print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
#         #   ('double' if event.dblclick else 'single', event.button,
#         #    event.x, event.y, event.xdata, event.ydata))
#     if not event.dblclick and event.button==1:
#         print('ok')
#         g[0]=event.x
#         g[1]=event.y
#         print(g[0])

# plt.show()
# while g[0]==0 or g[1]==0:
#     cid = fig.canvas.mpl_connect('button_press_event', onclick)

controller1 = PID(150, 35, 45)        # create pid control
controller1.send(None)              # initialize
controller2 = PID(100, 25, 32)        # create pid control
controller2.send(None)              # initialize

for t in range(0,int(T/glb_.dt)):      #int(T/glb_.dt)
    # q_.append(q)
    q1, q1d = manipulator1(q, qdot, tau)
    q=q1
    # print("q {} ".format(q1))
    qdot=q1d
    tau[0] = controller1.send([q[0], q_goal[0]])
    tau[1] = controller2.send([q[1], q_goal[1]])
    # print("tau {} ".format(tau))
    duration=duration+glb_.dt
    if duration>dispt:
        im1=plt.plot([0,glb_.l1*cos(q[0][0])],[0,glb_.l1*sin(q[0][0])],'ro-')
        im2=plt.plot([glb_.l1*cos(q[0][0]),glb_.l1*cos(q[0][0]) + glb_.l2*cos(q[0][0] + q[1][0])],[glb_.l1*sin(q[0][0]),glb_.l1*sin(q[0][0]) + glb_.l2*sin(q[0][0] + q[1][0])],'bo-')
        im_goal=plt.plot([glb_.l1*cos(q_goal[0][0]) + glb_.l2*cos(q_goal[0][0] + q_goal[1][0])],[glb_.l1*sin(q_goal[0][0]) + glb_.l2*sin(q_goal[0][0] + q_goal[1][0])],'gx')
        # im_goal2=plt.plot(g[0],g[1],'go')
        ims.append(im1+im2+im_goal)
        duration=0


plt.xlim([-3, 3])
plt.ylim([-3, 3])
ax.set_aspect('equal', adjustable='box')
ani = animation.ArtistAnimation(fig, ims, interval=50)
# f = r"animation.gif" 
# writergif = animation.PillowWriter(fps=30) 
# ani.save(f, writer=writergif)
plt.show()