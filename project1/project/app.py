import streamlit as st
from modules.graph_utils import create_random_graph, get_graph_info
from modules.algorithms import dfs, bfs
from modules.visualization import visualize_graph, visualize_algorithm_step
from modules.llm_integration import get_explanation, get_conversation_response
from modules.tutorial_content import algorithm_descriptions
from modules.exercises import generate_exercise, verify_solution

st.set_page_config(
    page_title="Graph Algorithm Tutor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if they don't exist
if 'graph' not in st.session_state:
    st.session_state.graph = create_random_graph(7)
if 'algorithm' not in st.session_state:
    st.session_state.algorithm = "DFS"
if 'start_node' not in st.session_state:
    st.session_state.start_node = 0
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'algorithm_steps' not in st.session_state:
    st.session_state.algorithm_steps = []
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'exercise_mode' not in st.session_state:
    st.session_state.exercise_mode = False
if 'exercise' not in st.session_state:
    st.session_state.exercise = None

# Sidebar for algorithm selection and graph customization
with st.sidebar:
    st.title("Graph Algorithm Tutor")
    
    # Algorithm selection
    st.header("Algorithm")
    algorithm = st.radio(
        "Select an algorithm to learn:",
        ["DFS (Depth-First Search)", "BFS (Breadth-First Search)"]
    )
    st.session_state.algorithm = "DFS" if "DFS" in algorithm else "BFS"
    
    # Display algorithm description
    st.markdown(algorithm_descriptions[st.session_state.algorithm])
    
    # Graph customization
    st.header("Graph Settings")
    graph_type = st.radio("Graph type:", ["Random", "Custom"])
    
    if graph_type == "Random":
        nodes = st.slider("Number of nodes:", 4, 15, 7)
        if st.button("Generate New Random Graph"):
            st.session_state.graph = create_random_graph(nodes)
            st.session_state.start_node = 0
            st.session_state.current_step = 0
            st.session_state.algorithm_steps = []
    else:
        st.text("Custom graph coming soon...")
        # This would be implemented with a more complex interface
    
    # Start node selection
    st.header("Start Node")
    start_node = st.number_input(
        "Select starting node:", 
        min_value=0, 
        max_value=len(st.session_state.graph.nodes)-1, 
        value=st.session_state.start_node
    )
    st.session_state.start_node = start_node
    
    # Exercise mode toggle
    st.header("Exercise Mode")
    exercise_toggle = st.checkbox("Enable Exercise Mode", value=st.session_state.exercise_mode)
    if exercise_toggle != st.session_state.exercise_mode:
        st.session_state.exercise_mode = exercise_toggle
        if exercise_toggle:
            st.session_state.exercise = generate_exercise(st.session_state.algorithm)
        else:
            st.session_state.exercise = None

# Main content area
col1, col2 = st.columns([3, 2])

with col1:
    # Graph visualization area
    st.header(f"{st.session_state.algorithm} Visualization")
    
    if st.session_state.exercise_mode and st.session_state.exercise:
        st.subheader("Exercise")
        st.markdown(st.session_state.exercise["description"])
        
    # Execute algorithm if needed
    if not st.session_state.algorithm_steps:
        if st.session_state.algorithm == "DFS":
            st.session_state.algorithm_steps = dfs(st.session_state.graph, st.session_state.start_node)
        else:
            st.session_state.algorithm_steps = bfs(st.session_state.graph, st.session_state.start_node)
    
    # Visualization
    if st.session_state.current_step < len(st.session_state.algorithm_steps):
        current_state = st.session_state.algorithm_steps[st.session_state.current_step]
        fig = visualize_algorithm_step(st.session_state.graph, current_state, st.session_state.algorithm)
        st.pyplot(fig)
    else:
        fig = visualize_graph(st.session_state.graph)
        st.pyplot(fig)
    
    # Algorithm navigation controls
    col1a, col1b, col1c = st.columns(3)
    
    with col1a:
        if st.button("⏮️ Reset") and len(st.session_state.algorithm_steps) > 0:
            st.session_state.current_step = 0
    
    with col1b:
        if st.button("⏪ Previous Step") and st.session_state.current_step > 0:
            st.session_state.current_step -= 1
    
    with col1c:
        if st.button("Next Step ⏩") and st.session_state.current_step < len(st.session_state.algorithm_steps) - 1:
            st.session_state.current_step += 1

with col2:
    # Explanation and conversation area
    if st.session_state.exercise_mode and st.session_state.exercise:
        st.header("Exercise")
        
        user_solution = st.text_area("Your solution:")
        
        if st.button("Check Solution"):
            result, feedback = verify_solution(
                st.session_state.exercise, 
                user_solution, 
                st.session_state.algorithm
            )
            if result:
                st.success("Correct! " + feedback)
            else:
                st.error("Not quite right. " + feedback)
    else:
        st.header("Step Explanation")
        
        if st.session_state.current_step < len(st.session_state.algorithm_steps):
            current_state = st.session_state.algorithm_steps[st.session_state.current_step]
            explanation = get_explanation(
                st.session_state.algorithm,
                current_state,
                st.session_state.current_step,
                len(st.session_state.algorithm_steps)
            )
            st.markdown(explanation)
        
        # Conversation area
        st.header("Ask a Question")
        
        # Display chat history
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(f"**Tutor:** {message['content']}")
        
        # Input for new questions
        user_question = st.text_input("Type your question here:")
        
        if st.button("Send") and user_question:
            st.session_state.chat_history.append({"role": "user", "content": user_question})
            
            response = get_conversation_response(
                question=user_question,
                algorithm=st.session_state.algorithm,
                current_state=st.session_state.algorithm_steps[st.session_state.current_step] 
                if st.session_state.current_step < len(st.session_state.algorithm_steps) else None,
                chat_history=st.session_state.chat_history
            )
            
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.experimental_rerun()

# Display algorithm stats
if not st.session_state.exercise_mode:
    st.header("Algorithm Statistics")
    
    if st.session_state.algorithm_steps:
        total_steps = len(st.session_state.algorithm_steps)
        visited_nodes = len(set(node for step in st.session_state.algorithm_steps for node in step["visited"]))
        
        col_stats1, col_stats2, col_stats3 = st.columns(3)
        col_stats1.metric("Total Steps", total_steps)
        col_stats2.metric("Visited Nodes", visited_nodes)
        col_stats3.metric("Completion", f"{(st.session_state.current_step + 1) / total_steps * 100:.1f}%")