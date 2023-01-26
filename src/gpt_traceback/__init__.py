__version__ = "0.1.0"

import warnings

try:
    from .ipython_traceback import *
except ImportError:
    warnings.warn("IPython could not be imported, are you in Google Colab?")