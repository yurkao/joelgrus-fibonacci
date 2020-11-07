# joelgrus-fibonacci
Based on Joel Grus functional implementation of Fibonacci numbers. See
1. https://joelgrus.com/2015/07/07/haskell-style-fibonacci-in-python/
2. https://youtu.be/ThS4juptJjQ?t=919

This is more Pythonic and a bit faster way to implement fibonacci numbers generator: no need to use overkill "iterate" function from https://youtu.be/ThS4juptJjQ?t=600
since f(x) , f(f(x), f(f(f(x)), ...) is recurrent relation which is already implemented by python's [itertools.accumulate](https://docs.python.org/3/library/itertools.html#itertools.accumulate)
