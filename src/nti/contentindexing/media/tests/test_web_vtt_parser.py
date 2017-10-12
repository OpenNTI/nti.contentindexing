#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import none
from hamcrest import is_not
from hamcrest import assert_that
from hamcrest import has_property

from nti.contentindexing.media.web_vtt_parser import Cue
from nti.contentindexing.media.web_vtt_parser import WebVTTCueTimingsAndSettingsParser

from nti.contentindexing.tests import ContentIndexingLayerTest


class _Parser(WebVTTCueTimingsAndSettingsParser):

    def __init__(self, *args, **kwargs):
        super(_Parser, self).__init__(*args, **kwargs)
        self.err = self._local_error
        
    def _local_error(self, *unused_args):
        self.has_error = True


class TestWebVttParser(ContentIndexingLayerTest):

    def test_cue(self):
        a = Cue(u'1', u'ichigo', end_time=1)
        b = Cue(u'2', u'aizen', start_time=1, end_time=2)
        assert_that(str(a), is_('ichigo'))
        assert_that(repr(b), is_not(none()))
        assert_that(a.__lt__(b), is_(True))
        assert_that(b.__gt__(a), is_(True))

    def test_cue_timings_parser(self):
        p = WebVTTCueTimingsAndSettingsParser('', pos=1)
        assert_that(p.timestamp(), is_(none()))
        
        p = WebVTTCueTimingsAndSettingsParser('ichigo')
        assert_that(p.timestamp(), is_(none()))
        
        p = WebVTTCueTimingsAndSettingsParser('130,')
        assert_that(p.timestamp(), is_(none()))
        
        p = WebVTTCueTimingsAndSettingsParser('00:0:')
        assert_that(p.timestamp(), is_(none()))
        
        p = WebVTTCueTimingsAndSettingsParser('120:00,')
        assert_that(p.timestamp(), is_(none()))
        
        p = WebVTTCueTimingsAndSettingsParser('120:00:0')
        assert_that(p.timestamp(), is_(none()))
        
        p = WebVTTCueTimingsAndSettingsParser('120:00:00')
        assert_that(p.timestamp(), is_(none()))
        
        p = WebVTTCueTimingsAndSettingsParser('20:00:00.89')
        assert_that(p.timestamp(), is_(none()))
        
        p = WebVTTCueTimingsAndSettingsParser('20:64:00.899')
        assert_that(p.timestamp(), is_(none()))
        
        p = WebVTTCueTimingsAndSettingsParser('00:00:89.899')
        assert_that(p.timestamp(), is_(none()))

    def test_cue_settings_parser(self):
        
        def parse_settings(value, check=True):
            cue = Cue()
            p = _Parser('')
            p.parse_settings(value, cue)
            if check:
                assert_that(p, has_property('has_error', is_(True)))
            
        parse_settings('align:middle align:middle')
        parse_settings('align:')
        parse_settings('vertical:xx')
        parse_settings('line:xx')
        parse_settings('line:1-')
        parse_settings('line:1%0')
        parse_settings('line:-10%')
        parse_settings('line:200%')
        
        parse_settings('position:10')
        parse_settings('position:300%')
        
        parse_settings('size:10')
        parse_settings('size:300%')
        
        parse_settings('align:invalid')
        
        parse_settings('invalid:300%')
