import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from matplotlib.colors import to_rgba

def create_sample_graph(num_nodes=6, edge_probability=0.4, directed=False):
    """
    Create a random graph for demonstration
    """
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
        
    # Add nodes
    for i in range(num_nodes):
        G.add_node(i)
    
    # Add random edges
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if np.random.random() < edge_probability:
                G.add_edge(i, j)
    
    # Ensure graph is connected
    if not nx.is_connected(G) and not directed:
        components = list(nx.connected_components(G))
        for i in range(1, len(components)):
            node1 = list(components[0])[0]
            node2 = list(components[i])[0]
            G.add_edge(node1, node2)
    
    return G

def visualize_graph(G, node_colors=None, highlighted_edges=None, title=None, figsize=(8, 6)):
    """
    Visualize a graph with optional node coloring and edge highlighting
    """
    plt.figure(figsize=figsize)
    pos = nx.spring_layout(G, seed=42)  # For consistent layout
    
    # Default node colors if not specified
    if node_colors is None:
        node_colors = ['#1f78b4'] * len(G.nodes())
    
    # Draw nodes
    nx.draw_networkx_nodes(
        G, pos, 
        node_color=node_colors,
        node_size=500,
        alpha=0.8,
        edgecolors='black',
        linewidths=1.0
    )
    
    # Draw all edges
    if highlighted_edges is None:
        nx.draw_networkx_edges(
            G, pos, 
            width=1.5,
            alpha=0.7,
            edge_color='gray'
        )
    else:
        # Draw regular edges
        regular_edges = [e for e in G.edges() if e not in highlighted_edges and (e[1], e[0]) not in highlighted_edges]
        nx.draw_networkx_edges(
            G, pos, 
            edgelist=regular_edges,
            width=1.5,
            alpha=0.5,
            edge_color='gray'
        )
        
        # Draw highlighted edges
        nx.draw_networkx_edges(
            G, pos, 
            edgelist=highlighted_edges,
            width=2.5,
            alpha=1.0,
            edge_color='red',
            arrowsize=20,
            arrowstyle='->'
        )
    
    # Draw labels
    nx.draw_networkx_labels(
        G, pos,
        font_size=14,
        font_weight='bold',
        font_color='white'
    )
    
    # Add title if provided
    if title:
        plt.title(title, fontsize=16)
    
    plt.axis('off')
    plt.tight_layout()
    
    return plt

def add_node_to_graph(G):
    """Add a new node to the graph"""
    new_node = len(G.nodes())
    G.add_node(new_node)
    return G

def add_edge_to_graph(G, from_node, to_node):
    """Add an edge to the graph"""
    if from_node in G.nodes() and to_node in G.nodes():
        G.add_edge(from_node, to_node)
    return G

def remove_node_from_graph(G, node):
    """Remove a node from the graph"""
    if node in G.nodes():
        G.remove_node(node)
    return G

def remove_edge_from_graph(G, from_node, to_node):
    """Remove an edge from the graph"""
    if G.has_edge(from_node, to_node):
        G.remove_edge(from_node, to_node)
    return G

def get_node_colors(G, visited=None, current=None):
    """
    Generate node colors based on visited status and current node
    
    Parameters:
    - visited: List of visited nodes
    - current: Current node being processed
    
    Returns:
    - List of colors for each node
    """
    if visited is None:
        visited = []
    
    colors = []
    for node in G.nodes():
        if node == current:
            colors.append('#e31a1c')  # Red for current node
        elif node in visited:
            colors.append('#33a02c')  # Green for visited nodes
        else:
            colors.append('#1f78b4')  # Blue for unvisited nodes
    
    return colors

def get_node_status_text(G, visited=None, current=None, queue=None, stack=None):
    """
    Generate text explaining the status of each node
    """
    if visited is None:
        visited = []
    if queue is None:
        queue = []
    if stack is None:
        stack = []
    
    status_text = ""
    for node in sorted(G.nodes()):
        status = f"Node {node}: "
        if node == current:
            status += "Currently being processed"
        elif node in visited:
            status += "Visited"
        else:
            status += "Not visited yet"
        
        if node in queue:
            status += f" (in queue at position {queue.index(node)})"
        if node in stack:
            status += f" (in stack at position {stack.index(node)})"
            
        status_text += status + "\n"
    
    return status_text