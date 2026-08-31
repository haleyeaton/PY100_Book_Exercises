value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')

# We recommend avoiding nested if statements when possible.
# Keep the nesting to a modest 2 or 3 levels deep
# Use functions to isolate complex code. 

# You can have as many elif blocks as you need, 
# but they all need to be after the if block, 
# and before else block (if there is one)

