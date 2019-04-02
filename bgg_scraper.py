import urllib.request
import os
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")

for i in range(2):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	print(str(i) + ": " + current_time_stamp)
	f = open("html_files/bgg" + current_time_stamp + ".html", "wb")
	response = urllib.request.urlopen('https://boardgamegeek.com/browse/boardgame')
	html = response.read()
	f.write(html)
	f.close()
	print("Requesting Board Game Geek")
	time.sleep(17)