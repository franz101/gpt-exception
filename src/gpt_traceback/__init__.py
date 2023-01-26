__version__ = "0.1.21"

import warnings
from getpass import getpass
import os

try:
    from .ipython_traceback import *
    apiKey = os.environ.get("OPENAI_API_KEY")
    if apiKey is None:
        print("""Api Key is missing. Head over to:
https://beta.openai.com/account/api-keys
Please enter OPENAI API KEY:""")
        apiKey = getpass()
        apiKey = apiKey.strip()
        assert "sk-" in apiKey, "API Key needs to start with sk-..."
        os.environ["OPENAI_API_KEY"] = apiKey

except ImportError:
    warnings.warn("IPython could not be imported, are you in Google Colab?")

def init():
    try:
        from .ipython_traceback import init_exception_hook
        init_exception_hook()
    except ImportError:
        warnings.warn("IPython could not be imported, are you in Google Colab?")


def deactivate():
    IPython.get_ipython().set_custom_exc((Exception,),
                                     None)

def change_model(model="code-davinci-002"):
    os.environ["OPENAI_MODEL"] = model