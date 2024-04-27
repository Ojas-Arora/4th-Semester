#Sliding Window Approach
def sum_of_subsets_sliding_window(w, m):
    start, end, total = 0, 0, 0
    found = False
    while end < len(w):
        total += w[end]
        while total > m and start <= end:
            total -= w[start]
            start += 1
        if total == m:
            found = True
            print("Subset with sum equal to", m, ":", w[start:end + 1])
            total -= w[start]
            start += 1
        end += 1
    if not found:
        print("No subset with sum equal to", m, "exist.")
n = int(input("Enter the total number elements: "))
w = []
for i in range(n):
    j = int(input("Enter the element number " + str(i + 1) + " : "))
    w.append(j)
m = int(input("Enter the desired sum of elements of the Subset : "))
sum_of_subsets_sliding_window(w, m)
