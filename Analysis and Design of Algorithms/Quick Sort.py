#Quick
import matplotlib.pyplot as plt
import numpy as np
import time
import random
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
def plot_runtime_analysis(arr_sizes, runtimes):
    plt.plot(arr_sizes, runtimes, linestyle='-')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Quick Sort Runtime Analysis')
    plt.show()
def benchmark_quick_sort(arr_sizes):
    runtimes = []
    for size in arr_sizes:
        num_list = [random.randint(1, 1000) for _ in range(size)]
        start_time = time.time()
        quick_sort(num_list, 0, len(num_list) - 1)
        end_time = time.time()
        runtimes.append(end_time - start_time)
    return runtimes
arr_sizes = np.arange(1000, 10001, 1000)
runtimes = benchmark_quick_sort(arr_sizes)
plot_runtime_analysis(arr_sizes, runtimes)
example_array = [12, 56, 78, 3, 45, 8, 31, 90, 27, 14]
quick_sort(example_array, 0, len(example_array) - 1)
print("Sorted array:", example_array)
