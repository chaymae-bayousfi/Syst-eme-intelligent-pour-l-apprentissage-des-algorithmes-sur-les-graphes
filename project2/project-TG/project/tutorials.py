def get_tutorial_content(algorithm, section):
    """
    Get tutorial content for a specific algorithm and section
    
    Parameters:
    - algorithm: String, either 'DFS' or 'BFS'
    - section: String, the section name
    
    Returns:
    - Dictionary with title and content
    """
    tutorials = {
        "DFS": {
            "introduction": {
                "title": "Introduction to Depth-First Search (DFS)",
                "content": """
# Depth-First Search (DFS)

Depth-First Search is a graph traversal algorithm that explores as far as possible along each branch before backtracking.

## Key Characteristics

- Uses a **stack** data structure (either explicitly or implicitly through recursion)
- Explores deep into the graph before exploring siblings
- Not guaranteed to find the shortest path
- Useful for topological sorting, finding connected components, and solving mazes

## How It Works

1. Start at a chosen node (root for trees)
2. Mark the current node as visited
3. Explore each adjacent unvisited node using DFS recursively
4. If all adjacent nodes have been visited, backtrack

DFS can be implemented using either recursion or an explicit stack.
                """
            },
            "pseudocode": {
                "title": "DFS Algorithm Pseudocode",
                "content": """
# DFS Pseudocode

```
DFS(graph, startNode):
    mark startNode as visited
    for each neighbor of startNode:
        if neighbor is not visited:
            DFS(graph, neighbor)
```

## Iterative Version (using explicit stack)

```
DFS_iterative(graph, startNode):
    create empty stack S
    push startNode to S
    
    while S is not empty:
        current = S.pop()
        if current is not visited:
            mark current as visited
            for each neighbor of current:
                if neighbor is not visited:
                    push neighbor to S
```

The key insight is that DFS always prioritizes depth over breadth - it will go as deep as possible before exploring siblings.
                """
            },
            "time_complexity": {
                "title": "DFS Time & Space Complexity",
                "content": """
# DFS Complexity Analysis

## Time Complexity
- **O(V + E)** where V is the number of vertices and E is the number of edges
- We must visit each vertex once
- We must explore each edge once

## Space Complexity
- **O(h)** where h is the height of the recursion tree
- In the worst case (a linear graph), this could be O(V)
- For balanced trees, this would be O(log V)

The space complexity primarily comes from:
1. The recursion stack in the recursive implementation
2. The explicit stack in the iterative implementation 
3. The visited set that tracks visited nodes

For dense graphs (where E is close to V²), the complexity can be dominated by the number of edges, making it closer to O(V²).
                """
            },
            "applications": {
                "title": "DFS Applications",
                "content": """
# Applications of DFS

## 1. Topological Sorting
- Finding an ordering of vertices in a directed acyclic graph (DAG)
- Useful for scheduling tasks with dependencies

## 2. Finding Connected Components
- Identifying separate groups of nodes in a graph
- Used in network analysis and image segmentation

## 3. Detecting Cycles
- Determining if a graph contains cycles
- Important for dependency analysis

## 4. Maze Solving
- Finding a path through a maze
- DFS will find *a* solution, though not necessarily the shortest

## 5. Generating Minimum Spanning Trees
- Building a tree that connects all vertices with minimum weight

## 6. Pathfinding in Game Trees
- Used in game AI to explore possible moves
- Algorithms like minimax use DFS to explore game states
                """
            },
            "comparison": {
                "title": "DFS vs BFS Comparison",
                "content": """
# DFS vs BFS: Key Differences

| Feature | DFS | BFS |
|---------|-----|-----|
| Data Structure | Stack | Queue |
| Traversal Order | Deep first, then siblings | Level by level |
| Space Complexity | O(h) - height of tree | O(w) - max width of tree |
| Completeness | Not complete for infinite graphs | Complete |
| Optimality | Not optimal for shortest path | Optimal for unweighted graphs |
| Implementation | Often recursive | Usually iterative |
| Memory Usage | Often less memory in balanced trees | Can use more memory |

## When to Choose DFS
- When you need to explore all possible paths
- When the solution is likely to be far from the root
- When working with deep, narrow trees
- For topological sorting or cycle detection

## When to Choose BFS
- When you need the shortest path
- When working with wide, shallow trees
- When the solution is likely to be close to the root
                """
            }
        },
        "BFS": {
            "introduction": {
                "title": "Introduction to Breadth-First Search (BFS)",
                "content": """
# Breadth-First Search (BFS)

Breadth-First Search is a graph traversal algorithm that explores all neighbors at the present depth before moving to nodes at the next depth level.

## Key Characteristics

- Uses a **queue** data structure
- Explores level by level (all siblings before children)
- Guaranteed to find the shortest path in unweighted graphs
- Useful for finding shortest paths, connected components, and level-order traversals

## How It Works

1. Start at a chosen node
2. Explore all neighbor nodes at the present depth
3. Move to the next level of nodes
4. Repeat until all nodes are visited

BFS is implemented using a queue to keep track of nodes to visit next.
                """
            },
            "pseudocode": {
                "title": "BFS Algorithm Pseudocode",
                "content": """
# BFS Pseudocode

```
BFS(graph, startNode):
    create empty queue Q
    mark startNode as visited
    enqueue startNode into Q
    
    while Q is not empty:
        current = Q.dequeue()
        
        for each neighbor of current:
            if neighbor is not visited:
                mark neighbor as visited
                enqueue neighbor into Q
```

The key insight is that BFS processes all nodes at a given distance from the start before moving to nodes that are farther away.

For finding shortest paths, you can easily modify BFS to keep track of the distance from the start node to each visited node.
                """
            },
            "time_complexity": {
                "title": "BFS Time & Space Complexity",
                "content": """
# BFS Complexity Analysis

## Time Complexity
- **O(V + E)** where V is the number of vertices and E is the number of edges
- Each vertex is dequeued exactly once
- Each edge is considered exactly once

## Space Complexity
- **O(w)** where w is the maximum width of the graph
- In the worst case (a completely connected graph), this could be O(V)
- The space is primarily used for the queue and the visited set

For a tree, the maximum width is the maximum number of nodes at any level, which can be up to V/2 in a balanced binary tree, making the space complexity O(V).

The space complexity of BFS is often higher than DFS, especially for deep, narrow graphs.
                """
            },
            "applications": {
                "title": "BFS Applications",
                "content": """
# Applications of BFS

## 1. Shortest Path Finding
- Finding the shortest path between two nodes in an unweighted graph
- Used in navigation systems and network routing

## 2. Web Crawling
- Exploring web pages by following links level by level
- Used by search engines to index the web

## 3. Social Network Analysis
- Finding friends or connections within n degrees of separation
- Calculating the "degrees of separation" between individuals

## 4. Connected Components
- Identifying separate groups of nodes in a graph
- Used in image segmentation and network analysis

## 5. Puzzle Solving
- Solving puzzles with the fewest moves
- Examples include sliding puzzles, Rubik's Cube, etc.

## 6. Bipartite Graph Testing
- Determining if a graph can be colored using only two colors
- Important in various matching problems
                """
            },
            "comparison": {
                "title": "BFS vs DFS Comparison",
                "content": """
# BFS vs DFS: Key Differences

| Feature | BFS | DFS |
|---------|-----|-----|
| Data Structure | Queue | Stack |
| Traversal Order | Level by level | Deep first, then siblings |
| Space Complexity | O(w) - max width of tree | O(h) - height of tree |
| Completeness | Complete | Not complete for infinite graphs |
| Optimality | Optimal for unweighted graphs | Not optimal for shortest path |
| Implementation | Usually iterative | Often recursive |
| Memory Usage | Can use more memory | Often less memory in balanced trees |

## When to Choose BFS
- When you need the shortest path
- When working with wide, shallow trees
- When the solution is likely to be close to the root

## When to Choose DFS
- When you need to explore all possible paths
- When the solution is likely to be far from the root
- When working with deep, narrow trees
- For topological sorting or cycle detection
                """
            }
        }
    }
    
    if algorithm in tutorials and section in tutorials[algorithm]:
        return tutorials[algorithm][section]
    else:
        return {"title": "Content Not Found", "content": "The requested tutorial content is not available."}

