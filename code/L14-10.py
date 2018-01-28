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


# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    b = 0
    if (len(list_of_numbers) > 0):
    	for x in list_of_numbers:
    		if (x == 0) or (b < x) : b = x
    	return b
    return 0


print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
