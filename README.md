# myntra
This is a Scrapy project to scrape product details from https://www.myntra.com/ppe-suit (Mynta category pages).

# Extracted data
This project extracts sample product details from specific individual products.

```
{
    'Brand': 'SWAYAM',
    'Category_URL': 'https://www.myntra.com/ppe-suit',
    'Price_Rs': 999,...
}
```

# Running the spiders
You can run a spider using the scrapy crawl command, such as:

`scrapy crawl myntra`

If you want to save the scraped data to a CSV file, you can pass the -o option:

`scrapy crawl mynta -o output.csv`
