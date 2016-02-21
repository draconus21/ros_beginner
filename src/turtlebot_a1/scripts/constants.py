#!/usr/bin/env python

CMD_VEL         = '/cmd_vel_mux/input/teleop'
#CMD_VEL         = '/mobile_base/commands/velocity'
SCAN            = '/scan/'
SET_MODEL_STATE = '/gazebo/set_model_state'
MODEL_STATES    = '/gazebo/model_states'
MOVE_BOT_SRV    = 'move_bot'
BOT             = 'mobile_base'

RATE     = 4
Q_SIZE   = 1000
ANG_SPD  = 1
FWD_SPD  = 1
DURATION = 0.25 

DEF_X   = 0
DEF_Y   = 0
N_LASER = 640

## Direction
FWD   =  1
BACK  = -1
LEFT  = -1
RIGHT =  1

##BOT STATES
B_CLEAR     = 0
B_OBS_LEFT  = 1
B_OBS_RIGTH = 2
B_WALL_FLW  = 3
B_END_WALL  = 4

##WALL CONSTANTS
W_UNKNOWN = -1
W_LEFT    =  0
W_RIGHT   =  1
W_FRONT   =  2
W_REAR    =  3
