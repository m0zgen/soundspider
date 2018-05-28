### Media downloader for [ВСЕСАУНДТРЕКИ.РФ](http://всесаундтреки.рф)

#### Synopsis

This crawler is built on top of [Scrapy](https://scrapy.org). My main goal was to implement simple wrapper to allow myself get some OST music with ease.


### Prerequisites

* Get all dependencies:
```bash
pip install scrapy
```


### Installation

To get this piece of software and fire it up you should do the following steps:

1. Clone this repo:
```bash
git clone https://github.com/m0zgen/soundspider.git
```

2. Open configuration file:
```bash
cd soundspider/soundspider/spiders/
vim mp3_spider.py
```
3. Configure `soundspider`:

Define download folder (don't worry, it'll be created automatically):
```bash
...
catalog_name = "God-of-war"
...
```

Define OST link to download from:
```bash
...
source_site = "http://xn--80adhccsnv2afbpk.xn--p1ai/saundtrek-k-igre/7141-2018-god-of-war-soundtrack.html"
...
```

### Troubleshooting

If you sow message after start crawl, such as:
```bash
...
 File "/usr/lib/python2.7/site-packages/pyasn1_modules/rfc2459.py", line 1014, in AttributeTypeAndValue
    openType=opentype.OpenType('type', certificateAttributesMap))
TypeError: __init__() got an unexpected keyword argument 'openType'
...
```

Please run this command:
```bash
pip install "pyasn1-modules<=0.2.0"
```

### Usage

After all needed changes are made to `mp3_spider.py` run the spider itself:
```bash
scrapy crawl mp3
```

Done! Happy downloading!

### Contacts

Feel free to check my [site](https://sys-adm.in).
