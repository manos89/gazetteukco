import scrapy


class GazSpider(scrapy.Spider):
    name="gazz"



    def start_requests(self):
        url="https://www.thegazette.co.uk/insolvency/notice?categorycode=-1+G406030016&location-distance-1=1&service=insolvency&numberOfLocationSearches=1&results-page-size=100&results-page="
        for i in range(1,2):
            full_url=url+str(i)
            request=scrapy.Request(url=full_url,callback=self.parse_links,dont_filter=True)
            yield request



    def parse_links(self,response):
        link_content=response.selector.css('div.notice-feed')
        print(len(link_content))