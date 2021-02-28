from .wine import Wine

class Proton(Wine):
    '''
    Create a new object of type Proton with all the methods for its management.

    Parameters
    ----------
    winepath : str
        full path to Wine
    wineprefix: str
        full path to your wineprefix
    '''

    _winepath = str
    _wineprefix = str

    def __init__(self, winepath:str, wineprefix:str):
        self._winepath = f"{winepath}/dist"
        self._wineprefix = wineprefix
        pass