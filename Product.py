class Product(object):
	"""docstring for Product"""
	def __init__(self, price, item_name, weight, brand):
		# super(Product, self).__init__()
		self.price = price;
		self.item_name = item_name;
		self.weight = weight;
		self.brand = brand;
		self.status = "for sale";
		
	def sell(self):
		self.status = "sold";
		return self;

	def add_tax(self,tax):
		price = (self.price*tax) + self.price;
		return price;
	def return_item(self,reason_returning):
		if(reason_returning == 'defective'):
			self.status = "defective";
			self.price = 0;
		elif(reason_returning == 'like new'):
			self.status = 'for sale';
		elif(reason_returning == 'opened'):
			self.price = self.price - (self.price*.2);
			self.status = 'used';
		return self;	
	def display_information(self):
		information = "Price: " + str(self.price) +"\n Item Name: " + self.item_name +"\n Weight: " +self.weight +"\n Brand: " + self.brand + "\n Status: " + self.status;	
		print information;
		return self;				



