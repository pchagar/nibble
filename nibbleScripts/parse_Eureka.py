from lxml import html
from lxml.etree import tostring
from util import *

import re
import requests

url = "http://www.eurekarestaurantgroup.com/eat/#"
page = requests.get(url)
tree = html.fromstring(page.content)
pageTitle = tree.xpath('//title/text()')
foodHeader = tree.xpath('//section[@class="entry-content"]//span//text()')
#foodDesc = tree.xpath('//table//tr//td//small/text()')
for string in foodHeader:
	if (len(string) < 4):
		foodHeader.remove(string)
	if ('\\xa0' in string):
		string = re.sub('\\xa0', '', string)
print (foodHeader)
# print (etree.tostring(tree, pretty_print=True))


