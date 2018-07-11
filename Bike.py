class Bike(object):
	"""docstring for Bike"""
	def __init__(self, price,max_speed):
		# super(Bike, self).__init__()
		self.price = price;
		self.max_speed = max_speed;
		self.miles = 0;
		
	def displayInfo(self):
		print "Price: " + str(self.price);
		print "Maximum Speed: " + str(self.max_speed);
		print "Total Miles: " + str(self.miles);
	def ride(self):
		print "Riding..."
		self.miles = self.miles + 10;
	def reverse(self):
		print "Reversing..."
		self.miles = self.miles - 5;

bike_one = Bike("200","25mph");		
bike_two = Bike("100","10mph");
bike_three = Bike("150","15mph");

print bike_three.displayInfo()
bike_three.ride()				   	
print bike_three.displayInfo()
bike_three.reverse()
print bike_three.displayInfo()
