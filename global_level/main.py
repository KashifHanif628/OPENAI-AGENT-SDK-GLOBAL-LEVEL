from dotenv import load_dotenv
import os

from openai import AsyncOpenAI
from agents import Agent, Runner, set_default_openai_client, set_tracing_disabled, set_default_openai_api

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)

agent = Agent(name="Assistant", instructions="You are a helpful assistant", model="gemini-2.0-flash")

result = Runner.run_sync(agent, "Tell me about Pakistan Geography?")
print("👉 Global-Level Response:\n", result.final_output)
