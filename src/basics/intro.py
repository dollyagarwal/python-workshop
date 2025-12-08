
# src/basics/intro.py
"""
Basics: Demonstrates Python's dynamic typing, f-strings, and simple functions.

- Dynamic typing
- f-strings
- Basic functions (with and without type hints)
- Truthy/falsy checks
- A quick loop

Run this file with: python src/basics/intro.py
"""

# Dynamic typing: variables can change type
name = "Team"
age = 30
pi = 3.14159

# f-string for formatted output
print(f"Hello {name}, age={age}, pi≈{pi:.2f}")

# Simple function without type hints
def add(a, b):
    return a + b

print("Sum of 2 and 3:", add(2, 3))

# Function with type hints (optional)
def greet(user: str) -> str:
    return f"Welcome, {user}!"

print(greet("Python Learner"))

# Demonstrate None and truthy/falsy values
value = None
if not value:
    print("Value is None or falsy")

# Quick loop example
for i in range(3):
    print(f"Loop iteration {i}")
