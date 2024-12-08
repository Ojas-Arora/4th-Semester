#Greedy Knapsack
class Item:
    def __init__(self, profit, weight, num):
        self.profit = profit
        self.weight = weight
        self.num = num
def fractionalKnapsack(m, lst, type):
    if type == 'profit':
        lst.sort(key=lambda x: x.profit, reverse=True)
    elif type == 'weight':
        lst.sort(key=lambda x: x.weight, reverse=True)
    elif type == 'profit by weight':
        lst.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    selected_objects = []
    final_profit = 0.0
    for item in lst:
        if item.weight <= m:
            m -= item.weight
            selected_objects.append(1)
            final_profit += item.profit
        else:
            selected_objects.append(m / item.weight)
            final_profit += item.profit * (m / item.weight)
            break
    return [selected_objects, final_profit]
m = int(input("Enter the size of the Knapsack: "))
lst = []
n = int(input("Enter the number of items: "))
for i in range(n):
    profit = float(input("Enter the profit associated with item {}: ".format(i+1)))
    weight = float(input("Enter the weight of the item: "))
    item = Item(profit, weight, i)
    lst.append(item)
solution1 = fractionalKnapsack(m, lst, 'profit')
print("Total Profit By Greedy On Profit Approach:", solution1[1])
print("Selected items:", solution1[0])
solution2 = fractionalKnapsack(m, lst, 'weight')
print("Total Profit By Greedy On Weight Approach:", solution2[1])
print("Selected items:", solution2[0])
solution3 = fractionalKnapsack(m, lst, 'profit by weight')
print("Total Profit By Greedy On Profit by Weight Approach:", solution3[1])
print("Selected items:", solution3[0])
