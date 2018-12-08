import scrapy

"""
scrapy startproject tutorial
scrapy crawl demo [-o demo.json]
"""


def parse(response):
    response.url
    response.body
    response.css('title')
    response.css('title::text').extract()
    response.css('title::text')[0].extract()
    response.css('title::text').extract_first()
    response.css('title::text').re(r'Q\w+')

    response.xpath('//title')
    response.xpath('//title/text()').extract_first()

    yield {
        'text': response.css('span.text::text').extract_first(),
        'author': response.css('small.author::text').extract_first(),
        'tags': response.css('div.tags a.tag::text').extract(),
    }

    for a in response.css('li.next a'):
        yield response.follow(a, callback=self.parse)
