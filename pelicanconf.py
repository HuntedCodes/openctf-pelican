#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vand & DC562'
SITENAME = 'OpenCTF @ DefCon 26'
#SITEURL = 'https://scoreboard.openctf.com'

#THEME = "themes/pelican-cait"
#THEME = "themes/pelican-blueidea"
#THEME = "themes/pelican-octopress-theme"

PATH = 'content'
SITEURL = '/posts'
OUTPUT_PATH = 'output/posts'
SLUGIFY_SOURCE = 'basename'
PAGE_URL = '../{slug}/'
PAGE_SAVE_AS = '../{slug}/index.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ('Home', '/'),
    ('Getting Started', '/getting-started/'),
    ('Status Updates', '/status/'),
    ('Fixes & Errata', '/fixes/'),
    ('Services', '/services/'),
    ('FAQ', '/faq/'),
]
LINKS = (
    ('V& (Vand)', 'https://openctf.com'),
    ('DC 562', 'https://dc562.org/'),
    ('OpenCTF Scoreboard', 'https://scoreboard.openctf.com/'),
)
STATIC_PATHS = [ 'static' ]
EXTRA_PATH_METADATA = {
    'static/vand.png': {'path': '../static/vand.png'},
    'static/dc562.png': {'path': '../static/dc562.png'},
}

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
