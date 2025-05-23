import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def visualize_graph(graph, node_size=700, font_size=10, title="Graph Visualization"):
    """
    Create a basic visualization of the graph.
    
    Parameters:
    - graph: A NetworkX graph
    - node_size: Size of nodes in the visualization
    - font_size: Size of node labels
    - title: Title of the plot
    
    Returns:
    - Matplotlib figure
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Use a fixed layout for consistent visualization
    pos = nx.spring_layout(graph, seed=42)
    
    # Draw the graph
    nx.draw_networkx(
        graph, 
        pos=pos,
        with_labels=True,
        node_color='lightblue',
        node_size=node_size,
        font_size=font_size,
        font_weight='bold',
        edge_color='gray',
        width=2,
        alpha=0.8,
        ax=ax
    )
    
    ax.set_title(title, fontsize=16)
    ax.set_axis_off()
    
    plt.tight_layout()
    return fig

def visualize_algorithm_step(graph, step_data, algorithm):
    """
    Visualize a specific step in the graph algorithm.
    
    Parameters:
    - graph: A NetworkX graph
    - step_data: Dictionary with step information
    - algorithm: String specifying the algorithm (DFS or BFS)
    
    Returns:
    - Matplotlib figure
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Use a fixed layout for consistent visualization
    pos = nx.spring_layout(graph, seed=42)
    
    # Define node colors based on the algorithm state
    node_colors = []
    visited = step_data["visited"]
    current = step_data["current"]
    
    for node in graph.nodes():
        if node == current:
            node_colors.append('red')  # Current node
        elif node in visited:
            node_colors.append('green')  # Visited node
        elif algorithm == "DFS" and "stack" in step_data and node in step_data["stack"]:
            node_colors.append('orange')  # Node in stack (DFS)
        elif algorithm == "BFS" and "queue" in step_data and node in step_data["queue"]:
            node_colors.append('orange')  # Node in queue (BFS)
        else:
            node_colors.append('lightblue')  # Unvisited node
    
    # Draw the graph
    nx.draw_networkx(
        graph, 
        pos=pos,
        with_labels=True,
        node_color=node_colors,
        node_size=700,
        font_size=10,
        font_weight='bold',
        edge_color='gray',
        width=2,
        alpha=0.8,
        ax=ax
    )
    
    # Add legend
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightblue', markersize=15, label='Unvisited'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=15, label='Visited'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=15, 
                  label='In Stack' if algorithm == "DFS" else 'In Queue'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=15, label='Current')
    ]
    ax.legend(handles=legend_elements, loc='upper right')
    
    # Add step description
    if "description" in step_data:
        ax.set_title(step_data["description"], fontsize=14)
    else:
        ax.set_title(f"{algorithm} Visualization - Step {step_data.get('step', 0)}", fontsize=14)
    
    ax.set_axis_off()
    
    # Add algorithm state information
    state_text = []
    
    if algorithm == "DFS":
        state_text.append(f"Stack: {step_data.get('stack', [])}")
    else:  # BFS
        state_text.append(f"Queue: {step_data.get('queue', [])}")
    
    state_text.append(f"Visited: {visited}")
    
    if "exploration_order" in step_data:
        state_text.append(f"Exploration Order: {step_data['exploration_order']}")
    
    fig.text(0.05, 0.05, "\n".join(state_text), fontsize=12)
    
    plt.tight_layout()
    return fig