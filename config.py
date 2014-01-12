import wpilib

import shooter

from utils import Button

# Joysticks
leftJoy = wpilib.Joystick(2)
rightJoy = wpilib.Joystick(1)


componets = []
	
class ShooterConfig(object):
	Motor1 = wpilib.Talon(1)
	Motor2 = wpilib.Talon(2)
	Motor3 = wpilib.Talon(3)
	Motor4 = wpilib.Talon(4)
	
	shoot_joy = leftJoy
componets.append(shooter.Shooter(ShooterConfig))
# Core Functions
def CheckRestart():
    return
    # We need to do something about this at some point.....
