__version__ = "0.1.11"

import warnings

try:
    from .ipython_traceback import *
except ImportError:
    warnings.warn("IPython could not be imported, are you in Google Colab?")

def deactivate():
    IPython.get_ipython().set_custom_exc((Exception,),
                                     None)