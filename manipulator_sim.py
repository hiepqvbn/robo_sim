import numpy as np
import matplotlib.pyplot as plt
from manipulator1 import manipulator1
import glb_

T=20
dispt = 1/24
duration=0

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

q_=[]

fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))
plt.plot(x, np.sin(x))


for t in range(0,int(T/glb_.dt)):
    q_.append(q)
    q1, q1d = manipulator1(q, qdot, tau)
    q=q1
    qdot=q1d
    duration=duration+glb_.dt
    if duration>0:

        duration=0

