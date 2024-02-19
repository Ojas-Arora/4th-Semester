import numpy as np
import timeit
import matplotlib.pyplot as plt
def simple_matrix_multiply(matrix1, matrix2):
    n = len(matrix1)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
def strassen_matrix_multiply(matrix1, matrix2, threshold=64):  
    def split_matrix(matrix):
        n = len(matrix)
        n2 = n // 2
        a11 = [[matrix[i][j] for j in range(n2)] for i in range(n2)]
        a12 = [[matrix[i][j] for j in range(n2, n)] for i in range(n2)]
        a21 = [[matrix[i][j] for j in range(n2)] for i in range(n2, n)]
        a22 = [[matrix[i][j] for j in range(n2, n)] for i in range(n2, n)]
        return a11, a12, a21, a22
    def add_matrices(matrix1, matrix2):
        n = len(matrix1)
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        return result
    def subtract_matrices(matrix1, matrix2):
        n = len(matrix1)
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = matrix1[i][j] - matrix2[i][j]
        return result
    def strassen_recursive(matrix1, matrix2):
        if len(matrix1) <= threshold:
            return simple_matrix_multiply(matrix1, matrix2)
        a11, a12, a21, a22 = split_matrix(matrix1)
        b11, b12, b21, b22 = split_matrix(matrix2)
        p1 = strassen_recursive(a11, subtract_matrices(b12, b22))
        p2 = strassen_recursive(add_matrices(a11, a12), b22)
        p3 = strassen_recursive(add_matrices(a21, a22), b11)
        p4 = strassen_recursive(a22, subtract_matrices(b21, b11))
        p5 = strassen_recursive(add_matrices(a11, a22), add_matrices(b11, b22))
        p6 = strassen_recursive(subtract_matrices(a12, a22), add_matrices(b21, b22))
        p7 = strassen_recursive(subtract_matrices(a11, a21), add_matrices(b11, b12))
        c11 = add_matrices(subtract_matrices(add_matrices(p5, p4), p2), p6)
        c12 = add_matrices(p1, p2)
        c21 = add_matrices(p3, p4)
        c22 = subtract_matrices(subtract_matrices(add_matrices(p5, p1), p3), p7)
        result = [[0 for _ in range(len(c11) * 2)] for _ in range(len(c11) * 2)]
        for i in range(len(c11)):
            for j in range(len(c11)):
                result[i][j] = c11[i][j]
                result[i][j + len(c11)] = c12[i][j]
                result[i + len(c11)][j] = c21[i][j]
                result[i + len(c11)][j + len(c11)] = c22[i][j]
        return result
    return strassen_recursive(matrix1, matrix2)
def generate_random_matrix(size):
    return np.random.randint(10, size=(size, size))
def time_matrix_multiplication(matrix_multiply_func, size):
    matrix1 = generate_random_matrix(size)
    matrix2 = generate_random_matrix(size)
    start_time = timeit.default_timer()
    matrix_multiply_func(matrix1, matrix2)
    end_time = timeit.default_timer()
    return end_time - start_time
sizes = [2, 4, 8, 16, 32, 64, 128]  
simple_times = [time_matrix_multiplication(simple_matrix_multiply, size) for size in sizes]
strassen_times = [time_matrix_multiplication(lambda x, y: strassen_matrix_multiply(x, y, threshold=32), size) for size in sizes]
plt.figure(figsize=(10, 5))
plt.plot(sizes, simple_times, label='Simple Matrix Multiplication')
plt.xlabel('Matrix Size')
plt.ylabel('Time (seconds)')
plt.title('Performance of Simple Matrix Multiplication')
plt.legend()
plt.grid(True)
plt.ylim(min(simple_times + strassen_times), max(simple_times + strassen_times)) 
plt.show()
plt.figure(figsize=(10, 5))
plt.plot(sizes, strassen_times, label="Strassen's Matrix Multiplication")
plt.xlabel('Matrix Size')
plt.ylabel('Time (seconds)')
plt.title("Performance of Strassen's Matrix Multiplication")
plt.legend()
plt.grid(True)
plt.ylim(min(simple_times + strassen_times), max(simple_times + strassen_times))  
plt.show()
plt.figure(figsize=(10, 5))
plt.plot(sizes, simple_times, label='Simple Matrix Multiplication')
plt.plot(sizes, strassen_times, label="Strassen's Matrix Multiplication")
plt.xlabel('Matrix Size')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Matrix Multiplication Algorithms')
plt.legend()
plt.grid(True)
plt.ylim(min(simple_times + strassen_times), max(simple_times + strassen_times))  
plt.show()
