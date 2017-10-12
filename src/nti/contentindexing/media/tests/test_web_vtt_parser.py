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

from nti.contentindexing.media.web_vtt_parser import Cue
from nti.contentindexing.media.web_vtt_parser import WebVTTCueTimingsAndSettingsParser

from nti.contentindexing.tests import ContentIndexingLayerTest


class TestWebVttParser(ContentIndexingLayerTest):

    def test_cue(self):
        a = Cue(u'1', u'ichigo', end_time=1)
        b = Cue(u'2', u'aizen', start_time=1, end_time=2)
        assert_that(str(a), is_('ichigo'))
        assert_that(repr(b), is_not(none()))
        assert_that(a.__lt__(b), is_(True))
        assert_that(b.__gt__(a), is_(True))

    def test_cue_timings_parser(self):
        p = WebVTTCueTimingsAndSettingsParser('')
        p.pos = 1
        assert_that(p.timestamp(), is_(none()))
