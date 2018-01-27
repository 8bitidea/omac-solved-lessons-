#-------------------------------------------
#One Million Arabic Coder (OMRC)
#patch Full Stack Web Dev .1
#Lisson 13 Problem Solving 
#this is test no 22
#I'm Byte idea (Say Hi : 8bitidea@gmail.com)
#-------------------------------------------


###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if(day == 30):
    	if (month == 12):
    		year += 1
    		month = 1
    		day = 1
    	else : 
    		month += 1 
    		day = 1
    else :
    	day += 1

    return (year , month , day)

print nextDay (2012, 12, 30)