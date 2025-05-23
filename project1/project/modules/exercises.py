import random
import networkx as nx
import re

def generate_exercise(algorithm):
    """
    Generate an exercise for the given algorithm.
    
    Parameters:
    - algorithm: String specifying the algorithm (DFS or BFS)
    
    Returns:
    - Dictionary with exercise information
    """
    exercise_type = random.choice(["traversal_order", "visited_nodes", "next_node", "application"])
    
    if exercise_type == "traversal_order":
        return generate_traversal_order_exercise(algorithm)
    elif exercise_type == "visited_nodes":
        return generate_visited_nodes_exercise(algorithm)
    elif exercise_type == "next_node":
        return generate_next_node_exercise(algorithm)
    else:  # application
        return generate_application_exercise(algorithm)

def generate_traversal_order_exercise(algorithm):
    """Generate an exercise about finding the correct traversal order."""
    # Create a small graph
    G = nx.Graph()
    
    # Simple tree-like structure
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    G.add_edges_from(edges)
    
    start_node = 0
    
    # Calculate the correct traversal order
    if algorithm == "DFS":
        # Simple DFS traversal order (this is a simplified version)
        correct_order = [0, 2, 6, 5, 1, 4, 3]
    else:  # BFS
        # Simple BFS traversal order
        correct_order = [0, 1, 2, 3, 4, 5, 6]
    
    return {
        "type": "traversal_order",
        "graph": G,
        "start_node": start_node,
        "correct_answer": correct_order,
        "description": f"""
        Consider the following graph with edges: {edges}
        
        Starting from node {start_node}, list the order in which nodes would be visited using {algorithm}.
        
        Enter your answer as a comma-separated list of node numbers.
        """
    }

def generate_visited_nodes_exercise(algorithm):
    """Generate an exercise about identifying visited nodes at a certain step."""
    # Create a small graph
    G = nx.Graph()
    
    # Simple structure
    edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5)]
    G.add_edges_from(edges)
    
    start_node = 0
    step = random.randint(2, 4)
    
    # Calculate visited nodes at the given step
    if algorithm == "DFS":
        # Simple DFS (this is a simplified version)
        visited_at_steps = [
            [0],
            [0, 2],
            [0, 2, 4],
            [0, 2, 4, 5]
        ]
    else:  # BFS
        # Simple BFS
        visited_at_steps = [
            [0],
            [0, 1, 2],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5]
        ]
    
    correct_visited = visited_at_steps[min(step, len(visited_at_steps)-1)]
    
    return {
        "type": "visited_nodes",
        "graph": G,
        "start_node": start_node,
        "step": step,
        "correct_answer": correct_visited,
        "description": f"""
        Consider the following graph with edges: {edges}
        
        When running {algorithm} starting from node {start_node}, which nodes would be marked as visited after {step} steps?
        
        Enter your answer as a comma-separated list of node numbers.
        """
    }

def generate_next_node_exercise(algorithm):
    """Generate an exercise about identifying the next node to be visited."""
    # Create a small graph
    G = nx.Graph()
    
    # Simple structure
    edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5)]
    G.add_edges_from(edges)
    
    start_node = 0
    
    # Set up a specific state
    if algorithm == "DFS":
        visited = [0, 2, 4]
        stack = [1]
        correct_answer = 1
    else:  # BFS
        visited = [0, 1, 2]
        queue = [3, 4]
        correct_answer = 3
    
    return {
        "type": "next_node",
        "graph": G,
        "start_node": start_node,
        "visited": visited,
        "data_structure": stack if algorithm == "DFS" else queue,
        "correct_answer": correct_answer,
        "description": f"""
        Consider the following graph with edges: {edges}
        
        When running {algorithm} starting from node {start_node}, assume the current state is:
        - Visited nodes: {visited}
        - {"Stack" if algorithm == "DFS" else "Queue"}: {stack if algorithm == "DFS" else queue}
        
        Which node will be visited next?
        
        Enter your answer as a single node number.
        """
    }

def generate_application_exercise(algorithm):
    """Generate an exercise about algorithm application."""
    if algorithm == "DFS":
        return {
            "type": "application",
            "correct_answer": ["cycle detection", "topological sorting", "finding connected components", "maze solving"],
            "description": """
            List at least two applications where Depth-First Search (DFS) is particularly useful.
            
            Explain briefly why DFS is well-suited for these applications.
            """
        }
    else:  # BFS
        return {
            "type": "application",
            "correct_answer": ["shortest path", "finding connected components", "level order traversal", "network analysis"],
            "description": """
            List at least two applications where Breadth-First Search (BFS) is particularly useful.
            
            Explain briefly why BFS is well-suited for these applications.
            """
        }

def verify_solution(exercise, user_solution, algorithm):
    """
    Verify the user's solution to the exercise.
    
    Parameters:
    - exercise: Dictionary with exercise information
    - user_solution: User's submitted solution
    - algorithm: String specifying the algorithm (DFS or BFS)
    
    Returns:
    - (result, feedback): Tuple with boolean result and feedback string
    """
    if exercise["type"] == "traversal_order" or exercise["type"] == "visited_nodes":
        # Parse user's comma-separated list
        try:
            user_answer = [int(x.strip()) for x in user_solution.split(',')]
            correct_answer = exercise["correct_answer"]
            
            if user_answer == correct_answer:
                return True, "Your traversal order is correct!"
            else:
                return False, f"Not quite right. The correct order should be: {correct_answer}"
        except:
            return False, "Please enter your answer as a comma-separated list of node numbers (e.g., 0, 1, 2, 3)."
    
    elif exercise["type"] == "next_node":
        try:
            user_answer = int(user_solution.strip())
            correct_answer = exercise["correct_answer"]
            
            if user_answer == correct_answer:
                return True, f"Correct! Node {correct_answer} will be visited next."
            else:
                return False, f"Not quite right. The next node to be visited would be {correct_answer}."
        except:
            return False, "Please enter your answer as a single node number (e.g., 3)."
    
    else:  # application
        user_answer_lower = user_solution.lower()
        correct_applications = exercise["correct_answer"]
        
        # Check if the user mentioned at least two valid applications
        mentioned_count = sum(1 for app in correct_applications if app.lower() in user_answer_lower)
        
        if mentioned_count >= 2:
            return True, "Your understanding of algorithm applications is correct!"
        elif mentioned_count == 1:
            return False, "You've identified one valid application. Can you think of another one?"
        else:
            return False, f"Try again. Some valid applications include: {', '.join(correct_applications[:3])}."