#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import urllib
import os.path
import scrapy

# --------------------------------------------------------------------------------------------------------------------------
# Catalog name
catalog_name = "Taxi5"

""" http://mp3.всесаундтреки.рф/ """
source_site = "http://xn--80adhccsnv2afbpk.xn--p1ai/saundtrek-k-filmu/7123-2018-taksi-5-soundtrack.html"

# --------------------------------------------------------------------------------------------------------------------------
# Save to download folder
global ITEMS_DIR
ITEMS_DIR = os.path.dirname(os.path.realpath(__file__)) + "/downloads/" + catalog_name

# Check exist download folder
if not os.path.exists(ITEMS_DIR):
  # If not exist - create
  os.makedirs(ITEMS_DIR)

def report(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r%d%%" % percent + ' complete')
    sys.stdout.flush()

class Mp3Spider(scrapy.Spider):
    name = "mp3"
    start_urls = [
        source_site,
    ]


    def parse(self, response):
        # Get links to download page
        for href in response.css("table.tracklist tr td.row-play a::attr(href)"):
            yield response.follow(href, self.get_download_link)

    # Get to download page and get link to file download
    def get_download_link(self, response):
        download_url = response.css("table.FullStoryInfoTable a.FullStoryKnopkaNew2download::attr(href)").extract()
        artist = response.css("table.FullStoryInfoTable td.namesongNew::text").extract_first()
        album = response.css("table.FullStoryInfoTable td.nameartistNew::text").extract_first()

        domain = source_site.split('/', 3)
        full_download_link = domain[0] + "//mp3m." + domain[1] + domain[2] + download_url[0]

        save_file = os.path.join(ITEMS_DIR, album + " - " + artist + ".mp3")

        print(save_file)
        urllib.urlretrieve(full_download_link, save_file, reporthook=report)
