import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from math import sin,cos
from jacobi import Jacobi
from tranjactor import Tranjator, Tranjator2
from manipulator1 import in_range, manipulator1, finger_pos
from PID_controller import PID
import glb_

T=15
dispt = 0.05
duration=0

goal1=np.array(
    [
        [1.5], [1.2]
    ]
)
goal2=np.array(
    [
        [-1.5], [1.2]
    ]
)
goals=[]
for i in range(0,int(T/glb_.dt)):
    del_g= (goal2[0][0]-goal1[0][0])/int(T/glb_.dt)
    g=np.array(
        [
            [1.5+del_g*i], [1.2]
        ]
    )
    goals.append(g)
goal=goals[0]

if in_range(goal):
    print("OK")


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
xd, N=Tranjator(goal, finger_pos(q))
# xd_x=[]
# for x in xd:
#     xd_x.append(x[0][0])
# xd_y=[]
# for y in xd:
#     xd_y.append(y[1][0])

q_goal=q
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

controller1 = PID(250, 65, 165)        # create pid control
controller1.send(None)              # initialize
controller2 = PID(200, 45, 145)        # create pid control
controller2.send(None)              # initialize

for t in range(0,int(T/glb_.dt)):      #int(T/glb_.dt)
    # q_.append(q)
    q1, q1d = manipulator1(q, qdot, tau)
    q=q1
    # print("q {} ".format(q1))
    qdot=q1d
    tau[0] = controller1.send([q[0], q_goal[0]])
    tau[1] = controller2.send([q[1], q_goal[1]])
    # goal=goals[t]
    if t<N:
        x_d=xd[t]
    else:
        x_d=goal
    f_p=finger_pos(q)
    # x_d=Tranjator2(goal, f_p)
    del_x=x_d-f_p
    del_theta=np.matmul(np.linalg.inv(Jacobi(q)), del_x)
    q_goal=q+del_theta
    if not in_range(finger_pos(q_goal)):
        print("Out range")
        break
    # print("tau {} ".format(tau))
    duration=duration+glb_.dt
    if duration>dispt:
        im1=plt.plot([0,glb_.l1*cos(q[0][0])],[0,glb_.l1*sin(q[0][0])],'ro-')
        im2=plt.plot([glb_.l1*cos(q[0][0]),glb_.l1*cos(q[0][0]) + glb_.l2*cos(q[0][0] + q[1][0])],[glb_.l1*sin(q[0][0]),glb_.l1*sin(q[0][0]) + glb_.l2*sin(q[0][0] + q[1][0])],'co-')
        im_q_goal=plt.plot([glb_.l1*cos(q_goal[0][0]) + glb_.l2*cos(q_goal[0][0] + q_goal[1][0])],[glb_.l1*sin(q_goal[0][0]) + glb_.l2*sin(q_goal[0][0] + q_goal[1][0])],'g+')
        # xxd, NN=Tranjator(goal, finger_pos(q))
        # xd_x=[]
        # for x in xxd:
        #     xd_x.append(x[0][0])
        # xd_y=[]
        # for y in xxd:
        #     xd_y.append(y[1][0])
        im_tranj=plt.plot([finger_pos(q)[0][0], goal[0][0]],[finger_pos(q)[1][0], goal[1][0]],'r--')
        im_goal=plt.plot([goal[0][0]],[goal[1][0]],'bD')
        ims.append(im1+im2+im_q_goal+im_goal+im_tranj)
        duration=0


plt.xlim([-3, 3])
plt.ylim([-3, 3])
ax.set_aspect('equal', adjustable='box')
ani = animation.ArtistAnimation(fig, ims, interval=50)
f = r"animation.gif" 
writergif = animation.PillowWriter(fps=30) 
ani.save(f, writer=writergif)
plt.show()