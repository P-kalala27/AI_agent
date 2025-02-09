import requests
from config.config import API_URL, Huggingface_Api_Key





HEADERS = {
    "Authorization": f"Bearer {Huggingface_Api_Key}"
}

def query_hugging_api(prompt):
    payload  = {
        "inputs": prompt,
        "options": {
            "wait_for_model": True
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.status_code} - {response.text}"



# if __name__ == "__main__":
#     prompt = "what is the useful of kubernetes?"
#     print(query_hugging_api(prompt))
    




