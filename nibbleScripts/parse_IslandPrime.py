from lxml import html
from lxml.etree import tostring
from util import *
import requests

# url = "https://www.cohnrestaurants.com/islandprime/menu"
# with urllib.request.urlopen(url) as page:
# 	soup = BeautifulSoup(open(page))
# 	print(soup.prettify())
page = requests.get("https://www.cohnrestaurants.com/islandprime/menu")
tree = html.fromstring(page.content)
pageTitle = tree.xpath('//title/text()')
foodHeader = tree.xpath('//table//tr//td//text()')
#foodDesc = tree.xpath('//table//tr//td//small/text()')
for string in foodHeader:
	if (len(string) < 5) & ("$" not in string):
		foodHeader.remove(string)
newL = []
fout = open('output.txt', 'w')
for i in range(2,len(foodHeader)):
	if (foodHeader[i].find("$") == -1):
		continue
	if (foodHeader[i-1].find("$") != -1):
		continue
	if (foodHeader[i-2].find("$") != -1):
		continue
	newL.append(dish(foodHeader[i-2],foodHeader[i-1],parseInt(foodHeader[i])))
for food in newL:
	fout.write(food.getName())
	fout.write("\n")
	fout.write(food.getDesc())
	fout.write("\n")
	fout.write(food.getPrice())
	fout.write("\n")




