# libwine
A python library for interacting with Wine.

## Usage
```python
from libwine.wine import Wine

my_wineprefix = Wine(
    winepath="/path/to/wine", # folder
    wineprefix="/path/to/wineprefix", # empty or existing
    verbose=3 # +all
)

'''
Update the wineprefix directory.
'''
my_wineprefix.update()

'''
Simulate system restart for the wineprefix,
don't do normal startup operations.
'''
my_wineprefix.restart()

'''
Kill all processes running inside the wineprefix.
'''
my_wineprefix.kill()

'''
Simulate system shutdown for the wineprefix, don't reboot.
'''
my_wineprefix.shutdown()

'''
Launch the winecfg tool on the active display.
'''
my_wineprefix.winecfg()

'''
Launch the cmd tool.
'''
my_wineprefix.cmd()
my_wineprefix.cmd(terminal="gnome-terminal") # on external terminal

'''
Launch the taskmgr tool on the active display.
'''
my_wineprefix.taskmanager()

'''
Launch the control tool on the active display.
'''
my_wineprefix.controlpanel()

'''
Launch the uninstaller tool on the active display.
'''
my_wineprefix.uninstaller()

'''
Launch the regedit tool on the active display.
'''
my_wineprefix.regedit()

'''
Execute custom wine commands inside the wineprefix.
'''
my_wineprefix.command("DIR)

'''
Execute exe/msi/bat files inside the wineprefix.
'''
my_wineprefix.run_exe("path/to/file.exe")
my_wineprefix.run_msi("ath/to/file.msi")
my_wineprefix.run_bat("ath/to/file.bat")

'''
Add (or erdit) key to the wineprefix register.
'''
my_wineprefix.reg_add(
    key="HKEY_CURRENT_USER\\Software\\Wine\\Explorer\\Desktops",
    value="Default",
    data="1920x1080"
)

'''
Delete key from the wineprefix register.
'''
my_wineprefix.reg_delete(
    key="HKEY_CURRENT_USER\\Software\\Wine\\Explorer\\Desktops",
    value="Default"
)

'''
Change Windows version
'''
my_wineprefix.set_windows("win10")

'''
Manage Virtual Desktop
'''
my_wineprefix.set_virtual_desktop(
    status=True,
    res="800x600"
)
my_wineprefix.set_virtual_desktop(status=False)

'''
Overriding a DLL in the wineprefix.
'''
my_wineprefix.override_dll(
    name="ucrtbase",
    type=2 # builtin/native
)

my_wineprefix.override_dll(
    name="ucrtbase",
    restore=True
)
```