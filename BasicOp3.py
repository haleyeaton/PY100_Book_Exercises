#What does the following code do? Why?

print('5' + '10')

#The code concatenates two string literals together. 
#The result is '510', not '15' because it is concatenating two strings,
#not adding two integers/performing arithmetic addition. 

#Refactor the code from the previous exercise to use coercion to print 15.

print(int('5') + int('10'))

#The code uses coercion to convert the string literals '5' and '10'
#into integers. Then, it adds the two integers together to get 15.

