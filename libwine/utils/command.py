import subprocess

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

    def __init__(self, command:str, cwd:str=None, envs:dict=None):
        self._command = command

        if cwd != None:
            self._cwd = cwd

        if envs != None:
            self._envs = envs

    def execute(self, comunicate:bool=False):
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
        '''
        command = self._command

        if len(self._envs) > 0:
            for e in self._envs:
                command = f"{e}={self._envs[e]} {command}"
        print(command)
        proc = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=self._cwd
        )
        try:
            proc = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                cwd=self._cwd,
                shell=True
            )
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

'''
cmd = Command(
    command="/home/mirko/.local/share/bottles/runners/chardonnay-6.0/bin/wine64 wineboot",
    envs={
        "WINEARCH":"win64",
        "WINEPREFIX": "/home/mirko/test"
    })
print(cmd.comunicate())
'''