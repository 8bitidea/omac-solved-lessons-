import webbrowser
class Movie():
	def __init__(self,title,storyline,poster,youtube):
		self.title = title
		self.storyline = storyline
		self.poster = poster
		self.youtube = youtube

	def ShowTrailer(self):
		webbrowser.open(self.youtube)