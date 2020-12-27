import os

files = os.listdir(f'{os.getcwd()}/docs')
for index,file in enumerate(files):
	name = "<p><a href={}> {}</a></p>".format(file,file)
	print(name)
