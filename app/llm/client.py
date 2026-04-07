from openai import OpenAI

class LLMClient:
    def __init__(self, model="gpt-4.1"):
        self.client = OpenAI()
        self.model = model

    def chat(self, messages):
        """
        messages: lit of dicts  [{"role": "user"/"assistant"/"system", "content": "..."}]
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return response.choices[0].message.content