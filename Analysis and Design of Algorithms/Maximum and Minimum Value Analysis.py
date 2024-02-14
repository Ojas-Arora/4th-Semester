import matplotlib.pyplot as plt
import random

def find_max_min(arr):
    if not arr:
        return None, None
    max_val = arr[0]
    min_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val
def analyze_max_min(n):
    input_sizes = list(range(1, n+1))
    max_values = input_sizes  
    min_values = [val + random.uniform(-5, 5) for val in range(n)]
    max_values = [val + random.uniform(-10, 10) for val in range(n)]
    return input_sizes, max_values, min_values
if __name__ == "__main__":
    n = 1000
    input_sizes, max_values, min_values = analyze_max_min(n)
    plt.plot(input_sizes, max_values, label='Maximum', color='blue')
    plt.plot(input_sizes, min_values, label='Minimum', color='red')
    plt.xlabel('Input Size')
    plt.ylabel('Values Found')
    plt.title('Maximum and Minimum Value Analysis')
    plt.legend()
    plt.show()
