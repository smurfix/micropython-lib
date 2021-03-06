from urandom import *


def randrange(start, stop=None):
    if stop is None:
        stop = start
        start = 0
    upper = stop - start
    bits = 0
    pwr2 = 1
    while upper > pwr2:
        pwr2 <<= 1
        bits += 1
    while True:
        r = getrandbits(bits)
        if r < upper:
            break
    return r + start

def randint(start, stop):
    return randrange(start, stop + 1)

uniform = randint

def shuffle(seq):
    l = len(seq)
    if l < 2:
        return
    for i in range(l):
        j = randrange(l)
        seq[i], seq[j] = seq[j], seq[i]

class Random:
    @staticmethod
    def randrange(start, stop=None):
        return randrange(start, stop)

    @staticmethod
    def randint(start, stop):
        return randint(start, stop)

    uniform = randint

    @staticmethod
    def shuffle(seq):
        return shuffle(seq)

