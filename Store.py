class Store(object):
	"""docstring for Store"""
	def __init__(self, products, location, owner):
		# super(Store, self).__init__()
		self.products = products;
		self.location = location;
		self.owner = owner;
	def add_product(self, product):
		self.products.append(product);
		return self;
	def remove_product(self,product_name):
		self.products.remove(product_name);
		return self;

	def inventory(self):
		for product in self.products:	
			print product.display_information();