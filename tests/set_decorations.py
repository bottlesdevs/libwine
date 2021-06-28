from libwine.wine import Wine

w = Wine(
    winepath="/home/mirko/.local/share/bottles/runners/chardonnay-6.11-unstable",
    wineprefix="/home/mirko/libwine_tests"
)
w.set_decorations(True)