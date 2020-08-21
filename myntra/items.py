import scrapy


class MyntraItem(scrapy.Item):
    """
    Declare product fields here
    """
    Category_URL = scrapy.Field()
    Product_URL = scrapy.Field()
    Brand = scrapy.Field()
    Product_Name = scrapy.Field()
    Price_Rs = scrapy.Field()
    Rating = scrapy.Field()
    Product_Code = scrapy.Field()
    Seller = scrapy.Field()
