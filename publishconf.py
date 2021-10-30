#!/usr/bin/env python

"""
This file is only used if you use `make publish` or explicitly specify it as
your config file.
"""

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://libgd.github.io'
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
