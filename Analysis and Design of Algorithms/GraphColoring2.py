#Greedy Algorithm Approach
import networkx as nx
import matplotlib.pyplot as plt
def greedy_coloring(G, m):
    colors = {}
    vertices = sorted(G.nodes(), key=lambda x: len(list(G.neighbors(x))), reverse=True)
    for v in vertices:
        used_colors = set(colors.get(neigh, None) for neigh in G.neighbors(v))
        for color in range(1, m + 1):
            if color not in used_colors:
                colors[v] = color
                break
    return colors
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
m = int(input("Enter the number of colors: "))
print("Input Edges:", edges)
print("\nSolutions of the Problem are: ")
colors = greedy_coloring(G, m)
print("Vertex Colors:", colors)
