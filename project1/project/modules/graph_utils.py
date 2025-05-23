import networkx as nx
import random

def create_random_graph(num_nodes, directed=False, connected=True, density=0.3):
    """
    Create a random graph with the specified number of nodes.
    
    Parameters:
    - num_nodes: Number of nodes in the graph
    - directed: If True, create a directed graph
    - connected: If True, ensure the graph is connected
    - density: Edge density (probability of edge creation)
    
    Returns:
    - A NetworkX graph
    """
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    # Add nodes
    G.add_nodes_from(range(num_nodes))
    
    # Add random edges
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if random.random() < density:
                G.add_edge(i, j)
    
    # Ensure the graph is connected
    if connected:
        components = list(nx.connected_components(G)) if not directed else list(nx.weakly_connected_components(G))
        if len(components) > 1:
            # Connect all components
            for i in range(len(components) - 1):
                u = random.choice(list(components[i]))
                v = random.choice(list(components[i+1]))
                G.add_edge(u, v)
    
    return G

def create_custom_graph(edges, directed=False):
    """
    Create a custom graph from a list of edges.
    
    Parameters:
    - edges: List of tuples representing edges (u, v)
    - directed: If True, create a directed graph
    
    Returns:
    - A NetworkX graph
    """
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    G.add_edges_from(edges)
    return G

def get_graph_info(graph):
    """
    Get basic information about the graph.
    
    Parameters:
    - graph: A NetworkX graph
    
    Returns:
    - Dictionary with graph information
    """
    info = {
        "num_nodes": graph.number_of_nodes(),
        "num_edges": graph.number_of_edges(),
        "is_directed": graph.is_directed(),
        "is_connected": nx.is_connected(graph) if not graph.is_directed() else nx.is_weakly_connected(graph),
        "average_degree": sum(dict(graph.degree()).values()) / graph.number_of_nodes(),
    }
    return info