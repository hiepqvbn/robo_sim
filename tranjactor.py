import numpy as np
from math import atan2, sqrt, sin, cos, atan2
import glb_


def Tranjator(goal, start):
    l=goal-start
    l_tranj=sqrt(l[0][0]**2+l[1][0]**2)
    a=(goal[1][0]-start[1][0])/(goal[0][0]-start[0][0])
    b=goal[1][0]-a*goal[0][0]
    alpha=atan2((goal[1][0]-start[1][0]),(goal[0][0]-start[0][0]))
    N=int(l_tranj/glb_.del_l)
    xd=[]
    xd.append(start)
    for i in range(N):
        x_d=np.array(
            [
                [xd[i][0][0]+glb_.del_l*cos(alpha)],
                [xd[i][1][0]+glb_.del_l*sin(alpha)]
            ]
        )
        xd.append(x_d)

    xd.append(goal)

    return xd

if __name__=="__main__":
    
    q=np.array(
        [
            [-1.4708], [0.2]
        ]
    )
    
    goal=np.array(
        [
            [-2.0], [1.2]
        ]
    )
    xd=Tranjator(goal,q)
    for i in xd:
        print("next q {} ".format(i))