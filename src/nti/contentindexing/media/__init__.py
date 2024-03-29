#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=no-member
        
from zope import interface

from nti.contentindexing.media.interfaces import IAudioTranscript
from nti.contentindexing.media.interfaces import IMediaTranscript
from nti.contentindexing.media.interfaces import IVideoTranscript
from nti.contentindexing.media.interfaces import IAudioTranscriptEntry
from nti.contentindexing.media.interfaces import IMediaTranscriptEntry
from nti.contentindexing.media.interfaces import IVideoTranscriptEntry

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.schema import SchemaConfigured

logger = __import__('logging').getLogger(__name__)


@interface.implementer(IMediaTranscriptEntry)
class MediaTranscriptEntry(SchemaConfigured):
    createDirectFieldProperties(IMediaTranscriptEntry)

    def __str__(self):
        return "%s,%s,%s" % (self.id, self.start_timestamp, self.end_timestamp)

    def __repr__(self):
        return "%s(%s,%s,%s\n%r)" % (self.__class__.__name__,
                                     self.id,
                                     self.start_timestamp,
                                     self.end_timestamp,
                                     self.transcript)


@interface.implementer(IAudioTranscriptEntry)
class AudioTranscriptEntry(MediaTranscriptEntry):
    createDirectFieldProperties(IAudioTranscriptEntry)


@interface.implementer(IVideoTranscriptEntry)
class VideoTranscriptEntry(MediaTranscriptEntry):
    createDirectFieldProperties(IVideoTranscriptEntry)


@interface.implementer(IMediaTranscript)
class MediaTranscript(SchemaConfigured):
    createDirectFieldProperties(IMediaTranscript)

    @property
    def text(self):
        return u'\n'.join(x.transcript for x in self.entries)

    def append(self, value):
        return self.entries.append(value)

    def __getitem__(self, index):
        return self.entries[index]

    def __len__(self):
        return len(self.entries)

    def __str__(self):
        return "%s" % len(self)

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.entries)

    def __iter__(self):
        return iter(self.entries)


@interface.implementer(IAudioTranscript)
class AudioTranscript(MediaTranscript):
    createDirectFieldProperties(IAudioTranscript)


@interface.implementer(IVideoTranscript)
class VideoTranscript(MediaTranscript):
    createDirectFieldProperties(IVideoTranscript)
