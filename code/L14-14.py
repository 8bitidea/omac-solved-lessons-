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


# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
def play_game(ml_string, parts_of_speech):    
    replaced = ml_string
    r = ""
    # your code here
    w = raw_input("type in a word : ")
#    theWord = ''.join([i for i in ml_string if i.isalpha()])
    for x in parts_of_speech:
    	r = replaced 
    	replaced = r.replace(x,w,int(len(x)))
    return replaced

    
def is_that_part (word):
	for i in test_string:

		if(word == i):
			return False
		else:
			return True


print play_game(test_string, parts_of_speech)       
