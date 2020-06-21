import numpy as np
import numpy.linalg as la
from io import StringIO


def iter_method(r, L):
    r_next = r
    while True:
        r_prev = r_next
        r_next = L @ r_prev
        if round(la.norm(r_prev - r_next), 2) <= 0.01:
            return r_next


def pagerank(link_matrix, d=0.5):
    n = link_matrix.shape[0]
    r = 100 * np.ones(n) / n
    M = d * link_matrix + (1 - d) / n * np.ones((n, n))
    return iter_method(r, M)


matrix_dimension = int(input('Please enter matrix dimension: '))
websites = input('Input websites: ').split()
print('Enter matrix:')
matrix = [[float(x) for x in input().split(" ")] for x in range(matrix_dimension)]
result = pagerank(np.array(matrix))
query = input('Search query: ')

rs = sorted(tuple(zip(websites, result)), reverse=True)
s = {k: v for k, v in sorted(rs, key=lambda item: round(item[1]), reverse=True)}

print(query)
count = 1
for k, v in s.items():
    if count == 5:
        exit()
    if k != query:
        print(k)
        count += 1
