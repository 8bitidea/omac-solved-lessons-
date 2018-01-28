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


# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.
from datetime import date

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#daysOfMonths = [ 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    ## From WIKI :
    #if (year is not divisible by 4) then (it is a common year)
	if year % 4 == 0: return bool(1)
	#else if (year is not divisible by 100) then (it is a leap year)
	if year % 100 == 0 :	return bool(0)
	#else if (year is not divisible by 400) then (it is a common year)
	if year % 400 == 300 :	return bool(1)
	#else (it is a leap year)
	else: return bool(0)


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysOfMonths[month - 1]:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    days = date(year2,month2,day2).toordinal() - date(year1,month1,day1).toordinal() #this ran with me . if you have another way please summit it 
#    while dateIsBefore(year1, month1, day1, year2, month2, day2):
#        days += 1
#        year1, month1, day1 = nextDay(year1, month1, day1)
#        if(day1 == 28) and (month1 == 2):
#        	if( isLeapYear(year1)):
#        		if (dateIsBefore(year1, month1, day1, year2, month2, day2)):
#	        		days +=1
#	        	else:
#	        		break
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()