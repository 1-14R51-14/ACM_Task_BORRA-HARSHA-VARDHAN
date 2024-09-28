import streamlit as st
import google.generativeai as genai

# Configure the Google Generative AI module
genai.configure(api_key="AIzaSyAL_T-aOIbZXaBtZuheDmPJ2_MKrpeBAV0")  

# Initialize the model
model = genai.GenerativeModel("gemini-pro")

# Define a function to get a response from the model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Set up the Streamlit app configuration
st.set_page_config(page_title="Gemini Pro Chatbot")
st.header("Gemini Pro Chatbot")

# Initialize session state for chat history if it doesn't exist
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Recursive function to display chat
def rec_fun():
    # Text input for user to ask a question
    input = st.text_input("Ask something:", key="user_input")
    
    # Button to submit the query
    if st.button("Generate Response"):
        if input.lower() not in ["quit", "exit", "bye"]:
            # Get the response from Gemini Pro
            response = get_gemini_response(input)
            
            # Store the input and response in session state
            st.session_state['history'].append({"question": input, "response": response})
    
    # Display the chat history
    if st.session_state['history']:
        for chat in st.session_state['history']:
            st.write(f"You: {chat['question']}")
            st.write(f"Gemini Pro: {chat['response']}")

# Call the recursive function
rec_fun()
