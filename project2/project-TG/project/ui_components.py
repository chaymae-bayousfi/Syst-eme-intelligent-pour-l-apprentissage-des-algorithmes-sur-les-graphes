import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from io import BytesIO
import base64

from graph_utils import create_sample_graph, visualize_graph, get_node_colors, add_node_to_graph, add_edge_to_graph
from algorithms import dfs_algorithm, bfs_algorithm, get_algorithm_properties
from llm_integration import get_explanation, get_hint, get_chat_response
from tutorials import get_tutorial_content, get_exercise, get_algorithm_quiz, get_comparison_content

def sidebar():
    """Create and manage the sidebar elements"""
    st.sidebar.title("Graph Algorithm Tutor")
    
    # Algorithm selection
    st.sidebar.header("Algorithm Settings")
    algorithm = st.sidebar.radio("Select Algorithm", ["DFS", "BFS"])
    
    # Update session state
    if algorithm != st.session_state.algorithm:
        st.session_state.algorithm = algorithm
        st.session_state.algorithm_steps = []
        st.session_state.current_step = 0
    
    # User level selection
    user_level = st.sidebar.select_slider(
        "Your Knowledge Level",
        options=["Beginner", "Intermediate", "Advanced"],
        value="Beginner"
    )
    
    # Graph options
    st.sidebar.header("Graph Settings")
    
    if st.sidebar.button("Generate New Graph"):
        num_nodes = st.sidebar.number_input("Number of Nodes", min_value=3, max_value=10, value=6)
        edge_probability = st.sidebar.slider("Edge Density", min_value=0.1, max_value=0.9, value=0.4, step=0.1)
        directed = st.sidebar.checkbox("Directed Graph", value=False)
        
        # Create new graph
        st.session_state.graph = create_sample_graph(
            num_nodes=num_nodes,
            edge_probability=edge_probability,
            directed=directed
        )
        st.session_state.algorithm_steps = []
        st.session_state.current_step = 0
        st.session_state.start_node = 0
    
    # Display algorithm properties
    st.sidebar.header("Algorithm Properties")
    properties = get_algorithm_properties()[algorithm]
    
    st.sidebar.markdown(f"**{properties['full_name']}**")
    st.sidebar.markdown(f"- Uses: {properties['data_structure']}")
    st.sidebar.markdown(f"- Time: {properties['time_complexity']}")
    st.sidebar.markdown(f"- Space: {properties['space_complexity']}")
    
    # API Key input
    st.sidebar.header("GPT Integration")
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    if api_key:
        st.sidebar.success("API Key set!")
    
    # Add the key to environment variables
    if api_key:
        import os
        os.environ["OPENAI_API_KEY"] = api_key

def tutorial_ui():
    """Display tutorial content"""
    st.header(f"{st.session_state.algorithm} Tutorial")
    
    # Tutorial sections
    sections = ["introduction", "pseudocode", "time_complexity", "applications", "comparison"]
    section_names = ["Introduction", "Pseudocode", "Time & Space Complexity", "Applications", "Comparison with " + ("BFS" if st.session_state.algorithm == "DFS" else "DFS")]
    
    # Create tabs for different sections
    tabs = st.tabs(section_names)
    
    # Fill each tab with content
    for i, section in enumerate(sections):
        with tabs[i]:
            content = get_tutorial_content(st.session_state.algorithm, section)
            st.markdown(content["content"])
    
    # Add a chat interface for questions
    st.header("Have Questions?")
    
    # Initialize messages if not already done
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    prompt = st.chat_input(f"Ask a question about {st.session_state.algorithm}...")
    
    if prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_chat_response(st.session_state.messages, st.session_state.algorithm)
                st.markdown(response)
        
        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

