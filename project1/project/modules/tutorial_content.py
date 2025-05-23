# Dictionary of algorithm descriptions
algorithm_descriptions = {
    "DFS": """
    ## Depth-First Search (DFS)
    
    DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking.
    
    ### Key Characteristics:
    - Uses a **stack** data structure (LIFO - Last In, First Out)
    - Explores deeply before going wide
    - Can be implemented recursively or iteratively
    - Often used for:
        - Finding connected components
        - Topological sorting
        - Solving mazes
        - Detecting cycles
    
    ### Pseudocode:
    ```
    DFS(graph, start_vertex):
        Create empty set 'visited'
        Create empty stack 'S'
        
        Add start_vertex to S
        
        while S is not empty:
            vertex = S.pop()
            
            if vertex not in visited:
                Add vertex to visited
                
                for each neighbor of vertex:
                    if neighbor not in visited:
                        Add neighbor to S
    ```
    
    ### Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
    """,
    
    "BFS": """
    ## Breadth-First Search (BFS)
    
    BFS is a graph traversal algorithm that explores all neighbors at the present depth prior to moving on to nodes at the next depth level.
    
    ### Key Characteristics:
    - Uses a **queue** data structure (FIFO - First In, First Out)
    - Explores wide before going deep
    - Finds shortest paths in unweighted graphs
    - Often used for:
        - Finding shortest path
        - Finding connected components
        - Testing bipartiteness
        - Network analysis
    
    ### Pseudocode:
    ```
    BFS(graph, start_vertex):
        Create empty set 'visited'
        Create empty queue 'Q'
        
        Add start_vertex to visited
        Add start_vertex to Q
        
        while Q is not empty:
            vertex = Q.dequeue()
            
            for each neighbor of vertex:
                if neighbor not in visited:
                    Add neighbor to visited
                    Add neighbor to Q
    ```
    
    ### Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
    """
}

# Dictionary of concept explanations
concept_explanations = {
    "graph": """
    ## Graphs
    
    A graph is a data structure consisting of a set of vertices (or nodes) and a set of edges connecting these vertices.
    
    ### Types of Graphs:
    - **Undirected Graph**: Edges have no direction
    - **Directed Graph**: Edges have direction
    - **Weighted Graph**: Edges have weights/costs
    - **Unweighted Graph**: Edges have no weights
    - **Connected Graph**: There is a path between every pair of vertices
    - **Disconnected Graph**: At least one vertex cannot be reached from another
    - **Cyclic Graph**: Contains at least one cycle
    - **Acyclic Graph**: Contains no cycles
    
    ### Graph Representations:
    - **Adjacency Matrix**: 2D array where cell [i][j] indicates an edge between vertices i and j
    - **Adjacency List**: Array of lists where each list contains the neighbors of a vertex
    """,
    
    "stack": """
    ## Stack Data Structure
    
    A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
    
    ### Operations:
    - **Push**: Add an element to the top of the stack
    - **Pop**: Remove the top element from the stack
    - **Peek/Top**: View the top element without removing it
    - **isEmpty**: Check if the stack is empty
    
    ### Applications:
    - Function call management (call stack)
    - Expression evaluation and conversion
    - Backtracking algorithms
    - Browser history
    - Undo operations in text editors
    """,
    
    "queue": """
    ## Queue Data Structure
    
    A queue is a linear data structure that follows the First In, First Out (FIFO) principle.
    
    ### Operations:
    - **Enqueue**: Add an element to the back of the queue
    - **Dequeue**: Remove the front element from the queue
    - **Front**: View the front element without removing it
    - **isEmpty**: Check if the queue is empty
    
    ### Applications:
    - Task scheduling
    - Print job processing
    - Breadth-first search
    - Message queues in distributed systems
    - Handling of requests on a single shared resource
    """
}