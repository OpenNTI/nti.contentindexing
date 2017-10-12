#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from zope import interface

from zope.interface.common.sequence import IMinimalSequence

from nti.schema.field import Object
from nti.schema.field import ValidText
from nti.schema.field import ListOrTuple
from nti.schema.field import DecodingValidTextLine as ValidTextLine


class IMediaTranscriptEntry(interface.Interface):
    """
    Marker interface for video transcript entry
    """
    id = ValidTextLine(title=u'Transcript entry id', required=False)

    transcript = ValidText(title=u'Transcript text')

    end_timestamp = ValidTextLine(title=u'End time stamp')

    start_timestamp = ValidTextLine(title=u'Start time stamp')

    language = ValidTextLine(title=u'Transcript language', required=False,
                             default=u'en')


class IAudioTranscriptEntry(IMediaTranscriptEntry):
    pass


class IVideoTranscriptEntry(IMediaTranscriptEntry):
    pass


class IMediaTranscript(IMinimalSequence):
    """
    Marker interface for media transcript
    """
    entries = ListOrTuple(Object(IMediaTranscriptEntry, title=u'the entry'),
                          title=u'Ordered transcript entries')

    text = interface.Attribute('All entries transcript text')
    text.setTaggedValue('_ext_excluded_out', True)


class IAudioTranscript(IMediaTranscript):
    """
    Marker interface for audio transcript
    """
    entries = ListOrTuple(Object(IAudioTranscriptEntry, title=u'the entry'),
                          title=u'Ordered transcript entries')


class IVideoTranscript(IMediaTranscript):
    """
    Marker interface for video transcript
    """
    entries = ListOrTuple(Object(IVideoTranscriptEntry, title=u'the entry'),
                          title=u'Ordered transcript entries')


class IMediaTranscriptParser(interface.Interface):
    """
    Marker interface for audio transcript parsers
    """

    def parse(source):
        """
        Parse the specified source

        :param source: Media transcript source
        :return a IMediaTranscript object
        """


class IAudioTranscriptParser(IMediaTranscriptParser):
    """
    Marker interface for audio transcript parsers
    """


class IVideoTranscriptParser(IMediaTranscriptParser):
    """
    Marker interface for video transcript parsers
    """
