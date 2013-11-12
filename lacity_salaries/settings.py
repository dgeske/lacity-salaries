# Scrapy settings for lacity_salaries project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lacity_salaries'

SPIDER_MODULES = ['lacity_salaries.spiders']
NEWSPIDER_MODULE = 'lacity_salaries.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lacity_salaries (+http://www.yourdomain.com)'

# Crawl responsibly by adding some delay
DOWNLOAD_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = True
