import sublime
import sublime_plugin

from editorconfig import get_properties, EditorConfigError


class PrettifyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.path_to_file = self.view.file_name()
        print(self.path_to_file)
