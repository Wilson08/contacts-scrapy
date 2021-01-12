# contacts-scrapy
This is a Scrapy project to scrape phone and logo from any WEB site.

#  Requirements
- Python => 3.6
- Scrapy

## Extracted data

This project extracts quotes, combined with the respective author names and tags.
The extracted data looks like this sample:


    {
      "logo": "https://www.illion.com.au/wp-content/uploads/2019/03/ION-RGB-Gradient-64.png", 
      "phones": ["+61871229452", "+64800836268", "+61398283200"],
      "website": "https://www.illion.com.au/contact-us/"
    }
    
## Spiders
This project contains only the **`contacts`** spider.
    
## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl contacts

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl contacts -o contacts.json
