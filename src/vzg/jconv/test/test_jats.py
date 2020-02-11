# -*- coding: UTF-8 -*-
"""Beschreibung

##############################################################################
#
# Copyright (c) 2020 Verbundzentrale des GBV.
# All Rights Reserved.
#
##############################################################################
"""

# Imports
import sys
import unittest
import logging
from vzg.jconv.converter.jats import JatsArticle
from vzg.jconv.gapi import JATS_PUBTYPE
from pathlib import Path
import json
from lxml import etree

__author__ = """Marc-J. Tegethoff <marc.tegethoff@gbv.de>"""
__docformat__ = 'plaintext'

logger = logging.getLogger(__name__)
logger.level = logging.INFO
# stream_handler = logging.StreamHandler(sys.stdout)
# logger.addHandler(stream_handler)


class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.fpath = Path("article.xml")
        self.jpath = Path("article.json")

        with open(self.jpath) as fh:
            self.testdata = json.load(fh)

        with open(self.fpath, 'rb') as fh:
            self.dom = etree.parse(fh)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test01(self):
        """title"""
        jobj = JatsArticle(self.dom, JATS_PUBTYPE.epub.name)
        self.assertEqual(jobj.title, self.testdata['title'], "title")

    def test02(self):
        """lang_code"""
        jobj = JatsArticle(self.dom, JATS_PUBTYPE.epub.name)
        self.assertEqual(
            jobj.lang_code, self.testdata['lang_code'], "lang_code")

    def test03(self):
        """primary_id"""
        jobj = JatsArticle(self.dom, JATS_PUBTYPE.epub.name)
        self.assertEqual(
            jobj.primary_id, self.testdata['primary_id'], "primary_id")

    def test04(self):
        """journal"""
        jobj = JatsArticle(self.dom, JATS_PUBTYPE.epub.name)
        self.assertEqual(
            jobj.journal, self.testdata['journal'], "journal")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCase))
    unittest.TextTestRunner(verbosity=2).run(suite)
