from bs4 import BeautifulSoup as Bs
import os, re, requests, time

def re_html(html,oldtag,newtag):
	oldtags = oldtag.split('...')
	index0 = html.find(oldtags[0])
	index1 = html.find(oldtags[1])

	if index0!=-1 and index1!=-1:
		html = html.replace(html[index0:index1+len(oldtags[1])],newtag)
	
	return html

k = 0

while 1:
	##### BOOKMARKS
	htmllines = []
	k+=1
	
	os.system("git commit -a -m 'Auto Summary'")
	os.system("git push origin 'main'")
	print(k)

	with open('/home/tima/Документы/GitHub/newrep/timaracov.github.io/static/docs/bookmark.dtb') as f:
		links = f.readlines()

	for i in range(len(links)):
		links[i] = links[i].split('<----->')
		sublink = links[i][0].split(' ')
		if len(sublink)>9:
			links[i][0] = ''.join(sublink[:len(sublink)//2])
			
		htmllines.append("\t\t\t<p> <a href={}> {} </a> </p>\n".format(links[i][1],links[i][0]))

	with open('/home/tima/Документы/GitHub/newrep/timaracov.github.io/pages/bmrk.html','r') as f:
		htmlfile = f.read()
		htmllines = '<div>\n'+''.join(htmllines)+'</div>'
		htmlfile = re_html(htmlfile,'<div>...</div>',htmllines)

	with open('/home/tima/Документы/GitHub/newrep/timaracov.github.io/pages/bmrk.html','w') as f:
		f.write(htmlfile)

	##### MUDIC FILES
	music_files = os.listdir('/home/tima/Документы/GitHub/newrep/timaracov.github.io/static/music/')

	for i in range(len(music_files)):
		music_files[i] = f'\t\t\t<p><a href="/static/music/{music_files[i]}">{music_files[i]}</a></p>\n'

	with open('/home/tima/Документы/GitHub/newrep/timaracov.github.io/pages/music.html','r') as f:
		htmlfile = f.read()
		htmllines = '<div>\n'+''.join(music_files)+'</div>'
		htmlfile = re_html(htmlfile,'<div>...</div>',htmllines)

	with open('/home/tima/Документы/GitHub/newrep/timaracov.github.io/pages/music.html','w') as f:
		f.write(htmlfile)

	time.sleep(200)
