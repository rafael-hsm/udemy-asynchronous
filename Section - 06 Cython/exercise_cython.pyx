# import math


# def compute(end, start=1):
#     pos = start
#     factor = 1000 * 1000
#     while pos < end:
#         pos += 1
#         math.sqrt((pos - factor) * (pos - factor))

import cython
from libc.math cimport sqrt

def compute(end: cython.int, start: cython.int = 1):
    pos: cython.int = start
    factor: cython.int = 1000 * 1000

    with nogil:
        while pos < end:
            pos += 1
            sqrt((pos - factor) * (pos - factor))
