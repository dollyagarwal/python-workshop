# Exercises: OOP, Decorators, Type Hints

1. **Class**  
   Implement `User` with fields `id`, `name`, `email`; add `__repr__` and a method `domain()`.

2. **Dataclass**  
   Reimplement `User` with `@dataclass` and type hints; compare ergonomics.

3. **Decorator**  
   Create `@timed` to measure function execution time.

4. **Context Manager**  
   Implement a simple timer context manager using `__enter__`/`__exit__`.

5. **Validation**  
   Use `pydantic` to validate email format (optional if installed).

*Stretch:* Add `__eq__` and hashing to support set operations of `User` objects.
