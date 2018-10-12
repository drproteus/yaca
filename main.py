# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import rumps
import subprocess

rumps.debug_mode(True)

class CaffeineApp(rumps.App):
    @rumps.clicked("caffeinate?")
    def toggle(self, sender):
        if not sender.state:
            try:
                self.caffeine_proc = subprocess.Popen(["caffeinate", "-d"])
                sender.state = not sender.state
            except Exception as e:
                print(e)
        else:
            try:
                if self.caffeine_proc:
                    self.caffeine_proc.kill()
                    self.caffeine_pro = None
                sender.state = not sender.state
            except Exception as e:
                print(e)
        self.title = "📺🔒" if sender.state else "📺🔓"

    @rumps.clicked("exit")
    def quit(self, sender):
        if isinstance(self.caffeine_proc, subprocess.Popen):
            self.caffeine_proc.kill()
        rumps.quit_application(sender)

    def __init__(self, *args, **kwargs):
        super(CaffeineApp, self).__init__(*args, **kwargs)
        self.quit_button = None
        self.caffeine_proc = None

if __name__ == "__main__":
    CaffeineApp("📺🔓").run()
