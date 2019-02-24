import ffilib


SIG_DFL = 0
SIG_IGN = 1

SIGINT = 2
SIGPIPE = 13
SIGTERM = 15

default_int_handler = SIG_IGN

libc = ffilib.libc()

signal_i = libc.func("i", "signal", "ii")
signal_p = libc.func("i", "signal", "ip")

def signal(n, handler):
    if isinstance(handler, int):
        return signal_i(n, handler)
    import ffi
    cb = ffi.callback("v", handler, "i")
    return signal_p(n, cb)
