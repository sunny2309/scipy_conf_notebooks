from numba import jit

@jit
def add(a, b):
    for i in range(100):
        c = i
        f = i + 7
        l = c + f
        
    return a + b

add('a', 'b')