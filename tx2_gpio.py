#!/usr/bin/env python
from __future__ import print_function

import os
import time

# Sysfs constants
SYSFS_BASE_PATH     = '/sys/class/gpio'

SYSFS_EXPORT_PATH   = SYSFS_BASE_PATH + '/export'
SYSFS_UNEXPORT_PATH = SYSFS_BASE_PATH + '/unexport'

SYSFS_GPIO_PATH           = SYSFS_BASE_PATH + '/gpio%d'
SYSFS_GPIO_DIRECTION_PATH = SYSFS_GPIO_PATH + '/direction'
SYSFS_GPIO_EDGE_PATH      = SYSFS_GPIO_PATH + '/edge'
SYSFS_GPIO_VALUE_PATH     = SYSFS_GPIO_PATH + '/value'
SYSFS_GPIO_ACTIVE_LOW_PATH = SYSFS_GPIO_PATH + '/active_low'

SYSFS_GPIO_VALUE_LOW   = '0'
SYSFS_GPIO_VALUE_HIGH  = '1'

# Public interface
INPUT   = 'in'
OUTPUT  = 'out'

RISING  = 'rising'
FALLING = 'falling'
BOTH    = 'both'

ACTIVE_LOW_ON = 1
ACTIVE_LOW_OFF = 0

DIRECTIONS = (INPUT, OUTPUT)
EDGES = (RISING, FALLING, BOTH)
ACTIVE_LOW_MODES = (ACTIVE_LOW_ON, ACTIVE_LOW_OFF)

class Pin_gpio():

    def __init__(self, number, direction):    
        self._number = number
        self._direction = direction
        self._sysfs_gpio_value_path = SYSFS_GPIO_VALUE_PATH % number
        self._sysfs_gpio_direction_path = SYSFS_GPIO_DIRECTION_PATH % number
        '''
        with open(SYSFS_EXPORT_PATH, 'w') as export:
            export.write(str(self._number))
        
        with open(self._sysfs_gpio_direction_path, 'w') as fsdir:
            fsdir.write(direction)
        '''    
        self._fd = open(self._sysfs_gpio_value_path, 'r+')
            
            
    def set_high():
        self._fd.write(1)
        self._fd.seek(0)        
    
    def set_low():
        self._fd.write(0)
        self._fd.seek(0)    
        
if __name__ == '__main__':
    pin298 = Pin_gpio(298,"OUTPUT")
    
    
    while True:
        pin289.set_high()
        time.sleep(3)
        pin289.set_low()
        time.sleep(1)
    










        
        
