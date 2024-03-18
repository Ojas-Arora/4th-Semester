import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate
def shortestPath(graph, source):
    s = {v: False for v in graph.nodes()}
    dist = {v: float('inf') for v in graph.nodes()}
    for v in graph[source]:
        dist[v] = int(graph[source][v]['weight'])
    s[source] = True
    dist[source] = 0
    for i in range(1, len(graph)):
        value = float('inf')
        for j in range(1, len(s)):
            if not s[j] and value >= dist[j]:
                value = dist[j]
                u = j
        s[u] = True
        for w in graph[u]:
            if not s[w] and dist[w] > dist[u] + int(graph[u][w]['weight']):
                dist[w] = dist[u] + int(graph[u][w]['weight'])
    return dist
G = nx.DiGraph()
all_edges = True
while all_edges:
    a = int(input("\nStarting Node of the edge: "))
    b = int(input("Ending Node of the edge: "))
    w = str(input("Enter the cost of the corresponding edge: "))
    G.add_edge(a, b, weight=w)
    ch = input("Do you want to enter another edge?: (y/n) ")
    if ch.lower() == 'n':
        all_edges = False
source = int(input("\nEnter the source vertex: "))
pos = nx.shell_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color="lightpink", node_size=500, font_size=14, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
result = shortestPath(G, source)
table = [[ele, d] for ele, d in result.items()]
print(tabulate(table, headers=["Element", "Distance"], tablefmt='grid'))
