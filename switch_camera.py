#!/usr/bin/env python

'''Farmware: switch between USB and Raspberry Pi cameras.'''

import os
import json

from farmware_tools import device
from farmware_tools import get_config_value

switch_camera_to = get_config_value(farmware_name='Switch Camera', config_name='camera_setter', value_type=str)
switch_camera_to = switch_camera_to.strip()
switch_camera_to = switch_camera_to.upper()

if switch_camera_to not in ("RPI", "USB"):
    message = "Wrong input to switch camera provided  ", switch_camera_to, ". Values USB or RPI shd be used"
    device.log(message, message_type='info')
else:
    camera = os.getenv('camera', 'USB')
    device.set_user_env('camera', json.dumps(switch_camera_to))
    message = "Camera was switched to ", switch_camera_to
    device.log(message, message_type='success')






