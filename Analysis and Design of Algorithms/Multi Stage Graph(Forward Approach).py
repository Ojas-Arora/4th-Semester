import matplotlib.pyplot as plt
import networkx as nx
def multistageGraph(graph, k, n):
    forward_cost = [0] * n
    backward_cost = [0] * n
    forward_path = [0] * n
    backward_path = [0] * n
    forward_cost[0] = 0.0
    backward_cost[n - 1] = 0.0
    # Forward Pass: Finding the minimum distance from the source to each node in each stage
    for j in range(1, n):
        minimum = float('inf')
        for r in range(j):
            if graph[r][j] != 0 and graph[r][j] + forward_cost[r] < minimum:
                minimum = graph[r][j] + forward_cost[r]
                forward_path[j] = r
                forward_cost[j] = minimum
    # Backward Pass: Finding the minimum distance from the sink to each node in each stage
    for j in range(n - 2, -1, -1):
        minimum = float('inf')
        for r in range(j + 1, n):
            if graph[j][r] != 0 and graph[j][r] + backward_cost[r] < minimum:
                minimum = graph[j][r] + backward_cost[r]
                backward_path[j] = r
                backward_cost[j] = minimum
    forward_paths = [n]
    current_node = forward_path[n - 1]
    while current_node != 0:
        forward_paths.insert(0, current_node)
        current_node = forward_path[current_node]
    forward_paths.insert(0, 0)
    backward_paths = [0]
    current_node = backward_path[0]
    while current_node != n - 1:
        backward_paths.append(current_node)
        current_node = backward_path[current_node]
    backward_paths.append(n - 1)
    return forward_cost[n - 1], forward_paths, backward_cost[0], backward_paths
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
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color="lightpink",
        node_size=500, font_size=14, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
A = nx.to_numpy_array(G)
result = multistageGraph(A, k, len(G))
print("\nMinimum cost to go from source to sink (Forward Approach):", result[0])
print("Path (Forward Approach):", result[1])
print("\nMinimum cost to go from source to sink (Backward Approach):", result[2])
print("Path (Backward Approach):", result[3])
edge_colors_forward = ['red' if (u, v) in zip(result[1], result[1][1:]) else 'black' for u, v in G.edges()]
edge_colors_backward = ['blue' if (u, v) in zip(result[3], result[3][1:]) else 'black' for u, v in G.edges()]
edge_widths = [4 if (u, v) in zip(result[1], result[1][1:]) else 1 for u, v in G.edges()]
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color="lightpink",
        node_size=500, font_size=14, font_weight='bold')
nx.draw_networkx_edges(G, pos, edge_color=edge_colors_forward, width=edge_widths)
nx.draw_networkx_edges(G, pos, edge_color=edge_colors_backward, width=edge_widths, style='dashed')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
