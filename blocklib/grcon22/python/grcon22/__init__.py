
import os

try:
    from .grcon22_python import *
except ImportError:
    dirname, filename = os.path.split(os.path.abspath(__file__))
    __path__.append(os.path.join(dirname, "bindings"))
    from .grcon22_python import *

# Because we have "numpy" implementations of blocks in this module
from . import numpy