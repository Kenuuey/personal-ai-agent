class Agent:
    def __init__(self, llm, tools, memory):
        self.llm = llm
        self.tools = tools
        self.memory = memory

    def run(self, user_input):
        messages = [{"role": "user", "content": user_input}]

        # Step 1: think
        response = self.llm.chat(messages)

        # Step 2: detect tool usage (simplified)
        if "USE_TOOL" in response:
            tool_name = "file_reader"
            tool_result = self.tools[tool_name].run("data.txt")

            messages.append({"role": "tool", "content": tool_result})
            response = self.llm.chat(messages)

        return response