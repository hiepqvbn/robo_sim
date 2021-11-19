import numpy as np
from math import sin, cos
import glb_

def Jacobi(q):
    j = np.array(
        [
            [-glb_.l1*sin(q[0][0])-glb_.l2*sin(q[0][0]+q[1][0]), -glb_.l2*sin(q[0][0]+q[1][0])],
            [glb_.l1*cos(q[0][0])+glb_.l2*cos(q[0][0]+q[1][0]), glb_.l2*cos(q[0][0]+q[1][0])]
        ]
    )
    return j

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
    
    j=Jacobi(q)
    print("j {} ".format(j))