#!/usr/bin/env python

'''Farmware: switch between USB and Raspberry Pi cameras.'''

import os
import json
#import farmware_tools


#try:

from farmware_tools import device
from farmware_tools import get_config_value

switch_camera_to = get_config_value('Switch Camera', 'camera_setter')

switch_camera_to = switch_camera_to.strip();
switch_camera_to = switch_camera_to.capitalize();

if switch_camera_to != "RPI" or switch_camera_to != "USB":
    device.log(message='Wrong input to switch camera provided - shd be USR or RPI', message_type='info')
else:
    camera = os.getenv('camera', 'USB')
    device.set_user_env('camera', json.dumps(switch_camera_to))

    # camera = os.getenv('camera', 'USB')
    # switch_camera_to = 'RPI' if 'USB' in camera else 'USB'
    # device.set_user_env('camera', json.dumps(switch_camera_to))


#except Exception as error:
#    farmware_tools.device.log(repr(error))


