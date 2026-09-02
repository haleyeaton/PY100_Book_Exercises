names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):  #while the index is less than the length of 'names'
    upper_name = names[index].upper() #names.upper() func changes to uppercase
    upper_names.append(upper_name) #see below
    index += 1 #modifies the index to increase by 1 (0, 1, 2, 3(Victor))

print(upper_names)

#.append(upper_name) adds the value stored in 'upper_name' to the end of 
# the 'upper_names' list. append mutates the list by adding one new element
# at the end. 