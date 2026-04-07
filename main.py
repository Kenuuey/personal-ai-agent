import requests


url = "http://localhost:11434/api/generate"

prompt = input("Prompt: ")

data = {
    "model": "qwen3.5",
    "prompt": prompt,
    "max_tokens": 300
}

response = requests.post(url, json=data)

output = response.json()["response"]

print("Ollama output:\n", output)