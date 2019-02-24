def attrgetter(attr):
    assert "." not in attr
    def _attrgetter(obj):
        return getattr(obj, attr)
    return _attrgetter

class itemgetter:
    def __init__(self, item, *items):
        if not items:
            self._items = (item,)
            def func(obj):
                return obj[item]
            self._call = func
        else:
            self._items = items = (item,) + items
            def func(obj):
                return tuple(obj[i] for i in items)
            self._call = func

    def __call__(self, obj):
        return self._call(obj)

def getitem(a, b):
    return a[b]

def lt(a, b):
    return a < b

def le(a, b):
    return a <= b

def gt(a, b):
    return a > b

def ge(a, b):
    return a >= b

def eq(a, b):
    return a == b

def ne(a, b):
    return a != b

def mod(a, b):
    return a % b

def truediv(a, b):
    return a / b

def floordiv(a, b):
    return a // b

def add(a, b):
    return a + b

def iadd(a, b):
    a += b
    return a

def sub(a, b):
    return a - b

def isub(a, b):
    a -= b
    return a

def mul(a, b):
    return a * b

def imul(a, b):
    a *= b
    return a

def div(a, b):
    return a / b

def idiv(a, b):
    a /= b
    return a

truediv = div
itruediv = idiv

def floordiv(a, b):
    return a // b

def ifloordiv(a, b):
    a //= b
    return a

def mod(a, b):
    return a % b

def imod(a, b):
    a %= b
    return a

def pow(a, b):
    return a ** b

def ipow(a, b):
    a **= b
    return a

def is_(a, b):
    return a is b

def is_not(a, b):
    return a is not b

def and_(a, b):
    return a & b

def iand(a, b):
    a &= b
    return a

def or_(a, b):
    return a | b

def ior(a, b):
    a |= b
    return a

def xor(a, b):
    return a ^ b

def ixor(a, b):
    a ^= b
    return a

def invert(a):
    return ~a

inv = invert

def lshift(a, b):
    return a << b

def ilshift(a, b):
    a <<= b
    return a

def rshift(a, b):
    return a >> b

def irshift(a, b):
    a >>= b
    return a


