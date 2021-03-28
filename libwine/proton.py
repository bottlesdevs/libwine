from .wine import Wine


class Proton(Wine):
    '''
    Create a new object of type Proton with all the methods for its management.

    Parameters
    ----------
    protonpath : str
        full path to Proton
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

    def __init__(self, protonpath: str, wineprefix: str, verbose: int = 0):
        self._winepath = f"{protonpath}/dist"
        self._wineprefix = wineprefix

        if verbose in self._verbose_levels:
            self._verbose = verbose

        if not self.validate_winepath():
            raise ValueError(
                "Given protonpath doesn't seem a valid Proton path.")
