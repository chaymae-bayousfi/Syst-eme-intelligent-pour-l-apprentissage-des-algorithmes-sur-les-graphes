def dfs(graph, start_node):
    """
    Perform a depth-first search on the graph and return the steps.
    
    Parameters:
    - graph: A NetworkX graph
    - start_node: The node to start the search from
    
    Returns:
    - A list of dictionaries, each representing a step in the algorithm
    """
    steps = []
    visited = set()
    stack = [start_node]
    exploration_order = []
    
    # Add initial state
    steps.append({
        "visited": list(visited),
        "stack": list(stack),
        "current": None,
        "exploration_order": list(exploration_order),
        "description": f"Starting DFS from node {start_node}. The stack contains the starting node."
    })
    
    while stack:
        current = stack.pop()
        
        if current not in visited:
            visited.add(current)
            exploration_order.append(current)
            
            # Add intermediate state after visiting node
            steps.append({
                "visited": list(visited),
                "stack": list(stack),
                "current": current,
                "exploration_order": list(exploration_order),
                "description": f"Visiting node {current} and marking it as visited."
            })
            
            # Get neighbors and sort them in reverse order (for DFS stack behavior)
            neighbors = sorted(list(graph.neighbors(current)), reverse=True)
            unvisited_neighbors = [n for n in neighbors if n not in visited]
            
            if unvisited_neighbors:
                stack.extend(unvisited_neighbors)
                
                # Add state after adding neighbors to stack
                steps.append({
                    "visited": list(visited),
                    "stack": list(stack),
                    "current": current,
                    "exploration_order": list(exploration_order),
                    "description": f"Adding unvisited neighbors of node {current} to the stack: {unvisited_neighbors}"
                })
    
    # Add final state
    steps.append({
        "visited": list(visited),
        "stack": list(stack),
        "current": None,
        "exploration_order": list(exploration_order),
        "description": "DFS completed. All reachable nodes have been visited."
    })
    
    return steps

def bfs(graph, start_node):
    """
    Perform a breadth-first search on the graph and return the steps.
    
    Parameters:
    - graph: A NetworkX graph
    - start_node: The node to start the search from
    
    Returns:
    - A list of dictionaries, each representing a step in the algorithm
    """
    steps = []
    visited = set()
    queue = [start_node]
    exploration_order = []
    
    # Add initial state
    steps.append({
        "visited": list(visited),
        "queue": list(queue),
        "current": None,
        "exploration_order": list(exploration_order),
        "description": f"Starting BFS from node {start_node}. The queue contains the starting node."
    })
    
    while queue:
        current = queue.pop(0)  # Pop from the beginning for queue behavior
        
        if current not in visited:
            visited.add(current)
            exploration_order.append(current)
            
            # Add intermediate state after visiting node
            steps.append({
                "visited": list(visited),
                "queue": list(queue),
                "current": current,
                "exploration_order": list(exploration_order),
                "description": f"Visiting node {current} and marking it as visited."
            })
            
            # Get neighbors
            neighbors = sorted(list(graph.neighbors(current)))
            unvisited_neighbors = [n for n in neighbors if n not in visited and n not in queue]
            
            if unvisited_neighbors:
                queue.extend(unvisited_neighbors)
                
                # Add state after adding neighbors to queue
                steps.append({
                    "visited": list(visited),
                    "queue": list(queue),
                    "current": current,
                    "exploration_order": list(exploration_order),
                    "description": f"Adding unvisited neighbors of node {current} to the queue: {unvisited_neighbors}"
                })
    
    # Add final state
    steps.append({
        "visited": list(visited),
        "queue": list(queue),
        "current": None,
        "exploration_order": list(exploration_order),
        "description": "BFS completed. All reachable nodes have been visited."
    })
    
    return steps