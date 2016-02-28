# -*- coding: utf-8 -*-
import os

from pprint import pprint

from editorconfig import get_properties, EditorConfigError

import jsbeautifier


class Prettifier(object):

    def __init__(self, file, options=None):
        if options is None:
            self.options = {}
        else:
            self.options = options

        cwd = os.path.dirname(os.path.realpath(__file__))
        self.path_to_file = os.path.join(cwd, file)

    def prettify(self):
        raise NotImplementedError()

    @property
    def config(self):
        try:
            self._config = get_properties(self.path_to_file)
        except EditorConfigError:
            print 'Error occurred while getting EditorConfig properties'

        return self._config


class JavaScriptPrettifier(Prettifier):

    def prettify(self):
        opts = jsbeautifier.default_options()
        res = jsbeautifier.beautify_file(self.path_to_file, opts)

        print(res)


if __name__ == '__main__':
    p = JavaScriptPrettifier('test.js')
    pprint(p.config)
    p.prettify()
