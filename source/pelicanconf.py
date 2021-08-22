#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Roll Cooksville'
SITENAME = ''
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SHOW_ARTICLE_AUTHOR = False

# Blogroll
LINKS = (('Mississauga Bikes', 'https://www.mississaugabikes.ca/'),
         ('2018 Mississauga Bike Map', 'https://www.mississaugabikes.ca/wp-content/uploads/2018/07/Mississauga-Cycling-Map-2018-web-with-panels.pdf'),
         ('Walk and Roll Peel', 'http://walkandrollpeel.ca/'),
         ('Peel Trails Map', 'http://walkandrollpeel.ca/map/themap.asp'),)

# Social widget
SOCIAL = (('Instagram',"https://www.instagram.com/rollcooksville/"),
          ('Twitter', 'https://twitter.com/RollCooksville'),
          ("Facebook Page", "https://facebook.com/RollCooksville/","Facebook"),
          ("Facebook Group", "https://facebook.com/groups/rollcooksville/","Facebook"),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
OUTPUT_PATH = '../output'
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
THEME = 'theme'
PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites', 'pelican_youtube',]
BOOTSTRAP_THEME = 'flatly'

STATIC_PATHS = ['images','maps']
SITELOGO = 'images/ROLL_COOKSVILLE_white.svg'
SITELOGO_SIZE = 160

READERS = {'html': None}
