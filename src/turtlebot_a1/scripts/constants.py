#!/usr/bin/env python

CMD_VEL         = '/cmd_vel_mux/input/teleop'
#CMD_VEL         = '/mobile_base/commands/velocity'
SCAN            = '/scan/'
SET_MODEL_STATE = '/gazebo/set_model_state'
MODEL_STATES    = '/gazebo/model_states'
MOVE_BOT_SRV    = 'move_bot'
BOT             = 'mobile_base'

DIST_THRESH = 1
ANG_THRESH  = 3

RATE     = 4
Q_SIZE   = 1000
ANG_SPD  = 0.5
FWD_SPD  = 0.5
DURATION = 0.25 

DEF_X   = 0
DEF_Y   = 0
N_LASER = 640

## Direction
FWD    =  1
BACK   = -1
LEFT   = -1
RIGHT  =  1
CENTER =  0

##BOT STATES
B_UNKNOWN = -1
B_CLEAR   =  0
B_FWD     =  1
B_BK      =  2
B_LEFT    =  3
B_RIGHT   =  4

##WALL CONSTANTS
W_UNKNOWN = -1
W_LEFT    =  0
W_RIGHT   =  1
W_FRONT   =  2
W_REAR    =  3
