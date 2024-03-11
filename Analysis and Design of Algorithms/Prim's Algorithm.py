import networkx as nx
import matplotlib.pyplot as plt
def prims(graph, start):
    mst = []
    visited = []
    min_cost = 0.0
    key = {v: float('inf') for v in graph.nodes()}
    parent = {v: None for v in graph.nodes()}
    key[start] = 0
    while len(visited) < len(graph):
        u = min(key, key=lambda v: key[v] if v not in visited else float('inf'))
        visited.append(u)
        if parent[u] is not None:
            min_cost += int(graph[parent[u]][u]['weight'])
            mst.append([parent[u], u, int(graph[parent[u]][u]['weight'])])
        for v in graph[u]:
            weight = float(graph[u][v]['weight'])
            if v not in visited and weight < key[v]:
                key[v] = weight
                parent[v] = u
    return mst, min_cost
G = nx.Graph()
all_edges = True
while all_edges:
    a = int(input("\nStarting Node of the edge: "))
    b = int(input("Ending Node of the edge: "))
    w = str(input("Enter the cost of the corresponding edge: "))
    G.add_edge(a, b, weight=w)
    ch = input("Do you want to enter another edge?: (y/n) ")
    if ch.lower() == 'n':
        all_edges = False
starting_vertex = int(input("\nEnter the starting vertex: "))
pos = nx.shell_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color="lightpink", node_size=500, font_size=14, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
result = prims(G, starting_vertex)
print("\nThe Minimum Cost of Tree is: " + str(result[1]))
V = nx.Graph()
for edge in result[0]:
    V.add_edge(edge[0], edge[1], weight=edge[2])
pos = nx.shell_layout(V)
edge_labels_mst = nx.get_edge_attributes(V, 'weight')
nx.draw(V, pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=14, font_weight='bold')
nx.draw_networkx_edge_labels(V, pos, edge_labels=edge_labels_mst)
plt.show()
