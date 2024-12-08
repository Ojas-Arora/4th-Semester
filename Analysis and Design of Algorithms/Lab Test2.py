#Lab Test 2
def min_pencils_needed(ranks):
    if not ranks:
        return 0   
    n = len(ranks)
    pencils = [1] * n  
    for i in range(1, n):
        if ranks[i] > ranks[i - 1]: 
            pencils[i] = pencils[i - 1] + 1
    
    for i in range(n - 2, -1, -1):
        if ranks[i] > ranks[i + 1]:    
            pencils[i] = max(pencils[i], pencils[i + 1] + 1) 
    return sum(pencils)
n = int(input("Enter the number of kids in the queue: "))
ranks = []
for i in range(n):
    rank = int(input(f"Enter the rank of kid {i+1}: "))
    ranks.append(rank)
print("Minimum number of pencils needed:", min_pencils_needed(ranks))
