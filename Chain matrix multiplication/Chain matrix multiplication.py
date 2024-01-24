def print_matrix(m, s):
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            print(m[i][j], s[i][j], end = '\t')
        print("\n")

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
    s = [["-" for _ in range(n)] for _ in range(n)]

    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k + 1

    return m, s


p = [5, 4, 6, 2, 7]
m, s = matrix_chain_order(p)
print_matrix(m, s)

