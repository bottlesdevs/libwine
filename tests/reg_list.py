from libwine.wine import Wine

w = Wine(
    winepath="/home/mirko/.local/share/bottles/runners/chardonnay-6.4",
    wineprefix="/home/mirko/libwine_tests"
)
w.override_dll(
    name="test123",
    override=2
)
w.override_dll(
    name="test321",
    override=1
)
values = w.reg_list("HKEY_CURRENT_USER\\Software\\Wine\\DllOverrides")
print(values)
