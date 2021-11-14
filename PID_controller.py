import numpy as np

# def PID(_SP, _PV, kp=[1.0, 1.0], ki=0.0, kd=0.0):
#     err=_SP-_PV
#     # print("SP {} ".format(_SP))
#     # print("PV {} ".format(_PV))
#     # print("err {} ".format(err))
#     tau=np.array(
#         [
#             [0], [0]
#         ]
#     )
#     tau[0]=kp[0]*err[0]
#     tau[1]=kp[1]*err[1]
#     # print(tau)
#     return tau

def PID(Kp, Ki, Kd, MV_bar=0):
    # initialize stored data
    e_prev = 0
    dt = 0.001
    I = 0
    
    # initial control
    MV = MV_bar
    
    while True:
        # yield MV, wait for new t, PV, SP
        PV, SP = yield MV
        
        # PID calculations
        e = SP - PV
        
        P = Kp*e
        # print("P {} ".format(P))
        I = I + Ki*e*dt
        D = Kd*(e - e_prev)/dt
        
        MV = MV_bar + P + I + D
        
        # update stored data for next iteration
        e_prev = e
        # t_prev = t