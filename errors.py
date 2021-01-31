class ReaderError(Exception):
    """base exception for the reader library"""
    pass
class CouldNotWrite(ReaderError):
    """raised when reader could not write to a file"""
    pass
class NotAFile(ReaderError):
    """raised when trying to open a directory"""
    pass
class CouldNotOpen(ReaderError):
    """raised when trying to open an unopenable file"""
    pass
class NotValidFilePosition(ReaderError):
    """raised when a seek failed"""
    pass
class CouldNotRead(ReaderError):
    """raised when a read failed"""
    pass
class NotAFilter(ReaderError):
    """raised when a filter does not exist"""
    pass
class ListToShort(ReaderError):
    """raised when a given list is to short"""
    pass