def get_exercise(algorithm, level="beginner"):
    """
    Get an exercise for a specific algorithm and difficulty level
    
    Parameters:
    - algorithm: String, either 'DFS' or 'BFS'
    - level: String, the difficulty level (beginner, intermediate, advanced)
    
    Returns:
    - Dictionary with exercise details
    """
    exercises = {
        "DFS": {
            "beginner": {
                "question": "Given a graph with 5 nodes (0-4) where node 0 connects to nodes 1 and 2, node 1 connects to node 3, and node 2 connects to node 4, what would be the order of nodes visited in a DFS starting from node 0?",
                "answer": [0, 1, 3, 2, 4],
                "explanation": "DFS starting at node 0 would first visit 0, then go to neighbor 1, then to 1's neighbor 3. After exploring that branch fully, it would backtrack and visit node 2 from node 0, and finally node 4 from node 2.",
                "graph_definition": {
                    "nodes": 5,
                    "edges": [(0, 1), (0, 2), (1, 3), (2, 4)]
                }
            },
            "intermediate": {
                "question": "In a graph with cycles, how does DFS prevent infinite loops? Explain how you would implement this and provide the traversal order for a graph with nodes 0-3 where there are edges between (0,1), (1,2), (2,0), and (1,3), starting from node 0.",
                "answer": [0, 1, 2, 3],
                "explanation": "DFS prevents infinite loops by keeping track of visited nodes. When we visit a node, we mark it as visited and never visit it again, even if we encounter it multiple times during traversal. Starting from node 0, we visit 0, then 1, then 2. When node 2 examines its neighbor 0, it finds that 0 is already visited, so it doesn't visit it again. Then we backtrack to node 1 and visit its other neighbor 3.",
                "graph_definition": {
                    "nodes": 4,
                    "edges": [(0, 1), (1, 2), (2, 0), (1, 3)]
                }
            },
            "advanced": {
                "question": "Implement DFS to detect if a cycle exists in a directed graph. Explain how the algorithm works and apply it to a graph with nodes 0-4 and edges (0,1), (1,2), (2,0), (0,3), (3,4).",
                "answer": "True",
                "explanation": "To detect cycles in a directed graph using DFS, we need to keep track of nodes in the current recursion stack in addition to the visited set. If we encounter a node that's already in the recursion stack, we've found a cycle. In this graph, the cycle is 0→1→2→0. The algorithm would visit node 0, then 1, then 2, and when it examines 2's neighbors, it finds node 0 which is in the current recursion path, indicating a cycle.",
                "graph_definition": {
                    "nodes": 5,
                    "edges": [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4)],
                    "directed": True
                }
            }
        },
        "BFS": {
            "beginner": {
                "question": "Given a graph with 5 nodes (0-4) where node 0 connects to nodes 1 and 2, node 1 connects to node 3, and node 2 connects to node 4, what would be the order of nodes visited in a BFS starting from node 0?",
                "answer": [0, 1, 2, 3, 4],
                "explanation": "BFS explores all neighbors at the current level before moving to the next level. Starting at node 0, we first visit 0, then all its neighbors (1 and 2). Only after visiting all nodes at this level do we move to the next level and visit 3 (neighbor of 1) and 4 (neighbor of 2).",
                "graph_definition": {
                    "nodes": 5,
                    "edges": [(0, 1), (0, 2), (1, 3), (2, 4)]
                }
            },
            "intermediate": {
                "question": "In an unweighted graph, BFS can be used to find the shortest path between two nodes. Explain how this works and find the shortest path from node 0 to node 3 in a graph with nodes 0-4 and edges between (0,1), (0,2), (1,3), (2,4), (4,3).",
                "answer": [0, 1, 3],
                "explanation": "BFS visits nodes in order of their distance from the start node, so the first time we reach a target node will be via the shortest path. To track the path, we need to store the parent of each node during traversal. For this graph, BFS from 0 visits nodes in order [0, 1, 2, 3, 4]. The shortest path from 0 to 3 is [0, 1, 3] with length 2.",
                "graph_definition": {
                    "nodes": 5,
                    "edges": [(0, 1), (0, 2), (1, 3), (2, 4), (4, 3)]
                }
            },
            "advanced": {
                "question": "Implement a modified BFS to find the shortest path in a graph where each edge has a weight of either 1 or 2. Explain your approach and apply it to find the shortest path from node 0 to node 5 in a graph with nodes 0-5 and edges (0,1,1), (0,2,2), (1,3,1), (2,3,1), (2,4,1), (3,5,1), (4,5,2) where the third value is the edge weight.",
                "answer": [0, 1, 3, 5],
                "explanation": "For graphs with edge weights of 1 or 2, a modified BFS using a deque works. For edges with weight 1, add the new node to the front of the deque. For weight 2, add to the back. This ensures we always process nodes in order of their distance from start. In this graph, the path [0,1,3,5] has total weight 3, which is less than [0,2,3,5] (weight 4), [0,2,4,5] (weight 5), or any other path.",
                "graph_definition": {
                    "nodes": 6,
                    "edges": [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)],
                    "weights": {"(0,1)": 1, "(0,2)": 2, "(1,3)": 1, "(2,3)": 1, "(2,4)": 1, "(3,5)": 1, "(4,5)": 2}
                }
            }
        }
    }
    
    if algorithm in exercises and level in exercises[algorithm]:
        return exercises[algorithm][level]
    else:
        return {
            "question": "No exercise available for the selected algorithm and level.",
            "answer": None,
            "explanation": None,
            "graph_definition": None
        }

