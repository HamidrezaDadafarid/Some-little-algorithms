def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

def knapsack(w, v, n, W):
    V = [[0] * (W + 1) for i in range (n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if (i == 0 or j == 0):
                V[i][j] == 0
            elif (w[i - 1] <= j):
                V[i][j] = max(V[i - 1][j], v[i - 1] + V[i - 1][j -  w[i - 1]])
            else:
                V[i][j] = V[i - 1][j] 
    print_matrix(V)


w = [5, 4, 6, 3]
v = [10, 40, 30, 50]
n = len(w)
W = 10
knapsack(w, v, n, W)


