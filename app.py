import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

def llm_judge(submission: str, rubric: str):
    prompt = f"""
    You are a strict judge. Evaluate the following submission against the rubric.

    Rubric:
    {rubric}

    Submission:
    {submission}

    Provide:
    1. A score (0-10)
    2. Detailed feedback
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",   # Groq supported model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content

# Streamlit UI
st.title("LLM Judge with Groq 🏛️")

rubric = st.text_area("Enter Rubric (criteria for evaluation):")
submission = st.text_area("Enter Submission (essay/code/answer):")

if st.button("Judge Now"):
    if rubric and submission:
        result = llm_judge(submission, rubric)
        st.subheader("Judge Output")
        st.write(result)
    else:
        st.warning("Please enter both rubric and submission.")