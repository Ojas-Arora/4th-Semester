#N-Queen
from tabulate import tabulate
def print_ans(r):
    n = len(r)
    z = []
    for i in r:
        m = [" "] * n
        m[i] = "Q"
        z.append(m)
    print(tabulate(z, tablefmt="grid"))
def place(k, i):
    for j in range(0, k):
        if x[j] == i or abs(x[j] - i) == abs(j - k):
            return False
    return True
def nQueens(k, n):
    for i in range(0, n):
        if place(k-1, i):
            x[k-1] = i
            if k == n:
                print_ans(x)
            else:
                nQueens(k+1, n)
n = int(input("Enter the number of Queens: "))
x = [-1] * n
nQueens(1, n)
