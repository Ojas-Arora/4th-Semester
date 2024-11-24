#MultiStage 
import matplotlib.pyplot as plt
import networkx as nx

def backward_approach(graph, n):
    backward_cost = [0] * n
    backward_path = [0] * n
    backward_cost[n - 1] = 0.0
    for j in range(n - 2, -1, -1):
        minimum = float('inf')
        for r in range(j + 1, n):
            if graph[j][r] != 0 and graph[j][r] + backward_cost[r] < minimum:
                minimum = graph[j][r] + backward_cost[r]
                backward_path[j] = r
                backward_cost[j] = minimum
    backward_paths = [0]
    current_node = backward_path[0]
    while current_node != n - 1:
        backward_paths.append(current_node)
        current_node = backward_path[current_node]
    backward_paths.append(n - 1)
    return backward_cost[0], backward_paths

def plot_graph(graph, paths, edge_colors, edge_widths):
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
result_backward = backward_approach(A, len(G))
print("\nMinimum cost to go from sink to source (Backward Approach):", result_backward[0])
print("Path (Backward Approach):", result_backward[1])
edge_colors_backward = ['blue' if (u, v) in zip(result_backward[1], result_backward[1][1:]) else 'black' for u, v in G.edges()]
edge_widths_backward = [4 if (u, v) in zip(result_backward[1], result_backward[1][1:]) else 1 for u, v in G.edges()]
plot_graph(G, result_backward[1], edge_colors_backward, edge_widths_backward)
