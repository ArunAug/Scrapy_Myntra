import re
import json

from scrapy import Request
from scrapy.spiders import Spider

from urllib.parse import urljoin

from myntra.items import MyntraItem


class MyntraSpider(Spider):
    name = "myntra"
    allowed_domains = ["myntra.com"]
    start_urls = ['https://www.myntra.com/surgical-masks',
                  'https://www.myntra.com/masks-store',
                  'https://www.myntra.com/ppe-suit']

    def parse(self, response, **kwargs):
        """
        Scraping all the product details from listing page itself
        :param response:
        :return:
        """
        text = response.text
        total_products = re.search('= {"searchData":(.+?),"seo":', text)
        if not total_products:
            raise Exception("Unable to find product details")
        total_products_ = total_products.group(1) + "}"
        result_dict = json.loads(total_products_)
        products = result_dict["results"]["products"]
        for product in products:
            item = MyntraItem()
            url = urljoin(response.url, product["landingPageUrl"])
            item["Category_URL"] = response.url
            item["Product_URL"] = url
            item["Brand"] = product["brand"]
            item["Product_Name"] = product["productName"]
            item["Price_Rs"] = product["price"]
            item["Rating"] = product["rating"]
            item["Product_Code"] = product["productId"]
            yield Request(url, meta={"item": item}, callback=self.parse_details)

        # implemented pagination here.
        total_items = result_dict["results"]["totalCount"]
        if "?p=" in response.url:
            main_url = response.url.split("?")[0]
        else:
            main_url = response.url
        if total_items > 50:
            total_pages = round(total_items/50)
            for i in range(2, total_pages+1):
                next_page_url = main_url+"?p={}".format(i)
                yield Request(next_page_url, callback=self.parse)

    def parse_details(self, response):
        """
        Fetching product seller information here
        :param response:
        :return:
        """
        item = response.meta["item"]
        text = response.text
        product_details = re.search('= {"pdpData":(.+?),"pageName":', text)
        if product_details:
            product_details_ = product_details.group(1)
            result_dict = json.loads(product_details_)
            item["Seller"] = result_dict["sellers"][0]['sellerName']
            yield item
