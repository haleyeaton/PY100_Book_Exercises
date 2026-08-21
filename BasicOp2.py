#Use the REPL and arithmetic operators to extract the individual 
# digits from the number 4936. 
# 1. One place is 6.
# 2. Ten place is 3.
# 3. Hundreds place is 9.
# 4. Thousands place is 4. 
# Each digit may require multiple Python statements.

number = 4936
ones = number % 10
ones
6

number = 4936
tens = (number // 10) % 10
tens
3

number = 4936
hundreds = (number // 100) % 10
hundreds
9

number = 4936
thousands = (number // 1000) % 10
thousands
4

#Use integer division // instead of regular division / to get the 
#integer result of the division. Then use the modulo operator % to get 
#the remainder of the division. The remainder is the digit you want.