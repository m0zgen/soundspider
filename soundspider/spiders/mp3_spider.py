#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import urllib
import os.path
import scrapy

# Catalog name
catalog_name = "Dirt4"
""" http://mp3.всесаундтреки.рф/ """
source_site = "http://xn--80adhccsnv2afbpk.xn--p1ai/saundtrek-k-igre/6759-2017-dirt-4.html"

# Save to download folder
global ITEMS_DIR
ITEMS_DIR = os.path.dirname(os.path.realpath(
    __file__)) + "/downloads/" + catalog_name
DWN_DOMAIN = ""

# Check exist download folder
if not os.path.exists(ITEMS_DIR):
    # If not exist - create
    os.makedirs(ITEMS_DIR)


# Show download progress percent
def report(count, blockSize, totalSize):
    percent = int(count * blockSize * 100 / totalSize)
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
            global DWN_DOMAIN
            DWN_DOMAIN = response.css(
                "table.tracklist tr td.row-play a::attr(href)").extract_first()
            DWN_DOMAIN = DWN_DOMAIN.split('/', 3)

            yield response.follow(href, self.get_download_link)

    # Get to download page and get link to file download
    def get_download_link(self, response):
        download_url = response.css(
            "table.FullStoryInfoTable a.FullStoryKnopkaNew2download::attr(href)").extract()
        artist = response.css(
            "table.FullStoryInfoTable td.namesongNew::text").extract_first()
        album = response.css(
            "table.FullStoryInfoTable td.nameartistNew::text").extract_first()
        domain = source_site.split('/', 3)
        full_download_link = domain[0] + "//" + DWN_DOMAIN[2] + download_url[0]
        save_file = os.path.join(ITEMS_DIR, album + " - " + artist + ".mp3")

        # Download mp3 from site with percent progress
        urllib.urlretrieve(full_download_link, save_file, reporthook=report)
