
# src/idioms/comprehensions.py
"""
Demonstrates Pythonic idioms:
- Comprehensions (list, set, dict)
- Idiomatic iteration with enumerate and zip
- Tuple unpacking with *rest
Run: python src/idioms/comprehensions.py
"""

# List comprehension: squares of odd numbers
nums = list(range(10))
odd_squares = [n * n for n in nums if n % 2]
print("Odd squares:", odd_squares)

# Set comprehension: unique domains from emails
emails = ['a@example.com', 'b@example.com', 'a@example.com', 'c@example.com']
domains = {email.split('@')[1] for email in emails}
print("Unique domains:", domains)

# Dict comprehension: map names to scores
names = ['Ann', 'Bob', 'Cara']
scores = [90, 82, 77]
score_map = {n: s for n, s in zip(names, scores)}
print("Score map:", score_map)

# enumerate for index-value pairs
for i, name in enumerate(names):
    print(f"{i}: {name}")

# Tuple unpacking with *rest
record = (101, 'Widget', 'Blue', 9.99, 'Extra', 'Unused')
id_, name, color, price, *rest = record
print(f"ID={id_}, Name={name}, Color={color}, Price={price}, Rest={rest}")