def practice_ui():
    """Display practice exercises"""
    st.header("Practice Exercises")
    
    # Level selection
    level = st.selectbox("Difficulty Level", ["beginner", "intermediate", "advanced"], 
                         format_func=lambda x: x.capitalize())
    
    # Get exercise for the selected algorithm and level
    exercise = get_exercise(st.session_state.algorithm, level)
    
    # Display exercise
    st.subheader("Exercise")
    st.markdown(exercise["question"])
    
    # Display graph if available
    if exercise["graph_definition"]:
        graph_def = exercise["graph_definition"]
        G = nx.Graph() if not graph_def.get("directed", False) else nx.DiGraph()
        
        # Add nodes
        for i in range(graph_def["nodes"]):
            G.add_node(i)
            
        # Add edges
        for edge in graph_def["edges"]:
            G.add_edge(edge[0], edge[1])
        
        # Visualize
        plt_fig = visualize_graph(G, title="Exercise Graph")
        st.pyplot(plt_fig)
        plt.close()
    
    # User answer input
    user_answer = st.text_area("Your Answer", height=100)
    
    # Check button
    if st.button("Submit Answer"):
        if not user_answer.strip():
            st.warning("Please provide an answer before submitting.")
        else:
            # Show feedback
            st.subheader("Feedback")
            
            if "answer" in exercise and exercise["answer"]:
                with st.expander("Correct Answer", expanded=True):
                    st.write(exercise["answer"])
                
                with st.expander("Explanation", expanded=True):
                    st.write(exercise["explanation"])
                    
                # Get personalized feedback using LLM
                with st.spinner("Analyzing your answer..."):
                    st.subheader("AI Analysis of Your Answer")
                    hint = get_hint(f"Is this answer correct for the question: {exercise['question']}? The answer given is: {user_answer}. The correct answer is {exercise['answer']}.", st.session_state.algorithm, level)
                    st.write(hint)
            else:
                st.info("No reference answer available for this exercise.")
    
    # Quiz section
    st.header("Quiz")
    quiz_questions = get_algorithm_quiz(st.session_state.algorithm)
    
    if quiz_questions:
        # Select a random question
        if 'current_quiz_question' not in st.session_state:
            st.session_state.current_quiz_question = np.random.choice(len(quiz_questions))
            st.session_state.quiz_answered = False
        
        question = quiz_questions[st.session_state.current_quiz_question]
        
        st.subheader(question["question"])
        
        # Radio buttons for options
        answer = st.radio(
            "Select your answer:",
            question["options"],
            key=f"quiz_radio_{st.session_state.current_quiz_question}"
        )
        
        # Check answer button
        if st.button("Check Answer"):
            st.session_state.quiz_answered = True
            
            if answer == question["correct_answer"]:
                st.success("Correct! 🎉")
            else:
                st.error(f"Incorrect. The correct answer is: {question['correct_answer']}")
            
            st.info(question["explanation"])
        
        # Next question button
        if st.session_state.quiz_answered and st.button("Next Question"):
            # Choose a different question
            prev_question = st.session_state.current_quiz_question
            while st.session_state.current_quiz_question == prev_question:
                st.session_state.current_quiz_question = np.random.choice(len(quiz_questions))
            st.session_state.quiz_answered = False
            st.experimental_rerun()

