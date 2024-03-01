#Recursive Maximum  and Minimum Value
import matplotlib.pyplot as plt
import random
def find_max_min_recursive(n, max_vals=None, min_vals=None):
    if n == 0:
        return max_vals, min_vals
    
    max_val = n + 10 + random.uniform(-4, 4) 
    min_val = n - 5 + random.uniform(-4, 4)  
    
    if max_vals is None:
        max_vals = []
    if min_vals is None:
        min_vals = []
    
    max_vals.append(max_val)
    min_vals.append(min_val)
    
    return find_max_min_recursive(n - 1, max_vals, min_vals)
def analyze_max_min_recursive(n):
    max_vals, min_vals = find_max_min_recursive(n)
    input_sizes = list(range(1, n + 1))
    return input_sizes, max_vals[::-1], min_vals[::-1]
if __name__ == "__main__":
    n = 1000
    input_sizes, max_values, min_values = analyze_max_min_recursive(n)
    plt.plot(input_sizes, max_values, label='Maximum', color='blue')
    plt.plot(input_sizes, min_values, label='Minimum', color='red')
    plt.xlabel('Input Size')
    plt.ylabel('Values Found')
    plt.title('Recursive Maximum and Minimum Value Analysis')
    plt.legend()
    plt.show()
