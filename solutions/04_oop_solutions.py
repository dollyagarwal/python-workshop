
from dataclasses import dataclass
from time import perf_counter
from typing import Callable

class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
    def domain(self) -> str:
        return self.email.split('@')[-1]
    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

@dataclass(eq=True, frozen=False)
class UserDC:
    id: int
    name: str
    email: str
    def domain(self) -> str:
        return self.email.split('@')[-1]

# Decorator
def timed(fn: Callable):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print(f"{fn.__name__} took {end-start:.6f}s")
        return result
    return wrapper

@timed
def work(n: int) -> int:
    return sum(range(n))

# Context manager
class Timer:
    def __enter__(self):
        self.start = perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.end = perf_counter()
        print(f"elapsed: {self.end - self.start:.6f}s")
        return False

# Optional: Pydantic validation
try:
    from pydantic import BaseModel, EmailStr
    class UserModel(BaseModel):
        id: int
        name: str
        email: EmailStr
    u = UserModel(id=1, name='Ann', email='ann@example.com')
    print(u)
except Exception as e:
    print('Pydantic not installed or validation error:', e)

if __name__ == '__main__':
    print(User(1,'Ann','ann@example.com').domain())
    print(UserDC(2,'Bob','bob@example.com').domain())
    work(1000000)
    with Timer():
        work(500000)
