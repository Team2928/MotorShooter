import wpilib

import shooter

from utils import Button

# Joysticks
leftJoy = wpilib.Joystick(2)
rightJoy = wpilib.Joystick(1)

leftMotor = wpilib.Jaguar(1)
rightMotor = wpilib.Jaguar(2)


componets = []
	




class ShooterConfig(object):
	Motor1 = wpilib.Jaguar(1)
	Motor2 = wpilib.Jaguar(2)
	Motor3 = wpilib.Jaguar(3)
	Motor4 = wpilib.Jaguar(4)
	
	shoot_joy = leftJoy
componets.append(shoot.Shoot(ShooterConfig))
# Core Functions
def CheckRestart():
    return
    # We need to do something about this at some point.....
