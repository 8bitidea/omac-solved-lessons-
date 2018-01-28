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

# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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

def bigger (x,y):
	if x>y : return x
	else: return y

def smaller (x,y):
	if x<y : return x
	else: return y

def daysBetweenDates(y1, m1, d1, y2, m2, d2):

    #sorting the big year for the mathmaticals
	years = int(bigger(y1,y2)) - int(smaller(y1,y2))
	r1 = 0
	if years != 0:
		years *= 12
		x= 0
		while (years != 0):
			if (x == 12) : x = 0
			r1+=daysOfMonths[x]
			x+=1
			years -=1
	mb = bigger (m1,m2)
	ms = smaller (m1,m2)
	months = mb - ms
	if( months != 0):
		while (mb != ms):
			r1 += daysOfMonths[mb]
			mb -= 1
	day = bigger(d1,d2) - smaller(d1,d2)
	if(day != 0):
		r1 += day
	return r1


print isLeapYear(1900)
print daysBetweenDates(2011, 6, 30, 2012, 6, 30)