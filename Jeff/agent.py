from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages.ai import AIMessage
from tools import get_availability

from dotenv import load_dotenv
load_dotenv()

memory=MemorySaver()

class JeffAgent():
    def __init__(self):
        self.model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")
        self.tools=[get_availability]
        self.system_prompt="Your are a scheduling personal assistant for Jeff.\n"
        "You can check Jeff's get_availability_tool on specific dates using the provided tool.\n"
        "Provide clear and concise responses based on Jeff's availability.\n"
        "If Jeff is not available on a requested date, suggest alternative dates if possible.\n"

        self.graph=create_agent(
            self.model,
            tools=self.tools,
            system_prompt=self.system_prompt,
            checkpointer= memory
        )
    async def get_response(self, query, context_id):
        inputs={"messages": [("user", query)]}
        config={"configurable": {"thread_id": context_id}}
        response=self.graph.invoke(inputs, config)
        messages=response.get["messages", []]
        ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
        response=ai_messages[-1] if ai_messages else "No response from AI."
        return {"content": response}


agent=JeffAgent()
import asyncio
response=asyncio.run(agent.get_response(query="Is Jeff available on 2025-11-11?", context_id=1234))
print(response)