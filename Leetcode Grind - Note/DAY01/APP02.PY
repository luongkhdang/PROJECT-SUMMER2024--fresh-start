import numpy as np

def matrix_mult(A, B):
    return np.dot(A, B)

def matrix_pow(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        half_pow = matrix_pow(A, n // 2)
        return matrix_mult(half_pow, half_pow)
    else:
        return matrix_mult(A, matrix_pow(A, n - 1))

def fibonacci_matrix(n):
    if n == 0:
        return 0
    A = np.array([[1, 1], [1, 0]], dtype=np.int64)
    result = matrix_pow(A, n - 1)
    return result[0][0]

# Example usage:
n = 5
print(f"The {n}-th Fibonacci number is: {fibonacci_matrix(n)}")