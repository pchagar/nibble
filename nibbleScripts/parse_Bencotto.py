from lxml import html
from lxml.etree import tostring
from util import *
import requests

url = "https://www.lovebencotto.com/lunch-and-dinner-menu/"
page = requests.get(url)
tree = html.fromstring(page.content)
pageTitle = tree.xpath('//title/text()')
foodHeader = tree.xpath('//div//strong')
#foodDesc = tree.xpath('//table//tr//td//small/text()')
for string in foodHeader:
	if (string.text):
		print(string.text)
	if (string.tail):
		print(string.tail)