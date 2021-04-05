from libwine.wine import Wine

w = Wine(
    winepath="/home/mirko/.local/share/bottles/runners/chardonnay-6.4",
    wineprefix="/home/mirko/libwine_tests"
)
w.set_dpi(96)