def get_algorithm_quiz(algorithm):
    """
    Get quiz questions for a specific algorithm
    
    Parameters:
    - algorithm: String, either 'DFS' or 'BFS'
    
    Returns:
    - List of dictionaries with quiz questions
    """
    quizzes = {
        "DFS": [
            {
                "question": "What data structure is used in the iterative implementation of DFS?",
                "options": ["Queue", "Stack", "Heap", "Array"],
                "correct_answer": "Stack",
                "explanation": "DFS uses a stack (either explicitly or through recursion) to keep track of nodes to visit. The stack's LIFO (Last In, First Out) property ensures we explore deeply first before backtracking."
            },
            {
                "question": "What is the time complexity of DFS?",
                "options": ["O(V)", "O(E)", "O(V + E)", "O(V * E)"],
                "correct_answer": "O(V + E)",
                "explanation": "DFS visits each vertex once (O(V)) and examines each edge once (O(E)), resulting in a total time complexity of O(V + E) where V is the number of vertices and E is the number of edges."
            },
            {
                "question": "Which of the following is NOT a common application of DFS?",
                "options": ["Topological sorting", "Finding connected components", "Finding the shortest path in an unweighted graph", "Detecting cycles in a graph"],
                "correct_answer": "Finding the shortest path in an unweighted graph",
                "explanation": "DFS does not guarantee finding the shortest path in an unweighted graph. BFS is better suited for this purpose. DFS is commonly used for topological sorting, finding connected components, and cycle detection."
            },
            {
                "question": "In DFS, when is a node marked as 'visited'?",
                "options": ["Before adding it to the stack", "After removing it from the stack", "When all its neighbors are explored", "When it's first discovered"],
                "correct_answer": "After removing it from the stack",
                "explanation": "In the iterative implementation of DFS, a node is typically marked as visited after it's removed from the stack and before its neighbors are explored. This ensures we don't visit the same node multiple times."
            },
            {
                "question": "What happens in DFS when it encounters a node that has already been visited?",
                "options": ["It visits it again", "It skips it and moves to the next node", "It stops the algorithm", "It backtracks to the previous node"],
                "correct_answer": "It skips it and moves to the next node",
                "explanation": "When DFS encounters a node that has already been visited, it skips that node to avoid cycles and infinite loops, and proceeds to the next node in the stack."
            }
        ],
        "BFS": [
            {
                "question": "What data structure is used in BFS?",
                "options": ["Stack", "Queue", "Heap", "Array"],
                "correct_answer": "Queue",
                "explanation": "BFS uses a queue to keep track of nodes to visit. The queue's FIFO (First In, First Out) property ensures we explore all nodes at a given distance before moving farther away."
            },
            {
                "question": "What is the time complexity of BFS?",
                "options": ["O(V)", "O(E)", "O(V + E)", "O(V * E)"],
                "correct_answer": "O(V + E)",
                "explanation": "BFS visits each vertex once (O(V)) and examines each edge once (O(E)), resulting in a total time complexity of O(V + E) where V is the number of vertices and E is the number of edges."
            },
            {
                "question": "Which of the following is a key advantage of BFS over DFS?",
                "options": ["Lower space complexity", "Guarantees shortest path in unweighted graphs", "Better for detecting cycles", "More efficient for sparse graphs"],
                "correct_answer": "Guarantees shortest path in unweighted graphs",
                "explanation": "BFS visits nodes in order of their distance from the start node, which guarantees that the first time a node is discovered will be via the shortest path from the start node in an unweighted graph."
            },
            {
                "question": "In BFS, nodes are processed in which order?",
                "options": ["Deepest first", "Random order", "In order of their degree (number of neighbors)", "Level by level"],
                "correct_answer": "Level by level",
                "explanation": "BFS processes all nodes at the current level (distance from the start) before moving to nodes at the next level. This level-by-level processing is a defining characteristic of BFS."
            },
            {
                "question": "Which application is BFS particularly well-suited for?",
                "options": ["Topological sorting", "Finding strongly connected components", "Finding shortest paths in unweighted graphs", "Solving puzzles with backtracking"],
                "correct_answer": "Finding shortest paths in unweighted graphs",
                "explanation": "BFS is particularly well-suited for finding shortest paths in unweighted graphs because it explores nodes in order of their distance from the start node."
            }
        ]
    }
    
    if algorithm in quizzes:
        return quizzes[algorithm]
    else:
        return []

