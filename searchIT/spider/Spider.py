import re
from urllib import request
from urllib.request import Request
from multiprocessing.dummy import Pool as ThreadPool

from searchIT.utils.utils import is_url,make_url

class Spider:

    def __init__(self,url, verbose=False):
        self.url = url
        self.domain = ''
        self.response = ''
        self.verbose = verbose
        self.get_domain()
        self.USER_AGENT = '''Mozilla/5.0 
                             (Macintosh; Intel Mac OS X 10_9_3) 
                             AppleWebKit/537.75.14 (KHTML, like Gecko) 
                             Version/7.0.3 Safari/7046A194A'''
        if(self.verbose):
            print("Visiting domain : " + self.domain)
        self.urls = []
        self.visit()
    
    def get_domain(self):

        pattern = r'(http[s]?://[a-zA-Z0-9]+?\.?[a-zA-Z0-9\-]+\.[a-z]{2,})'
        result = re.findall(pattern, self.url)

        if(result):
            self.domain = result[0]

    def visit(self):
            
            if(self.verbose):
                print("Visiting {}".format(self.url))
            
            try:
                request_obj = Request(self.url)
                request_obj.add_header('User-Agent',self.USER_AGENT)
                request_obj.add_header('Content-Type', 'text/html')
                response_obj = request.urlopen(request_obj)
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
