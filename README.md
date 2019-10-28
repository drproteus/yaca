# Yet Another Caffeine App

Creating desktop apps on OS X with Python is a pain. When all you want is a simple statusbar menu, it hurts to resort to Swift or Obj-C (I know).

So when I found this library [rumps](https://github.com/jaredks/rumps) I had to make a _something_ with it.

Since "caffeinating" a Mac is really just using the `caffeinate` CLI tool. A little `subprocess` here, a little `rumps` there, and no more sleepy Mac.

### Building

```bash
pip install -r requirements.txt
make build
# results in `dist/yaca.app`
```
