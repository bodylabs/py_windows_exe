__version__ = '1.0.0'

def running_as_windows_exe():
    import imp
    import sys
    return (
        hasattr(sys, "frozen") # new py2exe
        or hasattr(sys, "importers") # old py2exe
        or imp.is_frozen("__main__") # tools/freeze
    )

def get_main_dir():
    import os
    import sys
    if running_as_windows_exe():
        return os.path.dirname(sys.executable)
    return os.path.dirname(sys.argv[0])
