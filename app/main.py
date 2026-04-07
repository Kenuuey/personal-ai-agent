from app.agent.agent import Agent
from app.llm.client import LLMClient
from app.tools.file_reader import FileReaderTool

llm = LLMClient()
tools = [FileReaderTool()]

agent = Agent(llm=llm, tools=tools, memory=None)

while True:
    user_input = input(">> ")
    print(agent.run(user_input))