
from itertools import groupby

# Comprehension: even squares
evens_squared = [x*x for x in [1,2,3,4,5] if x % 2 == 0]
print(evens_squared)

# zip: combine names and scores
names = ['Ann', 'Bob', 'Cara']
scores = [90, 82, 77]
ns = {n: s for n, s in zip(names, scores)}
print(ns)

# groupby: aggregate by key
records = [
    {'dept': 'A', 'val': 1},
    {'dept': 'A', 'val': 2},
    {'dept': 'B', 'val': 3}
]
records.sort(key=lambda r: r['dept'])
for dept, group in groupby(records, key=lambda r: r['dept']):
    total = sum(r['val'] for r in group)
    print(dept, total)

# Context manager with pathlib
from pathlib import Path
p = Path('data.txt')
p.write_text('  line1\nline2  \n  line3  ')
with p.open() as src, open('clean.txt', 'w') as dst:
    for line in src:
        dst.write(line.strip() + '\n')