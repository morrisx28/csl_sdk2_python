
from .csl_pineapple.msg.dds_ import *

"""
" csl_pineapple.msg.dds_ dafault
"""

def csl_pineapple_msg_dds__Error_():
    return Error_(0, 0)

def csl_pineapple_msg_dds__IMUState_():
    return IMUState_([0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], 0)

def csl_pineapple_msg_dds__MotorCmd_():
    return MotorCmd_(0, 0.0, 0.0, 0.0, 0.0, 0.0, [0, 0, 0])

def csl_pineapple_msg_dds__MotorState_():
    return MotorState_(0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, [0, 0])

def csl_pineapple_msg_dds__LowCmd_():
    return LowCmd_([0, 0], 0, 0, [0, 0], [0, 0], 0, [csl_pineapple_msg_dds__MotorCmd_() for i in range(20)],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0], 0, 0, 0)

def csl_pineapple_msg_dds__LowState_():
    return LowState_([0, 0], 0, 0, [0, 0], [0, 0], 0, [csl_pineapple_msg_dds__IMUState_() for i in range(5)],
                [csl_pineapple_msg_dds__MotorState_() for i in range(20)],
                [0, 0, 0, 0], [0, 0, 0, 0], 0,
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                0, 0, 0, 0, 0.0, 0.0, [0, 0, 0, 0], 0, 0)

def csl_pineapple_msg_dds__TimeSpec_():
    return TimeSpec_(0, 0)

