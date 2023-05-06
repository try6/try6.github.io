


import networkx as nx
import matplotlib.pyplot as plt

# Generate a random graph
G = nx.erdos_renyi_graph(100, 0.1)

# Simulate a diffusion process on the graph
diffusion = nx.epidemics.diffusion(G, beta=0.1)

# Plot the graph and the diffusion process
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color='lightblue', with_labels=True)
nx.draw_networkx_nodes(G, pos, nodelist=diffusion[-1], node_color='red')
plt.show()




import networkx as nx
import matplotlib.pyplot as plt

# Generate a random graph
G = nx.erdos_renyi_graph(100, 0.1)

# Initialize the state of each node to 0
state = {node: 0 for node in G.nodes}

# Simulate a diffusion process on the graph
for i in range(10):
    # Update the state of each node based on the majority vote of its neighbors
    for node in G.nodes:
        neighbors = list(G.neighbors(node))
        num_neighbors = len(neighbors)
        num_ones = sum([state[neighbor] for neighbor in neighbors])
        if num_ones > num_neighbors / 2:
            state[node] = 1
        else:
            state[node] = 0
    # Plot the graph and the diffusion process
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color=[state[node] for node in G.nodes], with_labels=True)
    plt.show()



