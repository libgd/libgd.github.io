#!/usr/bin/env python

AUTHOR = 'libgd.org'
SITENAME = 'GD Graphics Library'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (
          ('Downloads', 'https://github.com/libgd/libgd/releases'),
          ('Issues', 'https://github.com/libgd/libgd/issues'),
          ('Mailing List', 'https://news-web.php.net/php.gd.devel/'),
#          ('Wiki', 'https://github.com/libgd/libgd/wiki'),
         )

# Social widget
SOCIAL = (#('You can add links in your config file', '#'),
          ('github', 'https://github.com/libgd/libgd'),
          ('gitter', 'https://gitter.im/libgd/libgd'),
         )

PAGE_EXCLUDES = ['manuals']
ARTICLE_EXCLUDES = ['manuals']
STATIC_PATHS = ['manuals']

DEFAULT_PAGINATION = 10

READERS = {'html': None}

THEME = 'libgd'
CSS_FILE = 'libgd.css'
