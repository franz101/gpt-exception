from rich.traceback import  Traceback
from rich.console import Console

console = Console()

def print_exception(exc_type, exc_value, exc_traceback):
    tb_offset = 0
    ltb = exc_traceback
    for _ in range(tb_offset):
        if ltb is None:
            break
        ltb = ltb.tb_next
    locals_hide_sunder = None
    locals_hide_sunder = (
        True
        if (console.is_jupyter and locals_hide_sunder is None)
        else locals_hide_sunder
    )
    traceback_exception = Traceback.from_exception(
                exc_type,
                exc_value,
                exc_traceback,
                width = 100,
    extra_lines = 3,
    theme= None,
    word_wrap = False,
    show_locals =  False,
    locals_max_length =  10,
    locals_max_string =  80,
    locals_hide_dunder =  True,
    locals_hide_sunder =  locals_hide_sunder,
    indent_guides =  True,
    suppress =   (),
    max_frames =  100,
            )
    console.print(
            traceback_exception
        )