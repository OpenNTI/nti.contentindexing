#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.contentindexing.media import VideoTranscript
from nti.contentindexing.media import VideoTranscriptEntry

from nti.contentindexing.media.interfaces import IVideoTranscriptParser

from nti.contentindexing.media.media_transcript_parsers import SRTTranscriptParser
from nti.contentindexing.media.media_transcript_parsers import SBVTranscriptParser
from nti.contentindexing.media.media_transcript_parsers import WebVttTranscriptParser

@interface.implementer(IVideoTranscriptParser)
class _SRTTranscriptParser(SRTTranscriptParser):
	entry_cls = VideoTranscriptEntry
	transcript_cls = VideoTranscript

@interface.implementer(IVideoTranscriptParser)
class _SBVTranscriptParser(SBVTranscriptParser):
	entry_cls = VideoTranscriptEntry
	transcript_cls = VideoTranscript

@interface.implementer(IVideoTranscriptParser)
class _WebVttTranscriptParser(WebVttTranscriptParser):
	entry_cls = VideoTranscriptEntry
	transcript_cls = VideoTranscript
