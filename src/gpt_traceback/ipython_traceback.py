import IPython, inspect
from IPython.core import ultratb
import traceback
from .prompt import predict_prompt

def exception_hook(exc_type, exc_value, exc_traceback):
    error = "Hello stack overflow, I need help I ran into the following error in my notebook:\n"
    exception = "\n".join(traceback.format_exception_only(exc_type, exc_value))
    error += "Exception type and exception value:\n" + exception + "\n"
    print(exception)
    traceback_str ="\n".join(traceback.format_tb(exc_traceback, 2))
    error += "Traceback (2):\n" + traceback_str + "\n"
    print(traceback_str)
    #print("\n".join(IPython.get_ipython().history_manager.get_range(-1,0)))
    # TODO: print the cell where the error happened and the previous cells of it
    last_tb = exc_traceback
    while last_tb.tb_next:
        last_tb = last_tb.tb_next
    f = last_tb.tb_frame
    lineno = last_tb.tb_lineno
    co = f.f_code
    filename = co.co_filename
    function_name = co.co_name
    source = inspect.getsource(f)
    print(f'File Name: {filename}, Function Name: {function_name}, Line No: {lineno}')
    print(source)
    error += "Source of cell:\n" + source + "\nThe solution to the exception is:"
    print("predicting exception...")
    print("...")
    print(predict_prompt(error))
    #linecache.checkcache(filename)
    #line = linecache.getline(filename, lineno, f.f_globals)
    #print(f'File Name: {filename}, Function Name: {function_name}, Line No: {lineno}, Line Content: {line.strip()}')

def custom_exc(shell, etype, evalue, tb, tb_offset=None):
  lshell = shell
  ltb_offset = tb_offset
  return exception_hook(etype, evalue, tb)
  


IPython.get_ipython().set_custom_exc((Exception,),
                                     custom_exc)