#Will an error occur if you try to access a list element with an index greater
#than or equal to the list length? For example:

foo = ['a', 'b', 'c']
print(foo[3])       #Will this result in an error?

#Yes, an IndexError will occur. The list foo has a length of 3,
# so the valid indices are 0, 1, and 2. The index 3 is out of range.
