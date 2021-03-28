from typing import NewType

from .exceptions import ProtectedProcess

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
    wine: Wine
        the Wine object
    '''

    pid = int
    name = str
    parent_pid = str
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
        str:
            a valid process ID as hex
        '''
        if pid is not None:
            return f"0x{pid}"

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
        if self.name not in self._protected:
            command = f"winedbg << END_OF_INPUTS\n\
                attach {self.pid}\n\
                kill\n\
                quit\n\
                END_OF_INPUTS"
            self.wine.execute(command=command, comunicate=True)
        else:
            raise ProtectedProcess(self.name)

    def update(self):
        '''
        Update process status/data.
        '''
        # TODO: update process info by pid
        return
