def factorial(n):
    if (n == 0 or n == 1):
        return 1
    return n * factorial(n - 1)

def binomial_coefficient(n, k):
    if (k > n - k):
        k = n - k
    return factorial(n) // (factorial(k) * factorial(n - k))

def catalan(n):
    return binomial_coefficient(2 * n, n) // (n + 1)

def count_BST(n):
    return catalan(n)

def count_BT(n):
    return catalan(n) * factorial(n)

n = int(input("Please enter the number of nodes: "))
print(f"Total number of BSTs with {n} nodes is: {count_BST(n)}")
print(f"Total number of BTs with {n} nodes is: {count_BT(n)}")