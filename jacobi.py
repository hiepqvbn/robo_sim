import numpy as np
from math import sin, cos
import glb_

def Jacobi(q,l1,l2):
    j = np.array(
        [
            [-l1*sin(q[0][0])-l2*sin(q[0][0]+q[1][0]), -l2*sin(q[0][0]+q[1][0])],
            [l1*cos(q[0][0])+l2*cos(q[0][0]+q[1][0]), l2*cos(q[0][0]+q[1][0])]
        ]
    )
    return j