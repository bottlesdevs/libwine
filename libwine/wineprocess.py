from typing import NewType

Wine = NewType('Wine', object)


class WineProcess:
    '''
    Create a new object of type WineProcess with all the methods for its management.

    Parameters
    ----------
    pid : str
        the process id
    name: str
        the process name (command)
    parent_pid: str (optional)
        the parent process id
    cpu: str (not implemented)
        the cpu used by the process
    memory: str (not implemented)
        the memory used by the process
    start: str (not implemented)
        the process start date/time
    wine: Wine
        the Wine object
    '''

    pid = int
    name = str
    parent_pid = str
    # cpu = int
    # memory = int
    # start = str
    wine = Wine

    _protected = [
        "explorer.exe",
        "services.exe",
        "rpcss.exe",
        "svchost.exe",
        "winedevice.exe",
        "plugplay.exe"
        "winedbg.exe",
        "conhost.exe"
    ]

    def __init__(self, pid: str, name: str, wine: Wine, parent_pid: str = None):
        self.pid = self._pid(pid)
        self.name = name
        self.parent_pid = self._pid(parent_pid)
        # self.cpu = self._cpu_usage(cpu)
        # self.memory = self._memory_usage(memory)
        # self.start = start
        self.wine = wine

    '''
    Data check and assignment
    '''

    def _pid(self, pid: str):
        '''
        Validate the process ID.

        Parameters
        ----------
        pid : str
            the process ID as string

        Return
        ----------
        int:
            a valid process ID as integer
        '''
        if pid != None:
            return int(f"0x{pid}", 16)

    def _cpu_usage(self, cpu: str):
        '''
        Get CPU usage as percentage.

        Parameters
        ----------
        cpu : str
            the CPU percentage used by the process as string

        Return
        ----------
        int:
            a valid CPU percentage usage as integer (100 = 1)
        '''
        # TODO: calculate cpu percentage
        return int(cpu)

    def _memory_usage(self, memory: str):
        '''
        Get memory usage as percentage.

        Parameters
        ----------
        memory : str
            the memory percentage used by the process as string

        Return
        ----------
        int:
            a valid memory percentage usage as integer (100 = 1)
        '''
        # TODO: calculate memory percentage
        return int(memory)

    '''
    Process management
    '''

    def kill(self):
        '''
        Kill the process.
        '''
        # TODO:
        # run winedbg
        # attach self.pid (converted from hexadecimal to decimal)
        # kill
        # quit
        # e.g. wine.execute(..)
        if self.name not in self._protected:
            self.wine(
                command="",
            )
        else:
            raise Exception("Cannot kill protected process.")

    def update(self):
        '''
        Update process status/data.
        '''
        # TODO: update process info by pid
        return
