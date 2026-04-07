import requests
import json


URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen3.5"

print("=== Local Ollama Chat ===")
print("Type 'exit' to quit.\n")

# data = {
#     "model": "qwen3.5",
#     "prompt": prompt,
#     "max_tokens": 300
# }

# try:
#     r = requests.post(url, json=data, stream=True, timeout=60)
#     print("Status code:", r.status_code)
#     print("Response text:", r.text)
# except requests.exceptions.RequestException as e:
#     print(f"Error: {e}")


while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat.")
        break

    data = {
        "model": MODEL,
        "prompt": user_input,
        "max_tokens": 300
    }

    try:
        r = requests.post(URL, json=data, stream=True, timeout=60)
    except Exception as e:
        print("Error:", e)
        continue

    final_text = ""
    print("AI: ", end="", flush=True)

    for line in r.iter_lines(decode_unicode=True):
        if line:
            obj = json.loads(line)
            thinking = obj.get("thinking", "")
            if thinking:
                print(thinking, end="", flush=True)
                final_text += thinking
            if obj.get("done", False):
                break

    print("\n")

    if final_text:
        print(final_text)