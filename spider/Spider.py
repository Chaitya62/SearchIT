import re
from urllib import request
from utils.utils import is_url,make_url
from multiprocessing.dummy import Pool as ThreadPool


class Spider:
	def __init__(self,url):
		self.url = url
		self.domain = ''
		self.response = ''
		self.get_domain()
		print("Visiting domain : " + self.domain)
		self.urls = []
		self.visit()
	
	def get_domain(self):
		pattern = r'(http[s]?://[a-zA-Z0-9]+\.[a-zA-Z0-9\-]+\.[a-z]{2,})'
		result = re.findall(pattern, self.url)
		if(result):
			self.domain = result[0]

	def visit(self):
			print("Visiting {}".format(self.url))
			try:
				response_obj = request.urlopen(self.url)
				self.response = str(response_obj.read());
				self.find_urls(str(self.response))
			except Exception as e: 
				print(e)
		
			#print(self.urls)
	
	def find_urls(self, response):
		url_find_pattern = r'<a href="?\'?([^"\'>]*)'
		results = re.findall(url_find_pattern, response)
		if(results):
			for url in results:
				if is_url(url):
					self.urls.append(url)
				else: 
					self.urls.append(make_url(self.domain, url))
	
urls= []

def test(url):
	print("URLS : ",len(urls))
	ax = Spider(url)
	urls.extend(ax.urls)
	return url
		

if __name__ == '__main__':
	content = ""
	url = input('Enter the url : ')
	#url = "http://chaitya62.github.io"
	urls.append(url)
	spider = Spider(url)
	print("Will visit :"+str(len(spider.urls))+" urls")
	pool = ThreadPool(10)
	results = pool.map(test, spider.urls)
	"""for i in spider.urls:
		print("URLS : ", len(urls))
		ax = Spider(i)
		urls.extend(ax.urls)
	print(len(urls))"""
	#spider.find_urls(content)
	#print(content)
