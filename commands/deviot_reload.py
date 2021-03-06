import sublime
import sublime_plugin

from ..api import deviot
from ..libraries.progress_bar import ProgressBar
from ..libraries.reloader import reload_package

NAME = deviot.plugin_name()


class DeviotReloadCommand(sublime_plugin.WindowCommand):

    def run(self, pkg_name=NAME):
        sublime.set_timeout_async(lambda: self.run_async(pkg_name))

    def run_async(self, pkg_name=None):
        progress_bar = ProgressBar("Reloading %s" % pkg_name)
        progress_bar.start()

        reload_package(pkg_name)

        progress_bar.stop()
