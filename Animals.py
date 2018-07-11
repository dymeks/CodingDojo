class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name,health):
		super(Animal, self).__init__()
		self.name = name
		self.health = health
	
	def walk(self):
		self.health = self.health -1;
		return self;

	def run(self):
		self.health = self.health -5;
		return self

	def displayHealth(self):
		print self.health;
		return self;

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name):
		# super(Dog, self).__init__()
		self.name = name;
		self.health = 150;
	def pet(self):
		self.health = self.health + 5;
		return self;
class Dragon(Animal):
	"""docstring for Dragon"""
	def __init__(self, name):
		# super(Dragon, self).__init__()
		self.name = name;
		self.health = 170;
	def fly(self):
		self.health = self.health - 10;
		return self;
	def displayHealth(self):
		super(Dragon, self).displayHealth();
		print "I am a Dragon!"												
						
golden = Dog("golden")
golden.walk();
golden.walk();
golden.walk();
golden.run();
# golden.fly();
golden.run().pet().displayHealth();

drogo = Dragon("dragon");
drogo.walk()
drogo.walk()
drogo.walk()
drogo.run()
# drogo.pet()
drogo.fly()
drogo.run().displayHealth();

horse = Animal("horse",40);
horse.walk()
horse.walk()
horse.walk()
horse.run()
# horse.pet()
# horse.fly()
horse.run().displayHealth();