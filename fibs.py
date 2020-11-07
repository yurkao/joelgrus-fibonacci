from itertools import accumulate, islice, repeat
from typing import Tuple, Generator


def next_fib(prev_res: Tuple[int, int], _) -> Tuple[int, int]:
    """
    Produces next pair of Fibonacci numbers

    :param prev_res: previous pair of Fibonacci numbers (F[N-1], F[N])
    :param _: ignored
    :return: next pair of Fibonacci numbers (F[N], F[N+1])
    """
    return prev_res[-1], prev_res[-1] + prev_res[-2]


def fibonacci_stream():
    """
    Fibonacci numbers generator: produces infinite Fibonacci numbers stream

    >>> list(islice(fibonacci_stream(), 1))
    [1]

    >>> list(islice(fibonacci_stream(), 2))
    [1, 1]

    >>> list(islice(fibonacci_stream(), 3))
    [1, 1, 2]

    >>> list(islice(fibonacci_stream(), 6))
    [1, 1, 2, 3, 5, 8]

    >>> list(islice(fibonacci_stream(), 24))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]


    :return: fibonacci iterable of ints
    :rtype: Generator[int]
    """
    # accumulator acts as recurrent relation handler:
    # 1. applies next_fib on previous pair of Fibonacci numbers and (0, 1)
    # 2. (0, 1) is
    # 2.a. used to calculate aggregation result on first first Fib elem: (0, 1) -> 1
    # 2.b. is ignored on further aggregation calls
    yield from (y for _, y in accumulate(repeat((0, 1)), next_fib))
