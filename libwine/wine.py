from typing import Union, NewType

class Wine:
    '''
    Create a new object of type Wine with all the methods for its management.

    Parameters
    ----------
    winepath : str
        full path to Wine
    wineprefix: str
        full path to your wineprefix
    '''

    def __init__(self, winepath:str, wineprefix:str):
        pass

    '''
    Wine Tools
    '''
    def winecfg(self):
        '''
        Launch the winecfg tool on the active display.
        '''
        return

    def debug(self, terminal:str=None):
        '''
        Launch the winedbg tool.

        Parameters
        ----------
        terminal : str, optional
            command to an external terminal (default is None)
        '''
        return

    def cmd(self, terminal:str=None):
        '''
        Launch the cmd tool.

        Parameters
        ----------
        terminal : str, optional
            command to an external terminal (default is None)
        '''
        return

    def taskmanager(self):
        '''
        Launch the taskmgr tool on the active display.
        '''
        return

    def controlpanel(self):
        '''
        Launch the control tool on the active display.
        '''
        return

    def uninstaller(self):
        '''
        Launch the uninstaller tool on the active display.
        '''
        return

    def regedit(self):
        '''
        Launch the regedit tool on the active display.
        '''
        return

    def command(self):
        '''
        Execute custom wine commands inside the wineprefix.
        '''
        return

    '''
    Wine uptime management
    '''
    def __wineboot(self, status:int):
        '''
        Manage Wine server uptime using wineboot

        Parameters
        ----------
        status : int
            the state ID to set in wineboot:
            0 (kill): Kill running processes without any cleanup
            1 (restart): Restart only, don't do normal startup operations
            2 (shutdown): Shutdown only, don't reboot
            3 (update): Update the wineprefix directory
        '''
        return
        
        
    def kill(self):
        '''
        Kill all processes running inside the wineprefix.
        '''
        self.__wineboot(0)
        return

    def restart(self):
        '''
        Simulate system restart for the wineprefix,
        don't do normal startup operations.
        '''
        self.__wineboot(1)
        return

    def shutdown(self):
        '''
        Simulate system shutdown for the wineprefix, don't reboot.
        '''
        self.__wineboot(2)
        return

    def update(self):
        '''
        Update the wineprefix directory.
        '''
        self.__wineboot(3)
        return
    
    '''
    Wine register management
    '''
    def reg_add(self):
        '''
        Add (or edit) key to the wineprefix register.
        '''
        return

    def reg_delete(self):
        '''
        Delete key from the wineprefix register.
        '''
        return
    
    '''
    Wine DLL overrides management
    '''
    def override_dll(self, type:int):
        '''
        Overriding a DLL in the wineprefix.

        Parameters
        ----------
        type : int
            the type of override:
            0 (builtin): provided by Wine
            1 (native): provided by Windows
            2 (builtin/native): builtin then native
            3 (native/builtin): native then builtin
        '''
        return