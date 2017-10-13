#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import none
from hamcrest import close_to
from hamcrest import assert_that
from hamcrest import starts_with
from hamcrest import contains_string
from hamcrest import less_than_or_equal_to

import unittest
from datetime import datetime

from nti.contentindexing.utils import get_datetime
from nti.contentindexing.utils import sanitize_content
from nti.contentindexing.utils import video_date_to_millis
from nti.contentindexing.utils import date_to_videotimestamp
from nti.contentindexing.utils import videotimestamp_to_datetime

from nti.contentindexing.tests import SharedConfiguringTestLayer


class TestUtils(unittest.TestCase):

    layer = SharedConfiguringTestLayer

    def test_sanitize_content(self):
        assert_that(sanitize_content(None), is_(none()))
        assert_that(sanitize_content(u'<b>ichigo</b>'),
                    is_('ichigo'))

    def test_videotimestamp(self):
        f = 1321391468.413528
        assert_that(date_to_videotimestamp(f), starts_with('15:11:08.4'))
        assert_that(date_to_videotimestamp(str(f)), starts_with('15:11:08.4'))
        assert_that(date_to_videotimestamp(None), is_(u''))

        dt = videotimestamp_to_datetime('15:11:08.413')
        assert_that(dt, is_(datetime))
        assert_that(str(dt), contains_string('15:11:08.413'))

    def test_video_date_to_millis(self):
        dt = videotimestamp_to_datetime('15:11:08.413')
        assert_that(video_date_to_millis(dt),
                    is_(close_to(54668413, 1)))

    def test_get_datetime(self):
        f = 1321391468.411328
        s = '1321391468.411328'
        assert_that(get_datetime(f), is_(get_datetime(s)))
        assert_that(datetime.now(), less_than_or_equal_to(get_datetime()))
