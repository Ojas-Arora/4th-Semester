#Backtracking Approach
import networkx as nx
import matplotlib.pyplot as plt

def next_value(k):
    while True:
        x[k] = (x[k] + 1) % (m + 1)
        if x[k] == 0:
            return
        j = 0
        while j < len(G):
            if A[k][j] != 0 and x[k] == x[j]:
                break
            j += 1
        if j == len(G):
            return
def m_coloring(k):
    solution_found = False  # Flag to track if a valid solution is found
    while True:
        next_value(k)
        if x[k] == 0:
            if k == len(G) - 1:
                solution_found = True
                print("Solution:", x)
                print("Edges:", edges)
            return
        if k == len(G) - 1 and not solution_found:
            print("No valid coloring solution exists.")

G = nx.Graph()
edges = []
all_edges = True
while all_edges:
    a = int(input("\nStarting Node of the edge: "))
    b = int(input("Ending Node of the edge: "))
    G.add_edge(a, b)
    edges.append((a, b))
    ch = input("Do you want to enter another edge?: (y/n) ")
    if ch.lower() == 'n':
        all_edges = False

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightpink",
        node_size=500, font_size=14, font_weight='bold')
plt.show()

A = nx.to_numpy_array(G)
x = [0] * len(G)
m = int(input("Enter the number of colors: "))

print("Input Edges:", edges)
print("\nSolutions of the Problem are: ")
m_coloring(0)

