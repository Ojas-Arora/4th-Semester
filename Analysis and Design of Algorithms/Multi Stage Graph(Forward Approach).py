#Multistage Graph
import matplotlib.pyplot as plt
import networkx as nx
def forward_approach(graph, n):
    forward_cost = [0] * n
    forward_path = [0] * n
    forward_cost[0] = 0.0
    for j in range(1, n):
        minimum = float('inf')
        for r in range(j):
            if graph[r][j] != 0 and graph[r][j] + forward_cost[r] < minimum:
                minimum = graph[r][j] + forward_cost[r]
                forward_path[j] = r
                forward_cost[j] = minimum
    forward_paths = [n]
    current_node = forward_path[n - 1]
    while current_node != 0:
        forward_paths.insert(0, current_node)
        current_node = forward_path[current_node]
    forward_paths.insert(0, 0)
    return forward_cost[n - 1], forward_paths
def plot_graph(graph, forward_paths, edge_colors, edge_widths):
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color="lightpink",
            node_size=500, font_size=14, font_weight='bold')
    nx.draw_networkx_edges(graph, pos, edge_color=edge_colors, width=edge_widths)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.show()
G = nx.DiGraph()
all_edges = True
while all_edges:
    a = int(input("\nStarting Node of the edge: "))
    b = int(input("Ending Node of the edge: "))
    w = int(input("Enter the cost of the corresponding edge: "))
    G.add_edge(a, b, weight=w)
    ch = input("Do you want to enter another edge? (y/n): ")
    if ch.lower() != 'y':
        all_edges = False
k = int(input("\nEnter the number of stages in the graph: "))
A = nx.to_numpy_array(G)
result_forward = forward_approach(A, len(G))
print("\nMinimum cost to go from source to sink (Forward Approach):", result_forward[0])
print("Path (Forward Approach):", result_forward[1])
edge_colors_forward = ['red' if (u, v) in zip(result_forward[1], result_forward[1][1:]) else 'black' for u, v in G.edges()]
edge_widths_forward = [4 if (u, v) in zip(result_forward[1], result_forward[1][1:]) else 1 for u, v in G.edges()]
plot_graph(G, result_forward[1], edge_colors_forward, edge_widths_forward)
