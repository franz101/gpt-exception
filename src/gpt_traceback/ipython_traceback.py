import IPython, inspect
import textwrap
from IPython.core import ultratb
import traceback
from .prompt import predict_prompt
from .print_exception import print_exception

def exception_hook(exc_type, exc_value, exc_traceback):
    last_tb = exc_traceback
    while last_tb.tb_next:
        last_tb = last_tb.tb_next
    source = inspect.getsource(last_tb.tb_frame)
    print_exception(exc_type, exc_value, last_tb)
    error = "Hello stack overflow, I need help I ran into the following error in my notebook:\n"
    exception = "\n".join(traceback.format_exception_only(exc_type, exc_value))
    error += "Exception type and exception value:\n" + exception + "\n"
    traceback_str ="\n".join(traceback.format_tb(exc_traceback, 2))
    error += "Traceback (2):\n" + traceback_str + "\n"
    error += "Source of cell:\n" + source + "\nThe solution to the exception is:"
    print("Loading answer:")
    print("...")
    formatted_string = textwrap.wrap(predict_prompt(error), width=60)
    print("\n".join(formatted_string))
    
def custom_exc(shell, etype, evalue, tb, tb_offset=None):
  return exception_hook(etype, evalue, tb)
  


IPython.get_ipython().set_custom_exc((Exception,),
                                     custom_exc)