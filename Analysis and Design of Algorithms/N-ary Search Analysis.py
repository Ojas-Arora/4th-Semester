# N ary search
import random
import time
import csv
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel('Value of N')
ax.set_ylabel('Time in seconds')
def binarySearch(arr, L, r, x):
    if r >= L:
        mid = L + (r - L) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, L, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1
def linear_search(List, n):
    for i in range(len(List)):
        if List[i] == n:
            return i
    return -1
def n_ary(arr, cuts, start_Loc, end_Loc, key):
    N = end_Loc - start_Loc
    cut_loc = []

    if N < (cuts + 1):
        k = binarySearch(arr, start_Loc, end_Loc, key)
        return k
    else:
        for i in range(1, cuts + 1):
            cut_loc.append(((i * N) // (cuts + 1)) + start_Loc)

        for j in range(0, cuts):
            if key == arr[cut_loc[j]]:
                return cut_loc[j]
            if key < arr[cut_loc[j]]:
                return n_ary(arr, cuts, start_Loc, cut_loc[j], key)
            start_Loc = cut_loc[j]  # Moved this line here
            if (j + 1) == cuts and key > arr[cut_loc[j]]:
                return n_ary(arr, cuts, cut_loc[j], end_Loc, key)
time_arr = []
N = []
file = "data.csv"
fields = ['No. of cuts', 'time_lapsed', 'Value_of_i']

with open(file, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    cuts = [2, 3, 5, 7, 9, 11, 15, 17]
    num = 10000

    for i in cuts:
        time_lapse = 0
        for j in range(1, 1000):
            l = random.sample(range(1, num + (num // 5)), num)
            l.sort()
            k = random.sample(range(1, num + (num // 5)), 1)
            start = time.time()
            val = n_ary(l, i, 0, len(l) - 1, k[0])
            stop = time.time()
            time_lapse += (stop - start)
            rows = [str(i), str(time_lapse), str(val)]
            csvwriter.writerow(rows)
        time_lapsel = time_lapse / 1000
        time_arr.append(time_lapsel)
        N.append(i)
ax.plot(N, time_arr)
plt.show()
