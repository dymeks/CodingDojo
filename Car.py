class Car(object):
	"""docstring for Car"""
	
	def __init__(self, price,speed,fuel,mileage):
		# super(Car, self).__init__()
		self.price = price;
		self.speed = speed;
		self.fuel = fuel;
		self.mileage = mileage;

		if(self.price > 10,000):
			self.tax  = .15;
		else:
			self.tax = .12;

		print self.display_all()

	def display_all(self):
		display = "Price = " +str(self.price) + "\n Speed: " +str(self.speed) +"\n Fuel: " + str(self.fuel) +"\n Mileage: " + str(self.mileage) +"\n Tax: " + str(self.tax);
		return display;	
		

car1 = Car(40000,"60mph","Full","20mpg");
car2 = Car(60000,"90mph","Full","40mpg");
car3 = Car(20000,"60mph","Empty","20mpg");
car4 = Car(5000,"30mph","Not Full","40mpg");
car5 = Car(40500,"60mph","Full","30mpg");
car6 = Car(50000,"60mph","Full","90mpg");
