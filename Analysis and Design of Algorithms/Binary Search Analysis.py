import matplotlib.pyplot as plt
import time

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    steps = 0

    while low <= high:
        mid = (low + high) // 2
        steps += 1

        if arr[mid] == target:
            return steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return steps

def analyze_binary_search(arr_size):
    arr = list(range(arr_size))
    target = arr_size // 2  # Target value is in the middle

    steps_list = []
    for _ in range(100):  # Run the search 100 times
        steps = binary_search(arr, target)
        steps_list.append(steps)

    average_steps = sum(steps_list) / len(steps_list)
    return average_steps

def plot_analysis(arr_sizes):
    average_steps_list = []

    for size in arr_sizes:
        average_steps = analyze_binary_search(size)
        average_steps_list.append(average_steps)

    # Plotting
    plt.plot(arr_sizes, average_steps_list, marker='o')
    plt.title('Binary Search Analysis')
    plt.xlabel('Array Size')
    plt.ylabel('Average Steps')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    array_sizes = [10, 100, 1000, 10000, 100000]
    plot_analysis(array_sizes)
