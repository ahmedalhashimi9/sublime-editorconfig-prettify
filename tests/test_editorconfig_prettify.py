#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_editorconfig_prettify.py
----------------------------------

Tests for `editorconfig_prettify` module.
"""

import os
import unittest

from editorconfig_prettify import Prettifier
from editorconfig_prettify.languages import JavaScriptPrettifier


class TestEditorconfigPrettify(unittest.TestCase):

    def setUp(self):
        self.prettifier = Prettifier('fixtures/test.js')

    def test_prettifier_prettify(self):
        self.assertRaises(NotImplementedError, self.prettifier.prettify)


class TestJavaScriptPrettifier(unittest.TestCase):

    def setUp(self):
        dir = os.path.dirname(__file__)
        path_to_file = os.path.join(dir, 'fixtures/test.js')

        self.prettifier = JavaScriptPrettifier(path_to_file)

    def test_javascript_prettifier(self):
        self.assertEqual(self.prettifier.prettify(), True)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
