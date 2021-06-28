from libwine.wine import Wine

w = Wine(
    winepath="/home/mirko/.local/share/bottles/runners/chardonnay-6.11-unstable",
    wineprefix="/home/mirko/.local/share/bottles/bottles"
)
w.set_app_default(
    executable="wmplayerexe",
    version="win7"
)
w.winecfg()