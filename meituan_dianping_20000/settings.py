# -*- coding: utf-8 -*-

# Scrapy settings for meituan_dianping_20000 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meituan_dianping_20000'

SPIDER_MODULES = ['meituan_dianping_20000.spiders']
NEWSPIDER_MODULE = 'meituan_dianping_20000.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'meituan_dianping_20000 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'meituan_dianping_20000.middlewares.MeituanDianping20000SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'meituan_dianping_20000.middlewares.MeituanDianping20000DownloaderMiddleware': 543,
    'meituan_dianping_20000.middlewares.UserAgentMiddleware': 544,
    # 'meituan_dianping_20000.middlewares.ProxyMiddleware': 545
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'meituan_dianping_20000.pipelines.MeituanDianping20000Pipeline': 300,
   'meituan_dianping_20000.pipelines.DianpingDetailPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 猿人云ip
APP_ID = 'A1909190000320165201'
SECRECT = 'vWwUoZa9Yotef33S'
YR_YUN_PROXY_URI = f'http://{APP_ID}:{SECRECT}@forward.apeyun.com:9082'

# 阿布云
ABU_YUN_PROXY_URI1 = 'http://H034E435SK942AAD:F21A9EC8AA72399E@http-dyn.abuyun.com:9020'
ABU_YUN_PROXY_URI2 = 'http://HB1160148BKW114D:3E4EDF8EA45E8AB6@http-dyn.abuyun.com:9020'
ABU_YUN_PROXY_URI3 = 'http://H1TL903Z5642CO9D:E10DEDE27413A1D0@http-dyn.abuyun.com:9020'
ABU_YUN_PROXY_URI4 = 'http://HQTW638UUSVB67GD:A8948ABAAB85043A@http-dyn.abuyun.com:9020'
ABU_YUN_PROXY_URI5 = 'http://HKIG3MQ94LC29Q7D:B2719E36CAF40759@http-dyn.abuyun.com:9020'

# 限速
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS =1

# 禁止cookie防跟踪
COOKIES_ENABLED = False


# 请求头 dianping_list
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Host': 'www.dianping.com',
#     'Pragma': 'no-cache',
#     'Referer': 'http://www.dianping.com/beijing/',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1'
# }

# 请求头 dianping_detail
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'www.dianping.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
}
