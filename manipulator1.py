import numpy as np
from math import cos, e, sin, sqrt
import glb_
from jacobi import Jacobi

def manipulator1(q, qdot, tau):

    theta=q
    thetadot=qdot

    lg1=glb_.l1*0.5
    lg2=glb_.l2*0.5

    M11=glb_.m1*lg1**2+glb_.I1+glb_.m2*(glb_.l1**2+lg2**2 +2*glb_.l1*lg2*cos(theta[1][0]))+glb_.I2
    M12=glb_.m2*(lg2**2+glb_.l1*lg2*cos(theta[1][0]))+glb_.I2
    M22=glb_.m2*lg2**2+glb_.I2
    g1 =glb_.m1*glb_.ghat*lg1*cos(theta[0][0])+glb_.m2*glb_.ghat*(glb_.l1*cos(theta[0][0])+lg2*cos(theta[0][0]+theta[1][0]))
    g2 =glb_.m2*glb_.ghat*lg2*cos(theta[0][0]+theta[1][0])

    h122=-glb_.m2*glb_.l1*lg2*sin(theta[1][0])
    h112=h122
    h211=-h122

    h1 = h122*thetadot[1][0]**2+2*h112*thetadot[0][0]*thetadot[1][0]
    h2 = h211*thetadot[0][0]**2

    M=np.array(
        [
            [M11, M12],
            [M12, M22]
        ]
    )

    g=np.array(
        [
            [g1],
            [g2]
        ]
    )

    h=np.array(
        [
            [h1],
            [h2]
        ]
    )

    qddot= np.matmul(np.linalg.inv(M),(tau-h-g))

    newqdot=qdot+qddot*glb_.dt
    # print(newqdot)
    newq=theta+thetadot*glb_.dt
    # print(newq)

    return newq, newqdot

def finger_pos(q):
    f_pos = np.array(
        [
            [glb_.l1*cos(q[0][0]) + glb_.l2*cos(q[0][0] + q[1][0])],
            [glb_.l1*sin(q[0][0]) + glb_.l2*sin(q[0][0] + q[1][0])]
        ]
    )
    return f_pos

def in_range(goal):
    l=goal-glb_.O
    l_len=sqrt(l[0][0]**2+l[1][0]**2)
    if l_len > glb_.l1+glb_.l2:
        return False
    else:
        return True

if __name__=="__main__":
    tau=np.array(
        [
            [0], [0]
        ]
    )
    q=np.array(
        [
            [-1.4708], [0.2]
        ]
    )
    qdot=np.array(
        [
            [0], [0]
        ]
    )
    goal=np.array(
        [
            [-2.0], [1.2]
        ]
    )
    del_x=goal-finger_pos(q)
    # q1,q1d=manipulator1(q,qdot,tau)
    # print("q {} ".format(q1d))
    f=finger_pos(q)
    del_theta=np.matmul(np.linalg.inv(Jacobi(q)), del_x)
    q_goal=q+del_theta
    print("q {} ".format(q))
    print("next q {} ".format(q_goal))