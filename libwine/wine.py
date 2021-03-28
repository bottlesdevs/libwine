import glob
import re

from .utils.command import Command
from .wineprocess import WineProcess


class Wine:
    '''
    Create a new object of type Wine with all the methods for its management.

    Parameters
    ----------
    winepath : str
        full path to Wine
    wineprefix: str
        full path to your wineprefix
    verbose: int, optional
        verbosity status of wine logs (default is 0):
        0 (silent): -all
        1 (quite): -warn+all
        2 (no fixme): fixme-all
        3 (debug): +all

    Raises
    ------
    ValueError
        If the given winepath doesn't contains all the essential paths.
    '''

    _winepath = str
    _wineprefix = str
    _verbose = int

    _terminals = {
        'xterm': 'xterm -e %s',
        'konsole': 'konsole -e %s',
        'gnome-terminal': 'gnome-terminal -- %s',
        'xfce4-terminal': 'xfce4-terminal --command %s',
        'mate-terminal': 'mate-terminal --command %s'
    }

    _verbose_levels = {
        0: "-all",
        1: "-warn+all",
        2: "fixme-all",
        3: "+all"
    }
    _windows_versions = {
        "win10": {
            "ProductName": "Microsoft Windows 10",
            "CSDVersion": "",
            "CurrentBuild": "17763",
            "CurrentBuildNumber": "17763",
            "CurrentVersion": "10.0",
        },
        "win81": {
            "ProductName": "Microsoft Windows 8.1",
            "CSDVersion": "",
            "CurrentBuild": "9600",
            "CurrentBuildNumber": "9600",
            "CurrentVersion": "6.3",
        },
        "win8": {
            "ProductName": "Microsoft Windows 8",
            "CSDVersion": "",
            "CurrentBuild": "9200",
            "CurrentBuildNumber": "9200",
            "CurrentVersion": "6.2",
        },
        "win7": {
            "ProductName": "Microsoft Windows 7",
            "CSDVersion": "Service Pack 1",
            "CurrentBuild": "7601",
            "CurrentBuildNumber": "7601",
            "CurrentVersion": "6.1",
        },
        "win2008r2": {
            "ProductName": "Microsoft Windows 2008 R2",
            "CSDVersion": "Service Pack 1",
            "CurrentBuild": "7601",
            "CurrentBuildNumber": "7601",
            "CurrentVersion": "6.1",
        },
        "win2008": {
            "ProductName": "Microsoft Windows 2008",
            "CSDVersion": "Service Pack 2",
            "CurrentBuild": "6002",
            "CurrentBuildNumber": "6002",
            "CurrentVersion": "6.0",
        },
        "winxp": {
            "ProductName": "Microsoft Windows XP",
            "CSDVersion": "Service Pack 2",
            "CurrentBuild": "3790",
            "CurrentBuildNumber": "3790",
            "CurrentVersion": "5.2",
        },
    }

    _dll_overrides = {
        0: "builtin",
        1: "native",
        2: "builtin,native",
        3: "native,builtin"
    }

    def __init__(self, winepath: str, wineprefix: str, verbose: int = 0):
        self._winepath = winepath
        self._wineprefix = wineprefix

        if verbose in self._verbose_levels:
            self._verbose = verbose

        if not self.__validate_winepath():
            raise ValueError("Given winepath doesn't seem a valid Wine path.")

    '''
    Wine checks
    '''

    def __validate_winepath(self):
        '''
        Check if essential paths exist in winepath.
        '''
        promise = ["lib64", "share", "bin", "lib"]

        dirs = glob.glob(f"{self._winepath}/*")
        dirs = [d.replace(f"{self._winepath}/", "") for d in dirs]

        for p in promise:
            if p not in dirs:
                return False

        return True

    def check_arch_compatibility(self):
        '''
        Check if the given wine arch is compatible with the running system
        TODO: this method should check for ARM wine compatibility on ARM devices
        '''
        return

    def execute(self, command: str, comunicate: bool = False, envs: dict = {}, terminal: str = None):
        '''
        Execute command inside wineprefix using the wine in winepath

        Parameters
        ----------
        command : str
            command to be executed inside the wineprefix
        comunicate : bool, optional
            to get the output of the command (default is False)
        envs: dict, optional
            dict of environment variables to pass on the execution
        terminal : str, optional
            command to an external terminal (default is None)
        '''
        envs["WINEPREFIX"] = self._wineprefix
        envs["WINEDEBUG"] = self._verbose_levels[self._verbose]
        command = f"{self._winepath}/bin/wine64 {command}"

        if terminal in self._terminals:
            command = self._terminals[terminal] % command

        cmd = Command(
            command=command,
            cwd=self._wineprefix,
            envs=envs
        )

        if comunicate:
            return cmd.comunicate()

        return cmd.execute()

    '''
    Wine Tools
    '''

    def winecfg(self):
        '''
        Launch the winecfg tool on the active display.
        '''
        self.execute(command="winecfg")

    def debug(self, terminal: str = None):
        '''
        Launch the winedbg tool.

        Parameters
        ----------
        terminal : str, optional
            command to an external terminal (default is None)
        '''

        self.execute(
            command="winedbg",
            terminal=terminal
        )

    def cmd(self, terminal: str = None):
        '''
        Launch the cmd tool.

        Parameters
        ----------
        terminal : str, optional
            command to an external terminal (default is None)
        '''

        self.execute(
            command="cmd",
            terminal=terminal
        )

    def taskmanager(self):
        '''
        Launch the taskmgr tool on the active display.
        '''
        self.execute(command="taskmgr")

    def controlpanel(self):
        '''
        Launch the control tool on the active display.
        '''
        self.execute(command="control")

    def uninstaller(self):
        '''
        Launch the uninstaller tool on the active display.
        '''
        self.execute(command="uninstaller")

    def regedit(self):
        '''
        Launch the regedit tool on the active display.
        '''
        self.execute(command="regedit")

    '''
    Wine commandd execution
    '''

    def command(self, command: str):
        '''
        Execute custom wine commands inside the wineprefix.

        Parameters
        ----------
        command : str
            the command to be executed
        '''
        self.execute(command=command)

    def run_exe(self, executable_path: str, envs: dict = {}):
        '''
        Execute exe files inside the wineprefix.
        executable_path : str
            full path to the .exe file
        envs: dict, optional
            dict of environment variables to pass on the execution
        '''
        command = executable_path
        self.execute(command=command, envs=envs)

    def run_msi(self, msi_path: str, envs: dict = {}):
        '''
        Execute msi files inside the wineprefix.
        msi_path : str
            full path to the .msi file
        envs: dict, optional
            dict of environment variables to pass on the execution
        '''
        command = f"msiexec /i {msi_path}"
        self.execute(command=command, envs=envs)

    def run_bat(self, bat_path: str, envs: dict = {}):
        '''
        Execute bat files inside the wineprefix.
        bat_path : str
            full path to the .bat file
        envs: dict, optional
            dict of environment variables to pass on the execution
        '''
        command = f"wineconsole cmd /c '{bat_path}'"
        self.execute(command=command, envs=envs)

    '''
    Wine uptime management
    '''

    def __wineboot(self, status: int, silent: bool = True):
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
        silent: bool, optional
            if the command should not display on display (default True)

        Raises
        ------
        Exception
            If the given state is invalid.
        '''
        states = {
            0: "-k",
            1: "-r",
            2: "-s",
            3: "-u"
        }
        envs = {}

        if silent:
            envs["DISPLAY"] = ":0.0"

        if status in states:
            status = states[status]
            self.execute(command=f"wineboot {status}", envs=envs)
        else:
            raise ValueError(f"[{status}] is not a valid status for wineboot!")

    def kill(self):
        '''
        Kill all processes running inside the wineprefix.
        '''
        self.__wineboot(status=0)

    def restart(self):
        '''
        Simulate system restart for the wineprefix,
        don't do normal startup operations.
        '''
        self.__wineboot(status=1)

    def shutdown(self):
        '''
        Simulate system shutdown for the wineprefix, don't reboot.
        '''
        self.__wineboot(status=2)

    def update(self):
        '''
        Update the wineprefix directory.
        '''
        self.__wineboot(status=3, silent=True)

    '''
    Wine process management
    '''

    def processes(self):
        '''
        Get processes running on the wineprefix.

        Return
        ------
        list:
            A list of WineProcess.
        '''
        processes = []
        parent = None

        winedbg = self.execute(
            command='winedbg --command "info proc"',
            comunicate=True).split("\n")

        # remove the first line from the output (the header)
        del winedbg[0]

        for w in winedbg:
            w = re.sub("\s{2,}", " ", w)[1:].replace("'", "")

            if "\_" in w:
                w = w.replace("\_ ", "")
                w += " child"

            w = w.split(" ")
            w_parent = None

            if len(w) >= 3 and w[1].isdigit():
                w_pid = w[0]
                w_threads = w[1]
                w_name = w[2]

                if len(w) == 3:
                    parent = w_pid
                else:
                    w_parent = parent

                w = WineProcess(
                    pid=w_pid,
                    name=w_name,
                    parent_pid=w_parent,
                    wine=self
                )
                processes.append(w)

        return processes

    '''
    Wine register management
    '''

    def reg_add(self, key: str, value: str, data: str):
        '''
        Add (or edit) key to the wineprefix register.

        Parameters
        ----------
        key : str
            the key name
        value : str
            the key value
        data : str
            the data to store in the key value
        '''
        command = f"reg add '{key}' /v '{value}' /d '{data}' /f"
        self.execute(command=command)

    def reg_delete(self, key: str, value: str):
        '''
        Delete key from the wineprefix register.

        Parameters
        ----------
        key : str
            the key name
        value : str
            the key value to be removed
        '''
        command = f"reg delete '{key}' /v '{value}' /f"
        self.execute(command=command)

    '''
    Simplified Wine register keys
    '''

    def set_windows(self, version: str):
        '''
        Change Windows version of the wineprefix

        Parameters
        ----------
        version : str
            the Windows version to be setted:
            win10 (Microsoft Windows 10)
            win81 (Microsoft Windows 8.1)
            win8 (Microsoft Windows 8)
            win7 (Microsoft Windows 7)
            win2008r2 (Microsoft Windows 2008 R1)
            win2008 (Microsoft Windows 2008)
            winxp (Microsoft Windows XP)

        Raises
        ------
        ValueError
            If the given version is invalid.
        '''

        if version not in self._windows_versions:
            raise ValueError("Given version is not supported.")

        self.reg_add(
            key="HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
            value="ProductName",
            data=self._windows_versions.get(version)["ProductName"]
        )

        self.reg_add(
            key="HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
            value="CSDVersion",
            data=self._windows_versions.get(version)["CSDVersion"]
        )

        self.reg_add(
            key="HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
            value="CurrentBuild",
            data=self._windows_versions.get(version)["CurrentBuild"]
        )

        self.reg_add(
            key="HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
            value="CurrentBuildNumber",
            data=self._windows_versions.get(version)["CurrentBuildNumber"]
        )

        self.reg_add(
            key="HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
            value="CurrentVersion",
            data=self._windows_versions.get(version)["CurrentVersion"]
        )

    def set_virtual_desktop(self, status: bool, res: str = None):
        '''
        Enable or disable the Wine Virtual Desktop

        Parameters
        ----------
        status : bool
            the Virtual Desktop status
        res : str (optional)
            the resolution to be used (e.g. 800x600) only if status is True
        '''
        if status:
            self.reg_add(
                key="HKEY_CURRENT_USER\\Software\\Wine\\Explorer",
                value="Desktop",
                data="Default"
            )
            self.reg_add(
                key="HKEY_CURRENT_USER\\Software\\Wine\\Explorer\\Desktops",
                value="Default",
                data=res
            )
        else:
            self.reg_delete(
                key="HKEY_CURRENT_USER\\Software\\Wine\\Explorer",
                value="Desktop"
            )

    '''
    Wine DLL overrides management
    '''

    def override_dll(self, name: str, override: int = 0, restore: bool = False):
        '''
        Overriding a DLL in the wineprefix.

        Parameters
        ----------
        name : str
            the name of the DLL
        override : int
            the type of override (default 0:builtin):
            0 (builtin): provided by Wine
            1 (native): provided by Windows
            2 (builtin/native): builtin then native
            3 (native/builtin): native then builtin
        restore : bool (optional)
            restore the override to the initiale state (default False)
        '''

        if override not in self._dll_overrides:
            raise ValueError("Given override type is not supported.")

        if not restore:
            self.reg_add(
                key="HKEY_CURRENT_USER\\Software\\Wine\\DllOverrides",
                value=name,
                data=self._dll_overrides.get(override)
            )
        else:
            self.reg_delete(
                key="HKEY_CURRENT_USER\\Software\\Wine\\DllOverrides",
                value=name
            )
