# *** match statement ***

value = 5

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _: # default case
        print('value is neither 5 nor 6')
# value is 5

#*** if/else statement ***

value = 5

if value == 5:
    print('value is 5')
elif value == 6:
    print('value is 6')
else:
    print('value is neither 5 nor 6')
# value is 5

# functionally identical, but the match statement evaluates the expression,
# 'value' and compares it's value to the value in each case, and 
# executes the the block associated with the first matching case
# If you want to match multiple values in a case, 
# you can do so by using the | character to separate item values

value = 5

match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _: # default case
        print('value is not 1, 2, 3, 4, 5, or 6')
# value is 5 or 6
