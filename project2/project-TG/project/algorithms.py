import networkx as nx
import numpy as np

def dfs_algorithm(G, start_node):
    """
    Perform Depth-First Search on a graph and record each step
    
    Parameters:
    - G: NetworkX graph
    - start_node: Starting node for the traversal
    
    Returns:
    - List of steps, where each step contains:
      - visited: List of visited nodes
      - current: Current node being processed
      - stack: Current state of the stack
      - edges: Edges traversed in this step
      - explanation: Text explanation of this step
    """
    steps = []
    visited = []
    stack = [start_node]
    
    # Initial step
    steps.append({
        'visited': [],
        'current': None,
        'stack': stack.copy(),
        'edges': [],
        'explanation': f"Starting DFS from node {start_node}. Initialize with an empty visited set and add node {start_node} to the stack."
    })
    
    while stack:
        # Get the next node from stack
        current = stack.pop()
        
        # Skip if already visited
        if current in visited:
            steps.append({
                'visited': visited.copy(),
                'current': current,
                'stack': stack.copy(),
                'edges': [],
                'explanation': f"Node {current} has already been visited, so we skip it and move to the next node in the stack."
            })
            continue
        
        # Mark as visited
        visited.append(current)
        
        # Find neighbors
        neighbors = list(G.neighbors(current))
        
        # Sort neighbors to ensure consistent behavior
        neighbors.sort(reverse=True)  # Reverse to simulate traditional DFS behavior with stack
        
        steps.append({
            'visited': visited.copy(),
            'current': current,
            'stack': stack.copy(),
            'edges': [],
            'explanation': f"Visit node {current} and mark it as visited. Examine its neighbors: {neighbors}."
        })
        
        # Push neighbors to stack
        edges_added = []
        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)
                edges_added.append((current, neighbor))
        
        if edges_added:
            steps.append({
                'visited': visited.copy(),
                'current': current,
                'stack': stack.copy(),
                'edges': edges_added,
                'explanation': f"Add unvisited neighbors {[n for _, n in edges_added]} to the stack for later processing."
            })
    
    # Final step
    steps.append({
        'visited': visited.copy(),
        'current': None,
        'stack': [],
        'edges': [],
        'explanation': f"DFS complete. All reachable nodes have been visited in this order: {visited}."
    })
    
    return steps

def bfs_algorithm(G, start_node):
    """
    Perform Breadth-First Search on a graph and record each step
    
    Parameters:
    - G: NetworkX graph
    - start_node: Starting node for the traversal
    
    Returns:
    - List of steps, where each step contains:
      - visited: List of visited nodes
      - current: Current node being processed
      - queue: Current state of the queue
      - edges: Edges traversed in this step
      - explanation: Text explanation of this step
    """
    steps = []
    visited = []
    queue = [start_node]
    
    # Initial step
    steps.append({
        'visited': [],
        'current': None,
        'queue': queue.copy(),
        'edges': [],
        'explanation': f"Starting BFS from node {start_node}. Initialize with an empty visited set and add node {start_node} to the queue."
    })
    
    while queue:
        # Get the next node from queue
        current = queue.pop(0)
        
        # Skip if already visited
        if current in visited:
            steps.append({
                'visited': visited.copy(),
                'current': current,
                'queue': queue.copy(),
                'edges': [],
                'explanation': f"Node {current} has already been visited, so we skip it and move to the next node in the queue."
            })
            continue
        
        # Mark as visited
        visited.append(current)
        
        # Find neighbors
        neighbors = list(G.neighbors(current))
        
        # Sort neighbors to ensure consistent behavior
        neighbors.sort()
        
        steps.append({
            'visited': visited.copy(),
            'current': current,
            'queue': queue.copy(),
            'edges': [],
            'explanation': f"Visit node {current} and mark it as visited. Examine its neighbors: {neighbors}."
        })
        
        # Add neighbors to queue
        edges_added = []
        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                edges_added.append((current, neighbor))
        
        if edges_added:
            steps.append({
                'visited': visited.copy(),
                'current': current,
                'queue': queue.copy(),
                'edges': edges_added,
                'explanation': f"Add unvisited neighbors {[n for _, n in edges_added]} to the queue for later processing."
            })
    
    # Final step
    steps.append({
        'visited': visited.copy(),
        'current': None,
        'queue': [],
        'edges': [],
        'explanation': f"BFS complete. All reachable nodes have been visited in this order: {visited}."
    })
    
    return steps

def calculate_shortest_path(G, start_node, end_node):
    """Calculate the shortest path between two nodes"""
    try:
        path = nx.shortest_path(G, source=start_node, target=end_node)
        return path
    except nx.NetworkXNoPath:
        return None

def get_algorithm_properties():
    """
    Return the properties and characteristics of DFS and BFS algorithms
    """
    properties = {
        "DFS": {
            "full_name": "Depth-First Search",
            "data_structure": "Stack",
            "space_complexity": "O(h) where h is the height of the tree/graph",
            "time_complexity": "O(V + E) where V is vertices and E is edges",
            "uses": [
                "Finding connected components",
                "Topological sorting",
                "Detecting cycles",
                "Solving puzzles with backtracking"
            ],
            "characteristics": [
                "Explores as far as possible along each branch before backtracking",
                "Uses a stack (either explicitly or through recursion)",
                "May not find the shortest path between two nodes",
                "Good for exploring all possible paths"
            ]
        },
        "BFS": {
            "full_name": "Breadth-First Search",
            "data_structure": "Queue",
            "space_complexity": "O(w) where w is the maximum width of the tree/graph",
            "time_complexity": "O(V + E) where V is vertices and E is edges",
            "uses": [
                "Finding shortest paths in unweighted graphs",
                "Finding all nodes within a connected component",
                "Testing bipartiteness",
                "Building web crawlers"
            ],
            "characteristics": [
                "Explores neighbors at the present depth before moving to nodes at the next depth level",
                "Uses a queue to track nodes to visit next",
                "Guarantees shortest path in unweighted graphs",
                "Good for finding the shortest path"
            ]
        }
    }
    
    return properties