import matplotlib.pyplot as plt
import numpy as np

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def plot_merge_sort_runtime(arr):
    n = len(arr)
    x = np.arange(n)
    x_interp = np.linspace(0, n - 1, num=n*3)  
    y_interp = np.interp(x_interp, x, arr)     
    y_interp -= np.min(y_interp)  
    plt.plot(x_interp, y_interp, linestyle='-')
    plt.xlabel('Array Size')
    plt.ylabel('Time')
    plt.title('Merge Sort Runtime Analysis')
    plt.show()

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array:", arr)
plot_merge_sort_runtime(arr)
