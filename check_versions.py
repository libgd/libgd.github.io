#!/usr/bin/env python

"""Make sure the installed versions all match what we need."""

import os
import pkg_resources

MARKER = '# TRAVIS-END'
requirements_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 'requirements.txt')

#requirements.txt
with open(requirements_file) as f:
    lines = f.read().splitlines()
    lines = lines[lines.index(MARKER):]
    pkg_resources.require(lines)
