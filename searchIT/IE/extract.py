import re
from collections import Counter


from nltk.tokenize import  word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import  word_tokenize
from bs4 import BeautifulSoup

from  searchIT.spider.Spider import Spider


#move to different file later on
symbols_and_stops_words = [
    "=", "?", ".", "/", "}",
    "{", "]", "[", "\\n", "\\t",
    "\\n\\n\\n", "''", "\\n\\n",
    "``", "+=", "~", "`", "'" ,
    "\"" , "\\", ")", "(", "&", 
    "^", "%", "$", "#", "@", "!", 
    "-", "_", "<", ">", ",", "|", 
    ":", ";",
    ] 

class ExtractData(BeautifulSoup):

    #static variable
    stop_words = set(stopwords.words("english"))



    def  __init__(self, response, verbose=False):

        self.verbose = verbose

        for i in symbols_and_stops_words:
                ExtractData.stop_words.add(i)

        super().__init__(response, "lxml")
        self.response = response

        self.remove_tag("script");
        self.remove_tag("style");
        self.remove_tag("meta");
        self.remove_tag("head");
        
        self.get_text()     
    
    def remove_tag(self, tag_name):

        for _tag in self.findAll(tag_name):
                _tag.decompose()


    def get_text(self):

        self.data = [ 
                word 
                for text in self.strings 
                for word in word_tokenize(text)
                ]
        
        self.frequency_data = Counter()

        for word in self.data:

            word = word.lower()
            if word in ExtractData.stop_words: 
                continue
            if re.match(r'(\\n)+', word): 
                continue
            if re.match(r'(\\x[a-z0-9]{2,})+', word): 
                continue    
            self.frequency_data[word]+=1

        print(self.frequency_data.most_common(60))


def main():

    url = input("Enter website url : ")
    spider = Spider(url)
    data = ExtractData(spider.response)


if __name__ == '__main__':

    url = input("Enter website url : ")
    spider = Spider(url)
    data = ExtractData(spider.response)
    
