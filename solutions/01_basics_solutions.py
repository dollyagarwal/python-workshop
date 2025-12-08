
from typing import Optional

def grade(score: int) -> str:
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'

def fizzbuzz(n: int = 20) -> None:
    for i in range(1, n+1):
        out = ''
        if i % 3 == 0: out += 'Fizz'
        if i % 5 == 0: out += 'Buzz'
        print(out or i)

def repeat(s: str, times: int = 2, sep: str = '-') -> str:
    return sep.join([s] * times)

def safe_div(a: float, b: float) -> Optional[float]:
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None

if __name__ == '__main__':
    print(grade(88))
    fizzbuzz(16)
    print(repeat('go', times=3, sep=':'))
    print(safe_div(10, 2), safe_div(10, 0), safe_div('x', 2))
