import requests
import streamlit as st
import json


API_URL = "https://openrouter.ai/api/v1/chat/completions"

OPENROUTER_TOKEN = st.session_state.get("api_token", "Null")
MODEL = st.session_state.get("model", "meta-llama/llama-4-maverick")

if "api_token" not in st.session_state or not st.session_state.api_token:
    st.error("⚠️ No API token found. Please go back and enter your key.")
    st.stop()


# rag.py
import streamlit as st

def get_headers():
    token = st.session_state.get("api_token")
    if not token:
        st.error("API token missing. Please go back and enter your key.")
        st.stop()

    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

def get_model():
    return st.session_state.get("model", "meta-llama/llama-4-maverick")




HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_TOKEN}",
    "Content-Type": "application/json"
}


def chunkData(file) -> list:
    with open(file) as f:
        text = f.read()

    num_parts = 10

    full_stops_indices = [i for i, char in enumerate(text) if char == '.']
    full_stops_per_part = len(full_stops_indices) // num_parts
    split_indices = [full_stops_indices[(idx+1)*full_stops_per_part] for idx in range(num_parts-1)]

    parts = [text[i:j] for i, j in zip([0] + split_indices, split_indices + [None])]

    return parts


def extract_answer(generated_text):
    if "Answer:" in generated_text:
        return generated_text.split("Answer:")[-1].strip()
    return generated_text.strip()


def query_openrouter(prompt, context, model=MODEL):
    full_prompt = f"""You are an AI assistant. Based on the following context, provide a complete and detailed response, which are directions.

    Context:
    {context}

    User Question: {prompt}
    Answer:"""

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": full_prompt}
        ],
        "temperature": 0.5
    }

    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}", 0.0

    result = response.json()
    try:
        content = result['choices'][0]['message']['content']
        return extract_answer(content), 1.0
    except Exception as e:
        return f"Parsing Error: {str(e)}", 0.0


def reply(prompt, context_parts):
    answers_dict = {}
    for i, part in enumerate(context_parts):
        answer, confidence = query_openrouter(prompt, part)
        answers_dict[f"Chunk {i+1}"] = {answer: confidence}
    best_answer = max(answers_dict.values(), key=lambda x: list(x.values())[0])
    best_text = list(best_answer.keys())[0]
    return best_text

