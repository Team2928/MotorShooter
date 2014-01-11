import common 

__all__= ['Shooter']


class Shooter(common.ComponentBase):

	def __init__(self.config):
		self.joystick = config.leftJoy
		self.Motor1 = config.Motor1
		self.Motor2 = config.Motor2
		self.Motor3 = config.Motor3
		self.Motor4 = config.Motor4
	

	def op_init(self):
		self.shooter_motor.Set(0)


	def op_tick(self, Time):
		speed  = (self.joystick.GetY())
		Motor1.Set = speed
		Motor2.Set = speed
		Motor3.Set = speed
		Motor4.Set = speed
