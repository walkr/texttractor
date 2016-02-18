#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_texttractor
----------------------------------

Tests for `texttractor` module.
"""

import unittest

from texttractor import TextTractor
from texttractor import TextCleaner


class TestTexttractor(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic(self):
        t = TextTractor()

        with open('tests/testdata/coindesk.html') as fh:
            text = fh.read()
            text = t.extract(text=text)
            self.assertTrue('the' in text)


class TestTextCleaner(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cleanup(self):
        text = '''
            '''
        with open('tests/testdata/junk.html') as fh:
            text = fh.read()
            c = TextCleaner()
            self.assertTrue('abc' == c.clean(text))


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
