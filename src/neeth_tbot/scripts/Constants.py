#!/usr/bin/env python

CMD_VEL         = '/cmd_vel_mux/input/teleop'
#CMD_VEL         = '/mobile_base/commands/velocity'
SCAN            = '/scan/'
SET_MODEL_STATE = '/gazebo/set_model_state'
BOT             = 'mobile_base'

RATE     = 4
Q_SIZE   = 1000
ANG_SPD  = 1
FWD_SPD  = 1
DURATION = 1

## Direction
FWD   =  1
BACK  = -1
LEFT  =  1
RIGHT = -1
