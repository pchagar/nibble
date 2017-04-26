class dish(object):
	def __init__(self, name, desc, price):
		self.__name = name
		self.__desc = desc
		self.__price = price
	def getName(self):
		return self.__name
	def getDesc(self):
		return self.__desc
	def getPrice(self):
		return self.__price

def parseInt(sin):
	import re
	return re.findall(r"[-+]?\d*\.\d+|\d+", sin)[0]