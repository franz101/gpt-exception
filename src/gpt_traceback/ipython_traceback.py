import IPython, inspect
from IPython.core import ultratb
import traceback
from .prompt import predict_prompt
from .print_exception import print_exception
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter


def exception_hook(exc_type, exc_value, exc_traceback):
    last_tb = exc_traceback
    while last_tb.tb_next:
        last_tb = last_tb.tb_next
    source = inspect.getsource(last_tb.tb_frame)
    print_exception(exc_type, exc_value, last_tb)
    error = "##### Fix exception from the code below\n"
    error += source + "\n"
    exception = "\n".join(traceback.format_exception_only(exc_type, exc_value))
    error += "\"\"\"Caused this exception type and exception value: " + exception + "\n"
    traceback_str ="\n".join(traceback.format_tb(exc_traceback, 2))
    error += "With the follwoing traceback:" + traceback_str + "\"\"\"\n### Fixed Python\n"
    print("Loading answer:")
    print("...")
    code = predict_prompt(error)
    print(highlight(code, PythonLexer(), TerminalFormatter()))
    
def custom_exc(shell, etype, evalue, tb, tb_offset=None):
  return exception_hook(etype, evalue, tb)
  
def init_exception_hook():
  IPython.get_ipython().set_custom_exc((Exception,),
                                     custom_exc)

init_exception_hook()