#DynamicProgramming Approach
def sum_of_subsets_dp(w, m):
    n = len(w)
    total_sum = sum(map(abs, w))
    dp = [[False] * (total_sum + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for j in range(total_sum + 1):
            if j >= abs(w[i - 1]):
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - abs(w[i - 1])]
            else:
                dp[i][j] = dp[i - 1][j]
    if not dp[n][abs(m)]:
        print("No subset with the sum", m)
        return
    subset = []
    i, j = n, abs(m)
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            subset.append(w[i - 1])
            j -= abs(w[i - 1])
        i -= 1
    print("Subset with the sum", m, ":", subset)
n = int(input("Enter the total number elements: "))
w = []
for i in range(n):
    j = int(input("Enter the element number " + str(i + 1) + " : "))
    w.append(j)
m = int(input("Enter the desired sum of elements of the Subset : "))
sum_of_subsets_dp(w, m)
