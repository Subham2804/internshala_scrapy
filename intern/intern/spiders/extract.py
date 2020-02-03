import scrapy
from ..items import InternItem


class extract_data(scrapy.Spider):
    name='extractor'
    start_urls=[
        "https://internshala.com/internships/computer%20science-internship"
    ]

    def parse(self,response):
        details=InternItem()
        intern_type=response.css('internship_list_container h4:nth-child(1) a::text').extract()
        intern_company = response.css('.link_display_like_text::text').extract()
        intern_stipend = response.css('.stipend_container_table_cell::text').extract()
        intern_duration = response.css('td:nth-child(2)::text').extract()
        details['intern_type']=intern_type
        details['intern_company'] = intern_company
        details['intern_stipend'] = intern_stipend
        details['intern_duration'] = intern_duration

        yield details
