# -*- coding: utf-8 -*-
from editorconfig import get_properties, EditorConfigError


class Prettifier(object):

    def __init__(self, view, options=None):
        if options is None:
            options = {}

        self.options = options
        self.view = view

    def prettify(self):
        raise NotImplementedError('Subclasses need to implement this method')

    @property
    def config(self):
        try:
            self._config = get_properties(self.view)
        except EditorConfigError:
            print('Error occurred while getting EditorConfig properties')

        return self._config
