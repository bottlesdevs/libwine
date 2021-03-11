class ProtectedProcess(Exception):
    '''
    Raised when trying to kill a protected Wine process.

    Parameters
    ----------
    name : str
        the process name
    '''

    def __init__(self, name):
        self.message = f"Cannot kill the protected process: {name}"
        super().__init__(self.message)
