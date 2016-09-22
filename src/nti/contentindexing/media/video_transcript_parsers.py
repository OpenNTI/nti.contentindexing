#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
video transcript parsers.

.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.contentindexing.media import VideoTranscript
from nti.contentindexing.media import VideoTranscriptEntry

from nti.contentindexing.media.interfaces import IVideoTranscriptParser

from nti.contentindexing.media.media_transcript_parsers import _SRTTranscriptParser
from nti.contentindexing.media.media_transcript_parsers import _SBVTranscriptParser
from nti.contentindexing.media.media_transcript_parsers import _WebVttTranscriptParser

@interface.implementer(IVideoTranscriptParser)
class _SRTTranscriptParser(_SRTTranscriptParser):
	entry_cls = VideoTranscriptEntry
	transcript_cls = VideoTranscript

@interface.implementer(IVideoTranscriptParser)
class _SBVTranscriptParser(_SBVTranscriptParser):
	entry_cls = VideoTranscriptEntry
	transcript_cls = VideoTranscript

@interface.implementer(IVideoTranscriptParser)
class _WebVttTranscriptParser(_WebVttTranscriptParser):
	entry_cls = VideoTranscriptEntry
	transcript_cls = VideoTranscript