def get_comparison_content():
    """
    Get content comparing DFS and BFS
    
    Returns:
    - Dictionary with comparison content
    """
    return {
        "title": "Comparing DFS and BFS",
        "content": """
# DFS vs BFS: A Comprehensive Comparison

## Basic Approach
- **DFS** explores as far as possible along a branch before backtracking
- **BFS** explores all neighbors before moving to the next level

## Data Structure
- **DFS** uses a stack (or recursion)
- **BFS** uses a queue

## Properties
| Property | DFS | BFS |
|----------|-----|-----|
| Space Complexity | O(h) - height of tree | O(w) - width of tree |
| Complete | No (can get stuck in infinite branches) | Yes (will find a solution if one exists) |
| Optimal | No (may not find shortest path) | Yes (for unweighted graphs) |

## Visual Comparison

```
Graph:
    A
   / \\
  B   C
 / \\   \\
D   E   F

DFS order (starting from A): A, B, D, E, C, F
BFS order (starting from A): A, B, C, D, E, F
```

## When to Use Each

### Use DFS when:
- Memory is limited
- Solutions are likely to be far from the root
- The graph may have deep branches
- You need to perform backtracking
- You're looking for topological orderings

### Use BFS when:
- You need the shortest path
- Memory is not a concern
- Solutions are likely near the root
- You need to explore level by level
- You're working with an unweighted graph and need optimal paths
        """
    }