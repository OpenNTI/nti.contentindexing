#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id: video_transcript_parsers.py 38907 2014-05-13 16:48:46Z carlos.sanchez $
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.contentindexing.media import AudioTranscript
from nti.contentindexing.media import AudioTranscriptEntry

from nti.contentindexing.media.interfaces import IAudioTranscriptParser

from nti.contentindexing.media.media_transcript_parsers import SBVTranscriptParser
from nti.contentindexing.media.media_transcript_parsers import SRTTranscriptParser
from nti.contentindexing.media.media_transcript_parsers import WebVttTranscriptParser


@interface.implementer(IAudioTranscriptParser)
class _SRTTranscriptParser(SRTTranscriptParser):
    entry_cls = AudioTranscriptEntry
    transcript_cls = AudioTranscript


@interface.implementer(IAudioTranscriptParser)
class _SBVTranscriptParser(SBVTranscriptParser):
    entry_cls = AudioTranscriptEntry
    transcript_cls = AudioTranscript


@interface.implementer(IAudioTranscriptParser)
class _WebVttTranscriptParser(WebVttTranscriptParser):
    entry_cls = AudioTranscriptEntry
    transcript_cls = AudioTranscript
