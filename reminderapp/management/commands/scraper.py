from bs4 import BeautifulSoup
import urllib2
from urllib2 import HTTPError, URLError

f = open('bizurls.tsv', 'r')
i = 0

ValueErrorCount = 0
HttpErrorCount = 0
UrlErrorCount = 0
UnknownErrorCount = 0

for line in f:
	i += 1
	
	if i == 10:
		break
		
	split_line = line.split()
	biz_url = split_line[0]
	biz_id = split_line[2]
	print split_line
	print 'biz_url = ' + str(biz_url) + ', biz_id = ' + str(biz_id)

	try:
		url = urllib2.urlopen(biz_url)
		soup = BeautifulSoup(url.read())
		print soup.title
		filename = str(biz_id) + '.html'
		f = open(filename, 'w')
		f.write(soup)
		f.close()
	except ValueError:
		print 'ERROR'
		ValueErrorCount += 1
	except urllib2.HTTPError, e:
		print 'HTTPERROR' + str(e.code)
		HttpErrorCount += 1
	except URLError:
		print 'URLError'
		UrlErrorCount += 1
	except:
		UnknownErrorCount +=1
	
	
	print '\n'

print 'ValueErrorCount = ' + str(ValueErrorCount)
print 'HttpErrorCount = ' + str(HttpErrorCount)
print 'UrlErrorCount = ' + str(UrlErrorCount)
 


# try:
#     urllib2.urlopen(url)
# except urllib2.HTTPError, e:
#     print e.code
# except urllib2.URLError, e:
#     print e.args







# url_to_scrape = ["http://www.trickdogbar.com/"]


# url = urllib2.urlopen("http://www.trickdogbar.com/")
# soup = BeautifulSoup(url.read())

# print soup


# f = open('biz_html.html', "w")

# url_to_scrape = ["http://www.trickdogbar.com/"]
# url = urllib2.urlopen(url_to_scrape)
# soup = BeautifulSoup(url.read())
# f.write(soup)
# f.close()

# soup = {}

# for item in url_to_scrape:
# 	url = urllib2.urlopen(item)
# 	soup[item] = BeautifulSoup(url.read())

# for key in soup:
# 	print key
# 	print soup[item]
# 	print '\n'




# links = soup.find_all('a')

# print links

# attributes = {}

# for link in links:
# 	attributes.append(link.attrs)

# print type(attributes)

# for key in attributes
# 	print key, attributes[key]

# def mailto_link(e):
#     '''Return the email address if the element is is a mailto link,
#     otherwise return None'''
#     if e.name != 'a':
#         return None
#     for key, value in e.attrs:
#         if key == 'href':
#             m = re.search('mailto:(.*)',value)
#             if m:
#                 return m.group(1)
#     return None


