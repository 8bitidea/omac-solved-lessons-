#-------------------------------------------
#One Million Arabic Coder (OMRC)
#patch Full Stack Web Dev .1
#Lisson 13 Problem Solving 
#Please note that i am sharing this code to 
#find  the idea behined the problem not for
#copy and pasting !
#and i wish if you can find a mistake or ha
#ve a better answer let me know or correct 
#me please
#thank you in advance for correcting me ;)
#I'm Byte idea (Say Hi : 8bitidea@gmail.com)
#-------------------------------------------

# Now, we want to ask ourselves the question: How many occurrences of 
# the number 9 appear in our randomly made list?
# 
# For example, if we have a list: [2,8,9,9,4,5,9], we want to figure out
# how to loop through the list and count the number of occurrences of the
# number 9. In the example list above, the number 9 occurs three times.

import random

# 1. Create random list of integers using while loop
random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))
    
# Write code here to loop through the list and count all occurrences
# of the number 9. Note that `if` statements and `while` loops will help you solve
# this problem.
x = count = 0
while x < list_length:
	if(random_list[x] == 9):
		count += 1
	x+=1



# Test: If the `while` loop we wrote works, we should manually count
# how many times the number 9 is present in the list.
print random_list
print count
