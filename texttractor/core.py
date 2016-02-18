# -*- coding: utf-8 -*-
"""
Copyright (c) 2016 Tony Walker

TextTractor - Extract main text from web pages

Extraction Strategy:

    - Replace html tags with their space representation
    - Select the most promising block(s) of text
    - Reconstruct main text

"""

import re
import requests


class TextCleaner(object):
    """ Clean text of junk """

    def __init__(self, options=None):
        super(TextCleaner, self).__init__()
        self.options = options

    def clean(self, text):
        """ Remove unnecessary blocks of text, such as scripts, style, etc """

        # JS Scripts
        pattern_js = re.compile(r'<script.*?>.*?</script>', re.DOTALL)
        text = pattern_js.sub('', text)

        # HTML Comments
        pattern_comment = re.compile(r'<!--.+?-->', re.DOTALL)
        text = pattern_comment.sub('', text)

        # CSS/Style
        pattern_css = re.compile(r'<style.*?>.*?</style>', re.DOTALL)
        text = pattern_css.sub('', text)

        # Extract only html body
        pattern_body = re.compile(r'<body.*?>(.*?)</body>', re.DOTALL)
        match = pattern_body.search(text)
        text = match.groups()[0] if match else text

        # Finally, remove whitespace from edges
        final = text.strip('\n\t ').replace('\n', '')
        return final


class TextTractor(object):
    """ Main object for extracting text """

    def __init__(self, cleaner=None):
        super(TextTractor, self).__init__()
        self.cleaner = cleaner or TextCleaner()

    def extract(self, url=None, text=None):
        text = text if text else requests.get(url).text
        text = self.cleaner.clean(text)
        return self.blank(text)

    def blank(self, text):
        """ Replace html tags with blank spaces of the same size """
        pattern = r'(<.+?>)'
        for segment in re.findall(pattern, text, flags=re.DOTALL):
            text = re.sub(re.escape(segment), ' ' * len(segment), text)
        return text
