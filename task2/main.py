from decorators.type_check import type_check
from decorators.cache import cache
from decorators.auth import auth
from decorators.retry import retry

from generators.fibonacci import fibonacci
from generators.filters import gen
from generators.factorials import factorials
from generators.every_n import every_n

from closures.limit_calls import limit_calls
from closures.checker import checker
from closures.template import template
from closures.diff import diff
from closures.counter import count_args


@type_check(int, int)
def add(a, b):
    return a + b


@cache
def slow_sum(a, b):
    return a + b


print("---- DECORATORS ----")
print(add(2, 3))
print(slow_sum(2, 3))
print(slow_sum(2, 3))


print("\n---- GENERATORS ----")
fib = fibonacci()
print(next(fib))

print(list(gen(20)))
print(list(every_n([1, 2, 3, 4, 5, 6], 2)))


print("\n---- CLOSURES ----")
f = limit_calls(3)
print(f())
print(f())
print(f())