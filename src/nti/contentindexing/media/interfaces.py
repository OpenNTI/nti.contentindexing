#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from zope.interface.common.sequence import IMinimalSequence

from nti.schema.field import Object
from nti.schema.field import ValidText
from nti.schema.field import ListOrTuple
from nti.schema.field import ValidTextLine

class IMediaTranscriptEntry(interface.Interface):
	"""
	Marker interface for video transcript entry
	"""
	transcript = ValidText(title='Transcript text')
	end_timestamp = ValidTextLine(title='End time stamp')
	start_timestamp = ValidTextLine(title='Start time stamp')
	id = ValidTextLine(title='Transcript entry id', required=False)
	language = ValidTextLine(title='Transcript language', required=False,
							 default='en')

class IAudioTranscriptEntry(IMediaTranscriptEntry):
	pass

class IVideoTranscriptEntry(IMediaTranscriptEntry):
	pass

class IMediaTranscript(IMinimalSequence):
	"""
	Marker interface for media transcript
	"""
	entries = ListOrTuple(Object(IMediaTranscriptEntry, title='the entry'),
						  		 title='Ordered transcript entries')
	
	text = interface.Attribute('All entries transcript text')
	text.setTaggedValue('_ext_excluded_out', True)

class IAudioTranscript(IMediaTranscript):
	"""
	Marker interface for audio transcript
	"""
	entries = ListOrTuple(Object(IAudioTranscriptEntry, title='the entry'),
						  		 title='Ordered transcript entries')

class IVideoTranscript(IMediaTranscript):
	"""
	Marker interface for video transcript
	"""
	entries = ListOrTuple(Object(IVideoTranscriptEntry, title='the entry'),
						  		 title='Ordered transcript entries')

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
