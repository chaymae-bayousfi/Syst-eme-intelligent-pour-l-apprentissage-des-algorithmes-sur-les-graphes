import streamlit as st
import os
from dotenv import load_dotenv

from graph_utils import create_sample_graph, visualize_graph
from algorithms import dfs_algorithm, bfs_algorithm
from llm_integration import get_explanation, get_hint
from tutorials import get_tutorial_content, get_exercise
from ui_components import sidebar, tutorial_ui, practice_ui, visualization_ui

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Graph Algorithm Tutor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if they don't exist
if 'graph' not in st.session_state:
    st.session_state.graph = create_sample_graph()
if 'algorithm' not in st.session_state:
    st.session_state.algorithm = "DFS"
if 'algorithm_steps' not in st.session_state:
    st.session_state.algorithm_steps = []
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'start_node' not in st.session_state:
    st.session_state.start_node = 0
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'exercise_mode' not in st.session_state:
    st.session_state.exercise_mode = False
if 'current_exercise' not in st.session_state:
    st.session_state.current_exercise = None

def main():
    # Add custom CSS
    st.markdown(
        """
        <style>
        .main {
            background-color: #f5f5f5;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # App title
    st.title("Graph Algorithm Intelligent Tutor")
    
    # Display sidebar
    sidebar()
    
    # Main content tabs
    tab1, tab2, tab3 = st.tabs(["Learn", "Practice", "Visualize"])
    
    with tab1:
        tutorial_ui()
        
    with tab2:
        practice_ui()
        
    with tab3:
        visualization_ui()

if __name__ == "__main__":
    main()