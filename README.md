# libwine
A python library for interacting with Wine.

## Usage
```python
from libwine import wine

wine = Wine(
    winepath="/path/to/wine", # folder
    wineprefix="/path/to/wineprefix", # empty or existing
    verbose=3 # +all
)

wine.update()
wine.winecfg()
wine.cmd(terminal="gnome-terminal")
wine.kill()
```