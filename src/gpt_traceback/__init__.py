__version__ = "0.1.0"

import warning

try:
    from .ipython_traceback import *
except ImportError:
    warning.warn("IPython could not be imported, are you in Google Colab?")