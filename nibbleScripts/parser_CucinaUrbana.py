from lxml import html
from lxml import etree
from lxml.etree import tostring
from util import *
from selenium import webdriver

import requests

url = "http://www.eurekarestaurantgroup.com/eat/#"
browser = webdriver.PhantomJS()
browser.set_window_size(1024, 768)
browser.get(url)
content = browser.page_source
browser.quit()
tree = html.fromstring(content)
pageTitle = tree.xpath('//title/text()')
foodHeader = tree.xpath('//div//text()')
#foodDesc = tree.xpath('//table//tr//td//small/text()')
# for string in foodHeader:
# 	if (len(string) < 5) & ("$" not in string):
# 		foodHeader.remove(string)
print (foodHeader)
# print (etree.tostring(tree, pretty_print=True))


