#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_editorconfig_prettify.py
----------------------------------

Tests for `editorconfig_prettify` module.
"""

import unittest

from editorconfig_prettify import Prettifier
from editorconfig_prettify.languages import JavaScriptPrettifier


class TestEditorconfig_prettify(unittest.TestCase):

    def setUp(self):
        self.prettifier = Prettifier('fixtures/test.js')

    def tearDown(self):
        pass

    def test_prettifier_prettify(self):
        self.assertRaises(NotImplementedError, self.prettifier.prettify)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
