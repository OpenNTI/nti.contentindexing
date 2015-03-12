#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from .. import title, title_, TITLE
from .. import quick, quick_, QUICK
from .. import content, content_, CONTENT

book_prefix = BOOK_IDXNAME_PREFIX = u''
nticard_prefix = NTICARD_IDXNAME_PREDIX = u'nticard_'
atrans_prefix = AUDIO_TRANSCRIPT_IDXNAME_PREDIX = u'atrans_'
vtrans_prefix = VIDEO_TRANSCRIPT_IDXNAME_PREDIX = u'vtrans_'
