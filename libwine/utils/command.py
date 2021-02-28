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

    Raises
    ------
    Exception
        If the command execution fail.
    '''

    _command = str
    _cwd = "/tmp"

    def __init__(self, command:str, cwd:str=None):
        self._command = command

        if cwd != None:
            self._cwd = cwd

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
        try:
            proc = subprocess.Popen(
                self._command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                cwd=self._cwd
            )
        except OSError:
            raise Exception("Command execution failed.")

        if comunicate:
            return proc.communicate()[0].decode("utf-8")
        
        return proc
    
    def comunicate(self):
        '''
        Execute the command and get the output
        '''
        return self.execute(comunicate=True)