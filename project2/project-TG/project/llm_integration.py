import openai
import streamlit as st
import os

# Set up OpenAI API
def setup_openai():
    """Set up the OpenAI API with the API key from environment"""
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        openai.api_key = api_key
        return True
    else:
        st.warning("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
        return False

def get_explanation(algorithm, step_data, level="beginner"):
    """
    Get a detailed explanation of a specific algorithm step from GPT
    
    Parameters:
    - algorithm: String, either 'DFS' or 'BFS'
    - step_data: Dictionary containing data about the current step
    - level: String indicating the expertise level (beginner, intermediate, advanced)
    
    Returns:
    - String with the explanation
    """
    if not setup_openai():
        return "GPT integration not available. Please set your OpenAI API key."
    
    # Prepare prompt based on algorithm and step
    visited = step_data.get('visited', [])
    current = step_data.get('current')
    
    if algorithm == "DFS":
        stack = step_data.get('stack', [])
        data_structure_state = f"Stack: {stack}"
    else:  # BFS
        queue = step_data.get('queue', [])
        data_structure_state = f"Queue: {queue}"
    
    edges = step_data.get('edges', [])
    
    prompt = f"""
    Explain the following step of the {algorithm} algorithm to a {level} student:
    
    Current node: {current if current is not None else 'None'}
    Visited nodes so far: {visited}
    {data_structure_state}
    Edges being added in this step: {edges}
    
    Please explain:
    1. What's happening in this step
    2. Why it's happening
    3. How this relates to the {algorithm} algorithm principles
    
    Keep your explanation concise and educational, focusing on helping the student understand the algorithm.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" depending on your needs
            messages=[
                {"role": "system", "content": "You are a helpful tutor explaining graph algorithms."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error getting explanation: {str(e)}"

def get_hint(question, algorithm, level="beginner"):
    """
    Get a hint for a student's question about the algorithm
    
    Parameters:
    - question: Student's question
    - algorithm: String, either 'DFS' or 'BFS'
    - level: String indicating the expertise level
    
    Returns:
    - String with the hint
    """
    if not setup_openai():
        return "GPT integration not available. Please set your OpenAI API key."
    
    prompt = f"""
    A {level} student learning about the {algorithm} algorithm asks:
    
    "{question}"
    
    Give a helpful hint that guides them towards understanding without giving away the complete answer. Explain the concept in a way that's appropriate for their expertise level.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" depending on your needs
            messages=[
                {"role": "system", "content": "You are a helpful tutor explaining graph algorithms."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error getting hint: {str(e)}"

def evaluate_answer(student_answer, correct_answer, algorithm, context=None):
    """
    Evaluate a student's answer to a question about the algorithm
    
    Parameters:
    - student_answer: Student's answer
    - correct_answer: Correct answer to compare against
    - algorithm: String, either 'DFS' or 'BFS'
    - context: Additional context about the question
    
    Returns:
    - Dictionary with evaluation results
    """
    if not setup_openai():
        return {"score": 0, "feedback": "GPT integration not available. Please set your OpenAI API key."}
    
    prompt = f"""
    Evaluate this student's answer about the {algorithm} algorithm.
    
    Question context: {context if context else 'General question about the ' + algorithm + ' algorithm'}
    
    Correct answer: {correct_answer}
    
    Student's answer: {student_answer}
    
    Please provide:
    1. A score from 0-100
    2. Specific feedback about what was correct and what could be improved
    3. A brief explanation of any misconceptions
    
    Format your response as a JSON object with these keys: score, feedback, misconceptions
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" depending on your needs
            messages=[
                {"role": "system", "content": "You are a helpful tutor evaluating understanding of graph algorithms."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250,
            temperature=0.3
        )
        
        feedback = response.choices[0].message.content.strip()
        
        # Simple parsing of JSON-like response
        import json
        try:
            result = json.loads(feedback)
            return result
        except:
            # Fallback if GPT doesn't return valid JSON
            return {
                "score": 50,
                "feedback": feedback,
                "misconceptions": "Unable to parse specific misconceptions."
            }
            
    except Exception as e:
        return {
            "score": 0,
            "feedback": f"Error evaluating answer: {str(e)}",
            "misconceptions": "Unable to evaluate due to an error."
        }

def get_chat_response(messages, algorithm):
    """
    Get a chat response from the LLM based on conversation history
    
    Parameters:
    - messages: List of previous message dictionaries with 'role' and 'content'
    - algorithm: String, either 'DFS' or 'BFS'
    
    Returns:
    - String with the assistant's response
    """
    if not setup_openai():
        return "GPT integration not available. Please set your OpenAI API key."
    
    # Create system message with context about the algorithm
    system_message = f"""
    You are an intelligent tutoring system specializing in graph algorithms, particularly {algorithm}.
    Your goal is to help students understand the algorithm through conversation.
    
    - Explain concepts clearly and concisely
    - Use analogies when helpful
    - If asked about code, provide Python examples
    - If the student is confused, try different approaches to explanation
    - Keep responses focused on helping the student learn {algorithm}
    
    Your teaching approach should be socratic - guide the student to discover the answer rather than just telling them.
    """
    
    # Prepare the full message list including the system message
    full_messages = [
        {"role": "system", "content": system_message}
    ] + messages
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" depending on your needs
            messages=full_messages,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error getting response: {str(e)}"