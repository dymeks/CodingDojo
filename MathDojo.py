class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self):
		# super(MathDojo, self).__init__()
		self.result = 0;
	def add(self, *numbers):
		for number in numbers:
			
			if isinstance(number,list):
				for num in number:
					self.result += num;
			elif isinstance(number,tuple): 
				for num in number:
					self.result += num;
			else:
				self.result += number;	
		return self;

	def subtract(self, *numbers):	
		for number in numbers:
			if isinstance(number,list) or isinstance(number,tuple):
				for num in number:
					self.result -= num;
			else: 
				self.result -= number;
		return self;
md = MathDojo();		

print str(md.add([1], (1,2),4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result);