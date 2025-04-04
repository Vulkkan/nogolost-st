import requests
# from helper.key import API_TOKEN


# API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
# Kinda works
# API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"

# HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}
HEADERS = {"Authorization": ""}

def set_api_token(token):
    HEADERS["Authorization"] = f"Bearer {token}"
    

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
    """
    Given the full LLM output, extract just the answer part.
    """
    if "Answer:" in generated_text:
        return generated_text.split("Answer:")[-1].strip()
    return generated_text.strip()


# def answers(context, prompt):
#     instruction = (
#         f"Based on the following context, give complete and detailed directions to the user.\n\n"
#         f"Context:\n{context}\n\n"
#         f"User Question: {prompt}\n\n"
#         f"Answer:"
#     )

#     data = {
#         "inputs": instruction,
#         "parameters": {
#             "temperature": 0.7,
#             "max_new_tokens": 250,
#             "do_sample": True,
#         }
#     }

#     response = requests.post(API_URL, headers=HEADERS, json=data)

#     if response.status_code != 200:
#         return (
#             f"Error: {response.status_code}. Response: {response.text}",
#             0.0
#         )

#     try:
#         result = response.json()
#         generated_text = result[0]['generated_text']
#         return generated_text, 1.0
#     except Exception as e:
#         return f"Error parsing response: {e}", 0.0

def answers(context, prompt):
    data = {"inputs": f"Based on the following context, give complete and detailed directions to the user.\n\nContext:\n{context}\n\nUser Question: {prompt}"}
    import requests
    response = requests.post(API_URL, headers=HEADERS, json=data)
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}", 0.0
    result = response.json()
    if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
        return result[0]["generated_text"], 1.0
    return str(result), 0.5

def reply(prompt, context_parts) -> str:
    answers_dict = {}
    for i, part in enumerate(context_parts):
        answer, confidence = answers(part, prompt)
        answers_dict[f"Chunk {i+1}"] = {answer: confidence}
    best_answer = max(answers_dict.values(), key=lambda x: list(x.values())[0])
    best_text = list(best_answer.keys())[0]
    return best_text