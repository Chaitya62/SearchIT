import app.spider.Spider
from nltk.tokenize import  word_tokenize
from bs4 import BeautifulSoup
from collections import Counter
import re

class ExtractData(BeautifulSoup):
	def  __init__(self, response):
		super().__init__(response, "lxml")
		self.response = response
		self.get_text()

	def get_text(self):
		self.data = [word for text in self.strings for word in word_tokenize(text)]
		self.frequency_data = Counter()
		for word in self.data:
			self.frequency_data[word]+=1
		print(self.frequency_data)


if __name__ == '__main__':
	spider = Spider('https://stackoverflow.com/')
	data = ExtractData(spider.response)
