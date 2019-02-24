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

_sigs = {}

def signal(n, handler):
    if isinstance(handler, int):
        _sigs[n] = handler
        return signal_i(n, handler)
    import ffi
    cb = ffi.callback("v", handler, "i")
    _sigs[n] = cb
    return signal_p(n, cb)

def getsignal(n):
    return _sigs.get(n, SIG_DFL)

