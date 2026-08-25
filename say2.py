def say(text):
    print(text)

say('hello')
say('hi')
say('how do you do')
say('Quite all right')

# illustrates how we define and call a function
# that takes a value known as an argument.
# We assign the argument's value to the text parameter inside say.
# Parameters - the names between parentheses in the function definition.

def say(text='hello'):
    print(text + '!')

say('Howdy') # Howdy!
say()        # hello!

#default parameters