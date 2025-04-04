from .core.engine import Engine

# create the default instance
_instance = Engine()

# make the package itself behave like an instance
def __getattr__(name):
    return getattr(_instance, name)

def __setattr__(name, value):
    return setattr(_instance, name, value)

def __dir__():
    return dir(_instance)

# replace the module import with the instance
from sys import modules
modules[__name__] = _instance

# all this converts the import from a module to an interactive class instance
