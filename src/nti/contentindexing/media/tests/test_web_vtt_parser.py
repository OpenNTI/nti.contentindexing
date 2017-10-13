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
from hamcrest import has_entry
from hamcrest import assert_that
from hamcrest import has_property

from nti.testing.matchers import is_empty

from nti.contentindexing.media.web_vtt_parser import Cue
from nti.contentindexing.media.web_vtt_parser import WebVTTParser
from nti.contentindexing.media.web_vtt_parser import WebVTTCueTextParser
from nti.contentindexing.media.web_vtt_parser import WebVTTCueTimingsAndSettingsParser

from nti.contentindexing.tests import ContentIndexingLayerTest


class LocalCueTextParser(WebVTTCueTextParser):

    def __init__(self, *args, **kwargs):
        super(LocalCueTextParser, self).__init__(*args, **kwargs)
        self.err = self._local_error

    def _local_error(self, *unused_args):
        self.has_error = True


class LocalCueTimingsParser(WebVTTCueTimingsAndSettingsParser):

    def __init__(self, *args, **kwargs):
        super(LocalCueTimingsParser, self).__init__(*args, **kwargs)
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

    def test_cue_timings_timestamp(self):
        p = WebVTTCueTimingsAndSettingsParser('', pos=1)
        assert_that(p.timestamp(), is_(none()))

        p = LocalCueTimingsParser('ichigo')
        assert_that(p.timestamp(), is_(none()))

        p = LocalCueTimingsParser('130,')
        assert_that(p.timestamp(), is_(none()))

        p = LocalCueTimingsParser('00:0:')
        assert_that(p.timestamp(), is_(none()))

        p = LocalCueTimingsParser('120:00,')
        assert_that(p.timestamp(), is_(none()))

        p = LocalCueTimingsParser('120:00:0')
        assert_that(p.timestamp(), is_(none()))

        p = LocalCueTimingsParser('120:00:00')
        assert_that(p.timestamp(), is_(none()))

        p = LocalCueTimingsParser('20:00:00.89')
        assert_that(p.timestamp(), is_(none()))

        p = LocalCueTimingsParser('20:64:00.899')
        assert_that(p.timestamp(), is_(none()))

        p = LocalCueTimingsParser('00:00:89.899')
        assert_that(p.timestamp(), is_(none()))

        p = LocalCueTimingsParser('0:00:00.899')
        assert_that(p.parse_timestamp(), is_not(none()))

        p = LocalCueTimingsParser('1:00:02.691***')
        assert_that(p.parse_timestamp(), is_(none()))

    def test_cue_settings(self):

        def parse_settings(value, check=True):
            cue = Cue()
            p = LocalCueTimingsParser('')
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

    def test_cue_timings_parse(self):
        p = LocalCueTimingsParser('')
        assert_that(p.parse(Cue(), 0), is_(none()))

        p = LocalCueTimingsParser('0:00:00.899 --> 1:00:02.691')
        p.parse(Cue(), 1)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTimingsParser('0:00:00.899-1:00:02.691')
        p.parse(Cue(), 0)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTimingsParser('0:00:00.899*1:00:02.691')
        assert_that(p.parse(Cue(), 0), is_(none()))
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTimingsParser('0:00:00.899 -* 1:00:02.691')
        assert_that(p.parse(Cue(), 0), is_(none()))
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTimingsParser('0:00:00.899 --* 1:00:02.691')
        assert_that(p.parse(Cue(), 0), is_(none()))
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTimingsParser('0:00:00.899-->1:00:02.691')
        p.parse(Cue(), 0)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTimingsParser('0:00:00.899 --> ichigo')
        assert_that(p.parse(Cue(), 0), is_(none()))
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTimingsParser('0:00:00.899 --> 0:00:00.899')
        p.parse(Cue(), 0)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTimingsParser('0:00:00.899 --> 0:00:00.899-line:15%')
        assert_that(p.parse(Cue(), 0), is_(True))

    def test_cue_text_parse(self):
        data = (0.899, 2.691)
        # invalid tag
        p = LocalCueTextParser("<h>location</h>")
        p.parse(*data)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTextParser("<v>a<v>b</v></v>")
        p.parse(*data)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTextParser("<b foo>x</b>")
        p.parse(*data)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTextParser("<b>location</b> of the book.")
        p.parse(*data)

        s = "<ruby>WWW<rt>World Wide Web</rt>oui<rt>yes</rt></ruby>"
        p = LocalCueTextParser(s)
        p.parse(*data)

        # ivalid rubby content
        p = LocalCueTextParser("<ruby>x<rt>y</ruby></rt>")
        p.parse(*data)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTextParser("Like a <00:19.000> big-a")
        p.parse(*data)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTextParser("Like a <00:19.000> big-a <00:18.000> ")
        p.parse(*data)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTextParser("<b>Like")
        p.parse(*data)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTextParser("&lt;Like")
        p.parse(*data)

        p = LocalCueTextParser("&&Like")
        p.parse(*data)

        p = LocalCueTextParser("&gt; &amp; here")
        p.parse(*data)

        p = LocalCueTextParser("&pt; here")
        p.parse(*data)
        assert_that(p, has_property('has_error', is_(True)))

        p = LocalCueTextParser("&<")
        p.parse(*data)
        assert_that(p, has_property('has_error', is_(True)))

        # coverage... start tag followed by space
        p = LocalCueTextParser("< v/>")
        p.parse(*data)

        # coverage... start tag followed by class
        p = LocalCueTextParser("<.class />")
        p.parse(*data)

        # coverage... empty open-close tag
        p = LocalCueTextParser("<>")
        p.parse(*data)

        # coverage... empty open-close tag
        p = LocalCueTextParser("</>")
        p.parse(*data)

        # class
        p = LocalCueTextParser("<c.bleach>aizen</c>")
        p.parse(*data)

        # class
        p = LocalCueTextParser("<c.\tbleach>aizen</c>")
        p.parse(*data)

        # class
        p = LocalCueTextParser("<c.\nbleach>aizen</c>")
        p.parse(*data)

        # class
        p = LocalCueTextParser("<c..bleach>aizen</c>")
        p.parse(*data)

        # class
        p = LocalCueTextParser("<v\nbleach>aizen</v>")
        p.parse(*data)

    def test_web_vtt_parser(self):
        p = WebVTTParser()
        result = p.parse('ichigo')
        assert_that(result, has_entry('errors', is_not(is_empty())))

        result = p.parse('WEBVTT\aizen\n-->')
        assert_that(result, has_entry('errors', is_not(is_empty())))

        result = p.parse('WEBVTT\n\n1\n\t')
        assert_that(result, has_entry('errors', is_not(is_empty())))

        s = 'WEBVTT\n\n1\n00:00:00.899 --> 00:00:02.691\n00:00:00.899 --> 00:00:02.691\n-->\nhere\n-->'
        result = p.parse(s)
        assert_that(result, has_entry('errors', is_not(is_empty())))
