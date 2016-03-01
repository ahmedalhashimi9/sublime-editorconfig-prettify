import jsbeautifier

from .. import Prettifier


class JavaScriptPrettifier(Prettifier):

    def prettify(self):
        opts = jsbeautifier.default_options()
        res = jsbeautifier.beautify_file(self.path_to_file, opts)

        print(res)
        return True
