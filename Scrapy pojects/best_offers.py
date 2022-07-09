import scrapy


class BestOffersSpider(scrapy.Spider):
    name = 'best_offers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for product in response.xpath("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']"):
            product_url=product.xpath(".//div[@class='product-img-outer']/a/@href").get()
            product_img =product.xpath(".//div[@class='product-img-outer']/a/img[@class='lazy d-block w-100 product-img-default']/@data-src").get()
            product_name=product.xpath(".//div[@class='p-title']/a/@title").get()

            yield{
                'product_url': product_url ,
                'product_img': product_img,
                'product_name': product_name
            }

        # = response.xpath("//li[@class='page-item']/a/@href").get()
        #if next_page:
         #   yield scrapy.Request(url=next_page,callback=self.parse)

        next_page = response.xpath(
            "//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)