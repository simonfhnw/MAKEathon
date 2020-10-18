# import requests
# import re
import scrapy
from scrapy.crawler import CrawlerProcess


# def crawlWebsite():
#     page = requests.get("https://www.zdnet.com").text
#     print(re.findall("breach", page))
#     print(page.find("breach"))
# 'https://www.zdnet.com',


class HeaderSpider(scrapy.Spider):
    name = "header"


    def start_requests(self):
        urls = [
            'https://www.zdnet.com/article/three-npm-packages-found-opening-shells-on-linux-windows-systems/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        body = response.css('storyBody').getall()
        # body = response.selector.xpath('//storyBody').get().encode()
        # print(response.css('//storyBody').get())
        print(type(body))
        filename = f'Body.html'
        with open(filename, 'wb') as f:
            # f.write(response.html("body"))
            f.write(" ".join(body).encode())
        self.log(f'Saved file {filename}')



process = CrawlerProcess()
process.crawl(HeaderSpider)
process.start()
