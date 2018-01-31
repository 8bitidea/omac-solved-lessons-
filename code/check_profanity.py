#lesson 20-10
#One Million Arabic Coder patch .1
import urllib

def read_text():
	f = open(r"/Users/Macintosh/Downloads/language-timothy-master/profanity-list.txt")
	fc =  f.read()
	print fc
	check_profanity(fc)
	f.close()


def check_profanity (f):
	p = urllib.urlopen("http://www.wdylike.appspot.com/?q="+f)
	print p.read()
	p.close()



read_text()