def visualization_ui():
    """Display algorithm visualization"""
    st.header("Algorithm Visualization")
    
    # Graph display
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if not st.session_state.algorithm_steps:
            # Regular graph visualization
            plt_fig = visualize_graph(
                st.session_state.graph, 
                title=f"Graph Visualization"
            )
            st.pyplot(plt_fig)
            plt.close()
        else:
            # Show current step
            step = st.session_state.algorithm_steps[st.session_state.current_step]
            
            # Get node colors based on visited status
            node_colors = get_node_colors(
                st.session_state.graph,
                visited=step.get('visited', []),
                current=step.get('current')
            )
            
            # Highlight edges if any
            edges = step.get('edges', [])
            
            # Visualize
            plt_fig = visualize_graph(
                st.session_state.graph,
                node_colors=node_colors,
                highlighted_edges=edges,
                title=f"{st.session_state.algorithm} Step {st.session_state.current_step+1}/{len(st.session_state.algorithm_steps)}"
            )
            st.pyplot(plt_fig)
            plt.close()
    
    with col2:
        st.subheader("Algorithm Controls")
        
        # Start node selection
        start_node = st.selectbox(
            "Starting Node",
            sorted(list(st.session_state.graph.nodes())),
            index=0
        )
        
        # Only update if different from current
        if start_node != st.session_state.start_node:
            st.session_state.start_node = start_node
            st.session_state.algorithm_steps = []
            st.session_state.current_step = 0
        
        # Run algorithm button
        if st.button(f"Run {st.session_state.algorithm}"):
            with st.spinner(f"Running {st.session_state.algorithm}..."):
                if st.session_state.algorithm == "DFS":
                    st.session_state.algorithm_steps = dfs_algorithm(
                        st.session_state.graph, 
                        st.session_state.start_node
                    )
                else:  # BFS
                    st.session_state.algorithm_steps = bfs_algorithm(
                        st.session_state.graph,
                        st.session_state.start_node
                    )
                st.session_state.current_step = 0
                st.success(f"{st.session_state.algorithm} completed!")
    
    # Step navigation
    if st.session_state.algorithm_steps:
        col1, col2, col3 = st.columns([1, 3, 1])
        
        with col1:
            if st.button("⏮️ First"):
                st.session_state.current_step = 0
            if st.button("◀️ Previous") and st.session_state.current_step > 0:
                st.session_state.current_step -= 1
                
        with col2:
            # Step slider
            step = st.slider(
                "Current Step",
                0,
                len(st.session_state.algorithm_steps) - 1,
                st.session_state.current_step
            )
            if step != st.session_state.current_step:
                st.session_state.current_step = step
                
        with col3:
            if st.button("Next ▶️") and st.session_state.current_step < len(st.session_state.algorithm_steps) - 1:
                st.session_state.current_step += 1
            if st.button("Last ⏭️"):
                st.session_state.current_step = len(st.session_state.algorithm_steps) - 1
        
        # Display current step information
        current_step = st.session_state.algorithm_steps[st.session_state.current_step]
        
        # Step explanation
        st.subheader("Step Explanation")
        st.markdown(current_step.get('explanation', 'No explanation available.'))
        
        # Data structure state
        st.subheader("Data Structure State")
        if st.session_state.algorithm == "DFS":
            st.markdown(f"**Stack**: {current_step.get('stack', [])}")
        else:  # BFS
            st.markdown(f"**Queue**: {current_step.get('queue', [])}")
        
        # Visited nodes
        st.markdown(f"**Visited Nodes**: {current_step.get('visited', [])}")
        
        # Get detailed explanation from GPT if API key is provided
        if "OPENAI_API_KEY" in st.secrets or "OPENAI_API_KEY" in os.environ:
            with st.expander("AI-Powered Explanation", expanded=True):
                with st.spinner("Getting detailed explanation..."):
                    explanation = get_explanation(
                        st.session_state.algorithm,
                        current_step
                    )
                    st.markdown(explanation)
                    
        # Offer hint
        with st.expander("Need a hint?"):
            hint_question = st.text_input("Ask for a hint about this step")
            if hint_question:
                with st.spinner("Generating hint..."):
                    hint = get_hint(hint_question, st.session_state.algorithm)
                    st.markdown(hint)
    
    # Graph editing tools
    st.header("Graph Editor")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Add Node/Edge")
        
        # Add node
        if st.button("Add Node"):
            st.session_state.graph = add_node_to_graph(st.session_state.graph)
            st.session_state.algorithm_steps = []
            st.success(f"Node {len(st.session_state.graph.nodes())-1} added!")
            st.experimental_rerun()
        
        # Add edge
        edge_from = st.selectbox("Edge From", sorted(list(st.session_state.graph.nodes())), key="edge_from")
        edge_to = st.selectbox("Edge To", sorted(list(st.session_state.graph.nodes())), key="edge_to")
        
        if st.button("Add Edge"):
            if edge_from != edge_to:
                if st.session_state.graph.has_edge(edge_from, edge_to):
                    st.warning(f"Edge ({edge_from}, {edge_to}) already exists!")
                else:
                    st.session_state.graph = add_edge_to_graph(st.session_state.graph, edge_from, edge_to)
                    st.session_state.algorithm_steps = []
                    st.success(f"Edge ({edge_from}, {edge_to}) added!")
                    st.experimental_rerun()
            else:
                st.warning("Cannot add self-loop (edge to the same node)!")
    
    with col2:
        st.subheader("Graph Information")
        
        st.markdown(f"**Nodes**: {len(st.session_state.graph.nodes())}")
        st.markdown(f"**Edges**: {len(st.session_state.graph.edges())}")
        
        if nx.is_connected(st.session_state.graph):
            st.success("Graph is connected")
        else:
            st.warning("Graph is not connected")
            
        if nx.has_path(st.session_state.graph, st.session_state.start_node, list(st.session_state.graph.nodes())[-1]):
            st.success(f"Path exists from node {st.session_state.start_node} to node {list(st.session_state.graph.nodes())[-1]}")
        else:
            st.warning(f"No path from node {st.session_state.start_node} to node {list(st.session_state.graph.nodes())[-1]}")