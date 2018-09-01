from math import sin, cos,pi,sqrt

def main():
	f = 200	# [MHz]
	N = 4	# Number of section
	Zr = 50		# [Ohm]
	Thita = pi/2/N
	C1 = 1/(2*pi*f*10**6*sin(Thita)*Zr)/10**(-12)
	L1 = Zr/(2*pi*f*10**6*sin(Thita))*(1+cos(Thita))/10**(-9)
	print('LCL+LCL  C is %0.2fpf'%C1)
	print('LCL+LCL  L is %0.2fnH'%L1)

	L2 = Zr*sin(Thita)/(2*pi*f*10**6)/10**(-9)
	C2 = 1/(2*pi*f*10**6*Zr)*sqrt((1-cos(Thita))/(1+cos(Thita)))/10**(-12)
	print('CLC+CLC  C is %0.2fpf'%C2)
	print('CLC+CLC  L is %0.2fnH'%L2)
if __name__ == '__main__':
	main()