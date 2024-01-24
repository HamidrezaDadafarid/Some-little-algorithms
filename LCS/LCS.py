def print_matrix(b, c):
    for i in range(0, len(c)):
        for j in range(0, len(c[i])):
            print(c[i][j], b[i][j], end = '\t')
        print("\n")

def LCS_length(X, Y): # X and Y are two sequences
    m = len(X)
    n = len(Y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [['-' for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (X[i - 1] == Y[j - 1]):
               c[i][j] = (c[i - 1][j - 1] + 1)
               b[i][j] = '↖'
            elif (c[i - 1][j] >= c[i][j - 1]):
                c[i][j] = c[i - 1][j]
                b[i][j] = '↑'
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = '←'
    return b, c

def print_LCS(b, X, m, n):
    if m == 0 or n == 0:
        return
    if b[m][n] == '↖':
        print_LCS(b, X, m - 1, n - 1)
        print(X[m - 1], end = '')
    elif b[m][n] == '↑':
        print_LCS(b, X, m - 1, n)
    else:
        print_LCS(b, X, m, n - 1)



X = '10010101'
Y = '010110110'
b, c = LCS_length(X, Y)
print_matrix(b, c)
print_LCS(b, X, len(X), len(Y))



