# #Multiples part 1:
# for number in range(1,1001):
# 	if(number%2 == 1):
# 		print number

# #Print multiples of 5 from 5 to 1,000,000:
# for number in range(5,1000001):
# 	if(number%5 == 0):
# 		print number

# #SUM LIST:
# sum1 = 0
# arr = [134,23,1,6,45,89]
# for number in arr:
# 	sum1 += number
# print sum1	


# #Average List:
# sum2 = 0
# arr = [134,23,1,6,45,89]
# for number in arr:
# 	sum2 += number
# print sum2/len(arr)
# try this either as a .py file or in the python shell
import turtle
#Assignment Filter By TYPE:
def filter_by_type(value):
	print 
	if(isinstance(value,int)):
		if(value >=100):
			print "That's a big number!"
		elif (value < 100):
			print "That's a small number"	
	elif (isinstance(value,str)):
		if(len(value)>=50):
			print "Long sentence"
		else:
			print "Short sentence"
	elif(isinstance(value,list)):
		if(len(value)>= 10):
			print "Big List!"
		else:
			print "Short list."			

# filter_by_type("hello") #prints Short Sentence
# filter_by_type("This is a really really really really really long sentence.") #prints Long sentence
# filter_by_type(200) #prints That's a big number!
# filter_by_type(10) #prints That's a small number.
# filter_by_type([1,3,34,2345,234,23,4,234,234,234,234]) #prints Big List!
# filter_by_type([1,2,3,4])# prints Small List.	

#TYPE LIST
# l = ['magical unicorns',19,'hello',98.98,'world'] #Test case for mixed list
# l = [2,3,1,7,4,12] # test case for type ints
l = ['magical','unicorns'] #test case for type string
l = [] 
def typeList(input_list):
	sum = 0;
	result_string = '';
	if(len(input_list) == 0):
		print "You have submitted an empty string"
	for element in input_list:
		if(isinstance(element,str)):
			result_string = result_string + element + " ";
		elif(isinstance(element,int)):
			sum += element;
	print "The sum of the elements = " + str(sum)
	print "Here are the string elements in the list: " + result_string	

	if(sum != 0 and len(result_string) > 0):
		print 'Type: mixed'
	elif (sum > 0):
		print "Type: int"
	elif(len(result_string) > 0):
		print "Type: str"			

# typeList(l)

#COMPARE LISTS
# list_one = [1,2,5,6,2] #These two check the case where the lists 
# list_two = [1,2,5,6,2] #are identical.

# list_one = [1,2,5,6,5]   #These two check the case where the lists 
# list_two = [1,2,5,6,5,3] #are different lengths.

# list_one = [1,2,5,6,5,16] #These two check the case where the lists 
# list_two = [1,2,5,6,5]    #are different lengths.

list_one = ['celery','carrots','bread','milk']  #This case test two lists that are
list_two = ['celery','carrots','bread','cream'] #the same length but NOT identical.

def compare_lists(list1,list2):
	isTheSame = True;
	if(len(list2) != len(list1)):
		isTheSame = False
	else:	
		for index in range(0,len(list1)):
			print str(index) + " " + str(list1[index])
			if(list1[index] != list2[index]):
				isTheSame = False
				break
	
	if(isTheSame):
		print "The lists are identical"	
	else:
		print "The lists are not identical"	

# compare_lists(list_one,list_two)	

#FIND CHARACTERS
word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def find_characters(word_list,character):
	new_list = []
	for word in word_list:
		for letter in word:
			if(letter == character):
				new_list.append(word)
				break
	print new_list			

# find_characters(word_list,char)

#Checkerboard

def create_checkerboard():
	for row in range(1,9):
		if(row%2 == 0):
			print " * * * *"
		else:
			print "* * * * "	
# create_checkerboard()

def create_mulitiplication_table():
	first_row ='* '
	for num in range (1,13):
		first_row = first_row + str(num) + " "
	print first_row
		
	for row in range(1,13):
		print_row = ''
		for col in range(1,13):
			print_row = print_row + str(row*col) +" ";
		print print_row
		# print str(row)  + "\n cl"	
# create_mulitiplication_table()	

def print_prime_print_square():
	for number in range(100,100001):
		isPrime = false;
		for  in 


# the distance we want the pointer to travel each time
DIST = 100
for x in range(0,6):
    print "x", x
    for y in range(1,5):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.right(90)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 20			