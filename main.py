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
                proc = getattr(self, "caffeine_proc", None)
                if proc:
                    proc.kill()
                sender.state = not sender.state
            except Exception as e:
                print(e)
        self.title = "📺🔒" if sender.state else "📺🔓"

if __name__ == "__main__":
    app = CaffeineApp("📺🔓")
    app.run()
    proc = getattr(app, "caffeine_proc", None)
    if proc:
        proc.kill()
