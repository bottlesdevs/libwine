import subprocess
from os import path, mkdir, environ


class Command:
    '''
    Create a new object of type Command that can be used to run commands.

    Parameters
    ----------
    command : str
        the command to be executed
    cwd: str, optional
        full path to the working directory
    envs: dict, optional
        dict of environment variables to pass on the execution

    Raises
    ------
    Exception
        If the command execution fail.
    '''

    _command = str
    _cwd = "/tmp"
    _envs = {}

    def __init__(self, command: str, cwd: str = None, envs: dict = None):
        self._command = command
        self._envs = environ.copy()
        self._envs["PATH"] = "/usr/sbin:/sbin:" + self._envs["PATH"]

        if cwd is not None:
            if not path.exists(cwd):
                try:
                    mkdir(cwd)
                    self._cwd = cwd
                except PermissionError:  # the /tmp path will be used
                    pass

        if envs is not None:
            self._envs = {**self._envs, **envs}

    def execute(self, comunicate: bool = False):
        '''
        Execute the command.

        Parameters
        ----------
        comunicate : bool, optional
            to get the output of the command (default is False)

        Returns
        -------
        subprocess.Popen object
            the subprocess object
        str
            the command output if comunicate is set to True
        bool
            False if the command fail on execution

        Raises
        -------
        Exception
            if command not found
        '''
        command = self._command

        command = command.split(" ")
        try:
            proc = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                cwd=self._cwd,
                env=self._envs
            )
        except FileNotFoundError:
            raise Exception("Command not found")
        except OSError:
            return False

        if comunicate:
            return proc.communicate()[0].decode("utf-8")

        return proc

    def comunicate(self):
        '''
        Execute the command and get the output
        '''
        return self.execute(comunicate=True)
