def find_subrectangle(matrix, a, b):
    if not matrix or not matrix[0]:
        return None
    m, n = len(matrix), len(matrix[0])
    sum_matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            sum_matrix[i][j] = matrix[i-1][j-1] + sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1]

    for i in range(m - b + 1):
        for j in range(n - a + 1):
            total = sum_matrix[i+b][j+a] - sum_matrix[i+b][j] - sum_matrix[i][j+a] + sum_matrix[i][j]
            if total == a * b:
                return (i, j)
    return None

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0]
]
a, b = 2, 2

result = find_subrectangle(matrix, a, b)
print("Top-left corner of the rectangle:", result if result else "No such rectangle found")
