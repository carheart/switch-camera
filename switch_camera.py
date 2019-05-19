#!/usr/bin/env python

'''Farmware: switch between USB and Raspberry Pi cameras.'''

import os
import json

from farmware_tools import device
from farmware_tools import get_config_value

switch_camera_to = get_config_value(farmware_name='Switch Camera', config_name='camera_setter', value_type=str)
switch_camera_to = switch_camera_to.strip()
switch_camera_to = switch_camera_to.upper()

device.log(message=switch_camera_to, message_type='info')

if switch_camera_to not in ("RPI", "USB"):
    device.log(message='Wrong input to switch camera provided - shd be USB or RPI', message_type='info')
else:
    camera = os.getenv('camera', 'USB')
    device.set_user_env('camera', json.dumps(switch_camera_to))
    device.log(message='Camera was switched', message_type='info')
    # camera = os.getenv('camera', 'USB')
    # switch_camera_to = 'RPI' if 'USB' in camera else 'USB'
    # device.set_user_env('camera', json.dumps(switch_camera_to))





