import os

def rename_files():
	file_list = os.listdir(r"/Users/Macintosh/Documents/test")
	print file_list

	for file_name in file_list:
		dirr = "/Users/Macintosh/Documents/test/"+file_name
		print dirr
		print os.getcwd()
		os.rename(dirr,dirr.translate(None,"0123456789"))



rename_files()