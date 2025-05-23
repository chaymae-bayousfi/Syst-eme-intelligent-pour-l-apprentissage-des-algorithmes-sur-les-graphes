import openai
import streamlit as st
import os

# Initialize OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")  # Replace with your actual API key or use environment variable

def get_explanation(algorithm, step_data, current_step, total_steps):
    """
    Get a step-by-step explanation from the LLM for the current algorithm state.
    
    Parameters:
    - algorithm: String specifying the algorithm (DFS or BFS)
    - step_data: Dictionary with step information
    - current_step: Current step index
    - total_steps: Total number of steps
    
    Returns:
    - String explanation
    """
    # If API key is not available, return a predefined explanation
    if not openai.api_key or openai.api_key == "your-api-key-here":
        return get_default_explanation(algorithm, step_data, current_step, total_steps)
    
    try:
        # Construct the prompt for the LLM
        prompt = f"""
        You are an expert computer science tutor explaining graph algorithms to a student.
        The student is learning the {algorithm} algorithm and is currently at step {current_step + 1} of {total_steps}.
        
        Current algorithm state:
        - {"Stack" if algorithm == "DFS" else "Queue"}: {step_data.get('stack' if algorithm == 'DFS' else 'queue', [])}
        - Visited nodes: {step_data.get('visited', [])}
        - Current node: {step_data.get('current', 'None')}
        - Exploration order so far: {step_data.get('exploration_order', [])}
        
        Please provide a clear, step-by-step explanation of what is happening at this point in the algorithm.
        Explain the current step, why it's important, and how it relates to the overall algorithm.
        Use educational tone and include any relevant theoretical concepts.
        Keep your explanation concise (150-200 words).
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" for a less expensive option
            messages=[
                {"role": "system", "content": "You are an expert computer science tutor."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.5
        )
        
        return response.choices[0].message['content']
    
    except Exception as e:
        st.error(f"Error communicating with OpenAI API: {str(e)}")
        return get_default_explanation(algorithm, step_data, current_step, total_steps)

def get_conversation_response(question, algorithm, current_state, chat_history):
    """
    Get a response from the LLM for a user's question about the algorithm.
    
    Parameters:
    - question: The user's question
    - algorithm: String specifying the algorithm (DFS or BFS)
    - current_state: Dictionary with current algorithm state
    - chat_history: List of previous chat messages
    
    Returns:
    - String response
    """
    # If API key is not available, return a predefined response
    if not openai.api_key or openai.api_key == "your-api-key-here":
        return get_default_conversation_response(question, algorithm)
    
    try:
        # Construct the conversation history
        messages = [
            {"role": "system", "content": f"""
            You are an expert computer science tutor specializing in graph algorithms, particularly {algorithm}.
            You're currently helping a student understand how {algorithm} works and answering their questions.
            Keep your explanations clear, educational, and concise (around 150 words).
            Use analogies and examples when helpful.
            """}
        ]
        
        # Add chat history
        for message in chat_history[-6:]:  # Only include the last 6 messages to save tokens
            messages.append({"role": message["role"], "content": message["content"]})
        
        # Add current algorithm state context
        if current_state:
            state_desc = f"""
            Current algorithm state:
            - {"Stack" if algorithm == "DFS" else "Queue"}: {current_state.get('stack' if algorithm == 'DFS' else 'queue', [])}
            - Visited nodes: {current_state.get('visited', [])}
            - Current node: {current_state.get('current', 'None')}
            - Exploration order so far: {current_state.get('exploration_order', [])}
            """
            messages.append({"role": "system", "content": state_desc})
        
        # Add the current question
        messages.append({"role": "user", "content": question})
        
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" for a less expensive option
            messages=messages,
            max_tokens=300,
            temperature=0.7
        )
        
        return response.choices[0].message['content']
    
    except Exception as e:
        st.error(f"Error communicating with OpenAI API: {str(e)}")
        return get_default_conversation_response(question, algorithm)

def get_default_explanation(algorithm, step_data, current_step, total_steps):
    """Provide a default explanation when the LLM is not available."""
    if not step_data.get('description'):
        return "This step shows the progression of the algorithm. Notice how nodes are visited in a specific order based on the algorithm's traversal strategy."
    
    return step_data['description'] + "\n\n" + (
        f"In {algorithm}, we explore the graph {'deeply (by going as far as possible along a branch)' if algorithm == 'DFS' else 'broadly (by exploring all neighbors before moving to the next level)'} "
        f"before backtracking. This is why we use a {'stack' if algorithm == 'DFS' else 'queue'} data structure to keep track of nodes to visit next."
    )

def get_default_conversation_response(question, algorithm):
    """Provide a default response when the LLM is not available."""
    return (
        "I'm currently operating without LLM integration. Please check your OpenAI API key configuration to enable full conversational capabilities.\n\n"
        f"For questions about {algorithm}, I recommend referring to the algorithm description in the sidebar and watching the visualization step by step."
    )