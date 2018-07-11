#prints all numbers from 1-2000 and specifies whether they 
#are odd or even.
import random
def odd_even():
	for number in range(1,2001):
		if number%2 == 0:
			print "Number is " + str(number) + ". This is an even number."
		else:
			print "Number is " + str(number) + ". This is an odd number."	
# odd_even()

a = [2,4,10,16]
def multiply(list,multiplier):
	for index in range(0,len(list)):
		list[index] = list[index]*multiplier
	return list	
# multiply(a,5)		
# print(a)

def layered_multiples(arr):
	print arr
	result = []
	for number in range(0,len(arr)):
		ones_array = []
		for index in range(0,arr[number]):
			ones_array.append(1)
		result.append(ones_array)
	return result		

# x = layered_multiples(multiply([2,4,5],3))
# print x

#Grades Table
def scores_and_grades():
	print "Scores and Grades"
	for index in range(0,10):
		grade = random.randint(60,100);
		if(grade >= 60 and grade <=69):
			print "Score: " +str(grade) +"; Your grade is a D"
		elif(grade >= 70 and grade <=79):
			print "Score: " + str(grade) +"; Your grade is a C"
		elif(grade >=80 and grade <=89):
			print "Score: " + str(grade) +"; Your grade is a B"	
		else:
			print "Score: " + str(grade) +"; Your grade is a A"	
	print "End of the program. Bye!"		
# scores_and_grades()

#Coin Tosses
def coin_tosses(number):
	print "Starting the program..."
	number_of_heads = 0;
	number_of_tails = 0;

	for index in range(1,number+1):
		heads_or_tails = round(random.random())
		response = "Attempt #"+str(index)+": Throwing a coin..."
		if(heads_or_tails == 0):
			response = response + "It's a head!"
			number_of_heads = number_of_heads + 1
		elif(heads_or_tails == 1):
			response = response + "It's a tail!"
			number_of_tails = number_of_tails +1
		response = response +" ... Got " + str(number_of_heads) +" head(s) so far and " + str(number_of_tails) + " tail(s) so far";
		print response;

# coin_tosses(5000)

#Draw Stars	
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(list_of_numbers):
	for element in list_of_numbers:
		line_of_stars = ''
		end_index = 0
		character_repeat = ''
		if(isinstance(element,int)):
			end_index = element
			character_repeat = '*'
		elif(isinstance(element,str)):
			lowercase_string = element.lower()
			end_index = len(element)
			character_repeat = lowercase_string[0]	
		for index in range(0,end_index):
			line_of_stars = line_of_stars + character_repeat
		print line_of_stars	
# draw_stars(x)

#Dictionary Basics
def get_information_about_myself():
	information_about_me = {
	"name":"Susie",
	"age":23,
	"country_of_birth":"United States of America",
	"favorite_languages":["Spanish","English","Italian"]
	}

	print "My name is " + information_about_me['name']
	print "My age is " + str(information_about_me['age'])
	print "My country of birth is " + information_about_me['country_of_birth']
	print "My favorite_languages are " + information_about_me['favorite_languages'][0]
# get_information_about_myself()	

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#Names
def print_names(students):
	for student in students:
		print student['first_name'] + " " + student['last_name']

# print_names(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

#Names part 2
def print_names_numbers(users):
	print "Students"
	student_index = 1
	for student in users['Students']:
		print str(student_index) + ' - ' + student['first_name'].upper() + " " + student['last_name'].upper() + " - " + str(len(student['first_name'])+ len(student['last_name'])) 
		student_index = student_index +1
	instructor_index = 1;
	print "Instructors"
	for instructor in users['Instructors']:
		print str(instructor_index) + ' - ' + instructor['first_name'].upper() + " " + instructor['last_name'].upper() + " - " + str(len(instructor['first_name'])+ len(instructor['last_name'])) 
		instructor_index = instructor_index +1
# print_names_numbers(users)

#Dictionary and Tupples
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dictionary_to_tupples(dictionary):
	list_of_tupples =[]
	for item in dictionary:
		key_value = (item, dictionary[item])
		list_of_tupples.append(key_value)
	print list_of_tupples	
# dictionary_to_tupples(my_dict)	

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dictionary(list1,list2):
	new_dictionary = {}
	key_list = []
	value_list =[]
	if(len(list1) > len(list2)):
		key_list = list1
		value_list = list2
	else:
		key_list = list2
		value_list = list1

	for index in range(0,len(value_list)):
		new_dictionary[key_list[index]] = value_list[index]
	print new_dictionary
make_dictionary(name,favorite_animal)		

def foo_bar():
	for number in range(100,100001):
		isPrime = True
		isPerfectSquare = False	
		for num in range(1,number):
			if (number % num == 0)
				isPrime = False
			if(num*num == number):
				isPerfectSquare =True	
		if(isPrime):
			print number
		if(isPerfectSquare):
			print number		

