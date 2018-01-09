import os
from os import listdir
from os.path import isfile, join
from pprint import pprint

from searchIT.spider.Spider import Spider
from searchIT.IE.extract import ExtractData



class CollectData:

	def __init__(self, base_dir):
		self.BASE_DIR = base_dir
		self.files = []
		self.contents = {}


	def get_files(self):
		self.files = []
		for file in listdir(self.BASE_DIR):
			if(isfile(join(self.BASE_DIR, file))):
				self.files.append(file)
		
	def show_files(self):
		print(self.files)

	def show_content_of(self,fileindex):

		with open(join(self.BASE_DIR, self.files[fileindex]), 'r') as file:
			for line in file:
				print(line)

	def show_all(self):

		for i,file in enumerate(self.files):
			print("\n***********************************************\n")
			print("{} contains : \n".format(file))
			self.show_content_of(i)
			print("\n**********************************************\n")

	def get_content_of(self, fileindex):
		content = []
		
		with open(join(self.BASE_DIR, self.files[fileindex]), 'r') as file:
			for line in file:
				content.append(self.remove_end_line(line))

		return content

	def get_all(self):

		for i, file in enumerate(self.files):
			self.contents[file] = self.get_content_of(i)

		return self.contents;

	def remove_end_line(self, url):
		return url[:-1]

	def collect(self):
		for file in self.contents:
			print("\n***********************************************\n")
			print("\n collecting data from {} \n".format(file))
			urls = self.contents[file]
			for url in urls:
				print("\nworking on {} \n".format(url))
				self.get_page_data(url)


	def get_page_data(self, url):


		spider = Spider(url)
		data = ExtractData(spider.response)




def main():
	cd = CollectData('./searchIT/IE/urls/')
	cd.get_files()
	cd.show_all()
	pprint(cd.get_all())
	
	cd.collect()
