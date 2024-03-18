from tracemalloc import start
from matplotlib.patches import ConnectionStyle
import networkx as nx
import matplotlib.pyplot as plt
import tabulate
G = nx.MultiDiGraph()
def floydwarshall(adjacency_matrix, edge_list):
    for k in range(len(adjacency_matrix)):
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix)):
                adjacency_matrix[i][j] = min(
                    adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])
                if ((i, j) in edge_list):
                    edge_list.pop((i, j))
                    edge_list[(i, j)] = adjacency_matrix[i][j]
    return adjacency_matrix, edge_list
def neg_cycle(edge_list, num_nodes):
    dist = [float("inf")] * (num_nodes)
    dist[0] = 0
    for i in range((num_nodes)):
        for (start_node, end_node), weight in edge_list.items():
            if (
                dist[start_node] != float("inf")
                and dist[start_node] + weight < dist[end_node]
            ):
                dist[end_node] = dist[start_node] + weight
    for (start_node, end_node), weight in edge_list.items():
        if (
            dist[start_node] != float("inf")
            and dist[start_node] + weight < dist[end_node]
        ):
            return True
    return False
def accept_graph():
    print("Enter the number of nodes")
    num_nodes = int(input())
    print("Enter the number of edges")
    num_edges = int(input())
    edge_list = {}
    adjacency_matrix = [
        [float("inf") for i in range(num_nodes)] for j in range(num_nodes)
    ]
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if i == j:
                adjacency_matrix[i][j] = 0
    for i in range(num_edges):
        temp_start = int(input(f"Enter starting node "))
        temp_end = int(input(f"Enter ending node "))
        if temp_start == temp_end:
            print(f"Distance b/w same nodes is already zero")
            i -= 1
            continue
        temp_weight = int(input(f"Enter cost "))
        G.add_edge(temp_start, temp_end, weight=temp_weight)
        edge_list[(temp_start, temp_end)] = temp_weight
        adjacency_matrix[temp_start][temp_end] = temp_weight
    return num_nodes, num_edges, edge_list, adjacency_matrix
num_nodes, num_edges, edge_list, adjacency_matrix = accept_graph()
if neg_cycle(edge_list, num_nodes):
    print("Graph contains negative cycle")
    G.clear()
while neg_cycle(edge_list, num_nodes):
    num_nodes, num_edges, edge_list, adjacency_matrix = accept_graph()
    if neg_cycle(edge_list, num_nodes):
        print("Graph contains negative cycle")
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightpink",
    node_size=500,
    font_size=14,
    font_weight="bold",
    connectionstyle="arc3, rad = 0.1",
)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_list)
plt.show()
print(f"Initial Matrix")
print(tabulate.tabulate(adjacency_matrix, tablefmt="pretty"))
with open("Floyd Warshall.txt", "a") as f:
    f.write(f"Initial Matrix")
    f.write(tabulate.tabulate(adjacency_matrix, tablefmt="pretty"))
print(f"Adjusting the graph using Floyd Warshall Algorithm")
adjacency_matrix, edge_list = floydwarshall(adjacency_matrix, edge_list)
print(f"Final Matrix")
print(tabulate.tabulate(adjacency_matrix, tablefmt="pretty"))
with open("Floyd Warshall.txt", "a") as f:
    f.write(f"\n\n Final Matrix")
    f.write(tabulate.tabulate(adjacency_matrix, tablefmt="pretty"))
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightpink",
    node_size=500,
    font_size=14,
    font_weight="bold",
    connectionstyle="arc3, rad = 0.1",
)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_list)
plt.show()
