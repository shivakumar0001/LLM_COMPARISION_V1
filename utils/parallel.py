from concurrent.futures import ThreadPoolExecutor
from models.chatgpt_model import chatgpt_response
from models.gemini_model import gemini_response
from models.llama_model import llama_response

def run_parallel(prompt: str) -> dict:
    responses = {}

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            "ChatGPT": executor.submit(chatgpt_response, prompt),
            "Gemini": executor.submit(gemini_response, prompt),
            "LLaMA": executor.submit(llama_response, prompt)
        }

        for model, future in futures.items():
            try:
                responses[model] = future.result()
            except Exception as e:
                responses[model] = f"Error: {str(e)}"

    return responses