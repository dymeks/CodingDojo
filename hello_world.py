words = "It's thanksgiving day. It's my birthday,too!"
words_replaced_month = words.replace('day','month')
max_array = [-1,6,8,20,-16]
result = [max_array[0],max_array[len(max_array)-1]]
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()

first_half = x[0:int(round(len(x)/2))]
second_half = x[(int(round(len(x)/2))-1):]
second_half[0] = first_half
print second_half
# print result
# print words.find('day')
# print max(max_array)
# print min(max_array)
# print words_replaced_month