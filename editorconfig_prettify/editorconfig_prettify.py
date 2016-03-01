# -*- coding: utf-8 -*-
from functools import wraps

from editorconfig import get_properties, EditorConfigError


class Prettifier(object):

    def __init__(self, path_to_file, options=None):
        if options is None:
            self.options = {}
        else:
            self.options = options

        self.path_to_file = path_to_file

    def prettify(self):
        raise NotImplementedError('Subclasses need to implement this method')

    @property
    def config(self):
        try:
            self._config = get_properties(self.path_to_file)
        except EditorConfigError:
            print('Error occurred while getting EditorConfig properties')

        return self._config


def register(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        print('Registered {0}'.format(func.__name__))
        return True
    return func_wrapper
