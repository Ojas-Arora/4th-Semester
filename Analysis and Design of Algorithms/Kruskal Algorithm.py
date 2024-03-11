import networkx as nx
import matplotlib.pyplot as plt

def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]

def union(root1, root2, parent, rank):
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        rank[root2] += 1

def kruskal(graph):
    edges = []
    for u in graph:
        for v in graph[u]:
            edges.append([u, v, int(graph[u][v]['weight'])])
    edges.sort(key=lambda x: x[2])
    
    mst = []
    vertices = []
    min_cost = 0.0
    parent = {v: int(v) for v in graph}
    rank = {v: 0 for v in graph}
    
    for edge in edges:
        u, v, weight = edge
        root1 = find(parent, u)
        root2 = find(parent, v)
        if root1 != root2:
            mst.append([u, v, weight])
            min_cost += weight
            union(root1, root2, parent, rank)
            vertices.append(u)
            vertices.append(v)
    
    return mst, min_cost

G = nx.Graph()
all_edges = True
while all_edges:
    a = int(input("\nStarting Node of the edge: "))
    b = int(input("Ending Node of the edge: "))
    w = input("Enter the cost of the corresponding edge: ")
    G.add_edge(a, b, weight=w)
    ch = input("Do you want to enter another edge?: (y/n) ")
    if ch.lower() == 'n':
        all_edges = False

pos = nx.shell_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color="lightpink", node_size=500, font_size=14, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

result = kruskal(G)
print("The Minimum Cost of Tree is: " + str(result[1]))

V = nx.Graph()
for edge in result[0]:
    V.add_edge(edge[0], edge[1], weight=edge[2])

pos = nx.shell_layout(V)
edge_labels_mst = nx.get_edge_attributes(V, 'weight')
nx.draw(V, pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=14, font_weight='bold')
nx.draw_networkx_edge_labels(V, pos, edge_labels=edge_labels_mst)
plt.show()
