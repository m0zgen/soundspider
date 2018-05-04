# Soundspider for Russian soundtrack resource "http://всесаундтреки.рф"
This simple python script, which use [Scrapy] library:

How install Scrapy:
```sh
  pip install scrapy
```

You can:
* clone this repo
* change link to soundtrack category
* setup download folder name

All changes must be made in the spider script file (see Usage section bellow)

# Usage
Clone repository and go to spider folder:
```sh
  cd soundspider/soundspider/spiders
```

open file:
```sh
  nano mp3_spider.py
```

Change download catalog folder name (this folder will create automaticly), as example:
```sh
  catalog_name = "God-of-war"
```

Change link to soundtrack category:
```sh
  source_site = "http://xn--80adhccsnv2afbpk.xn--p1ai/saundtrek-k-igre/7141-2018-god-of-war-soundtrack.html"
```

Run spider:
```sh
  scrapy crawl mp3
```

Done! Happy coding!

# Future

Maybe create publication in my [blog]

[Scrapy]: https://scrapy.org/
[blog]: https://sys-adm.in