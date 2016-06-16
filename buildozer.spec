[app]
title = Catalogo UIP
package.name = mt.catalogouip
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py
requirements = sqlite3,kivy
orientation = all
fullscreen = Enabled
version = 1.0
android.permissions = INTERNET

[buildozer]
log_level = 1
warn_on_root = 1

