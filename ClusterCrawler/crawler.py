import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
import re
from tldextract import extract


# add linkextractor rules just to scrape contact, about, support, connect
# figure out how you want to store data (response.url gives specific url where e mail or number found)
# add social media rule and parser, remember it can be a "share" link to social media not profile
# add headers for user profiles
# add proxy support
# implement scrapy items into parse_item
# set custom_settings for "broad crawls"/commercial/large scrapes
# implement server sending 10-50? urls at a time per pi and send large data chunk back
# make sure all crawled data is unique then also make sure it doesn't already exist in database
# dont mark website in database as done until the message is received back with data
# does scrapy auto load webpages in english?

# email scraped data: host, domain, url, email
# phone scraped data: host, domain, url, phone
# social media scraped data: host, domain, url, platform(social media), link


class Crawler(CrawlSpider):
    name = "crawler"
    start_urls = []
    rules = [
        Rule(LinkExtractor(allow=[re.compile(r"contact|about|connect|support", re.IGNORECASE)]), callback='parse_item',
             follow='true')
    ]
    custom_settings = {
        'LOG_ENABLED': True
    }

    email_regex = re.compile(r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
    \x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[
    a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[
    0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[
    \x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""", re.IGNORECASE)

    old_email_regex = re.compile(r"""[a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[
    a-z0-9-]*[a-z0-9])""", re.IGNORECASE)

    phone_regex = r"""(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"""

    old_phone_regex = r"""(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[
    02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([
    0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?"""

    IGNORED_EXTENSIONS = (
        # images
        'mng', 'pct', 'bmp', 'gif', 'jpg', 'jpeg', 'png', 'pst', 'psp', 'tif',
        'tiff', 'drw', 'dxf', 'eps', 'ps', 'svg',

        # audio
        'mp3', 'wma', 'ogg', 'wav', 'ra', 'aac', 'mid', 'au', 'aiff',

        # video
        '3gp', 'asf', 'asx', 'avi', 'mov', 'mp4', 'mpg', 'qt', 'rm', 'swf', 'wmv',
        'm4a',

        # office suites
        'xls', 'xlsx', 'ppt', 'pptx', 'pps', 'doc', 'docx', 'odt', 'ods', 'odg',
        'odp',

        # other
        'css', 'pdf', 'exe', 'bin', 'rss', 'zip', 'rar',
    )

    def __init__(self, host=None, urls=None, *args, **kwargs):
        self.host = host
        self.urls = urls
        self.headers = []
        self.all_data = {"emails": set(), "phones": set()}

        super(Crawler, self).__init__(*args, **kwargs)
        self.start_urls = self.urls


    def parse_start_url(self, response, **kwargs):
        return self.parse_item(response)


    def parse_item(self, response):
        print("hello")
        emails = self.extract_emails(response.text)
        phones = self.extract_phones(response.text)


    def extract_emails(self, page_text):
        matches = re.finditer(self.email_regex, page_text)
        if matches:
            for match in matches:
                email_address = match.group()
                if not email_address.endswith(self.IGNORED_EXTENSIONS):
                    self.all_data["emails"].add(email_address)
        else:
            return None

        return print(f'email addresses: {self.all_data["emails"]}')

    def extract_phones(self, page_text):
        matches = re.finditer(self.phone_regex, page_text)
        if matches:
            for match in matches:
                phone_number = match.group()
                if len(phone_number) > 7:
                    self.all_data["phones"].add(phone_number)
        else:
            return None

        return print(f'phone numbers: {self.all_data["phones"]}')


    def extract_next_page(self):
        pass
        # next_page == None if not next page
        # return next_page

    def append_page_data_to_all_data(self, emails, phones):
        page_data = {"host": self.host, "url": self.url, "emails": emails, "phones": phones}
        self.all_data.append(page_data)

    def get_all_data(self):
        pass
        # a list of page_data dictionaries
        # return self.all_data


def main():
    host1 = "shopify"
    url1 = "https://shop.mocp.org/"

    host2 = "personal"
    url2 = "https://josefkjaergaard.com/"

    url3 = "https://www.jayforeman.co.uk/"

    url4 = "https://teskeys.com/"

    process = CrawlerProcess()
    process.crawl(Crawler, host=host2, urls=[url3])
    process.start()

if __name__ == '__main__':
    main()