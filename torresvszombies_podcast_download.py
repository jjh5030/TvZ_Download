from bs4 import BeautifulSoup
import urllib
import os.path

site_link = "http://www.torresvszombies.com/podcast/audio/"
pageFile = urllib.urlopen("http://www.torresvszombies.com/podcast/audio/")
pageHtml = pageFile.read()
pageFile.close()
 
soup = BeautifulSoup("".join(pageHtml))
sAll = soup.findAll("a")

for link in soup.find_all('a'):
	file_name = link.get('href')
	
	if file_name.endswith('.mp3') and not os.path.isfile(file_name):	
		print "\n\n*** FILE TO DOWNLOAD: ", file_name, "\n"
		
		u = urllib.urlopen(site_link + file_name)
		f = open(file_name, 'wb')
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		print "Downloading: %s Bytes: %s" % (file_name, file_size)
		
		file_size_dl = 0
		block_sz = 8192
		while True:
			buffer = u.read(block_sz)
			if not buffer:
				break

			file_size_dl += len(buffer)
			f.write(buffer)
			status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
			status = status + chr(8)*(len(status)+1)
			print status,

		f.close()