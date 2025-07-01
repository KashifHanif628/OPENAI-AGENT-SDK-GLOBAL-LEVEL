# 🌐 3. Global-Level Configuration (main_global.py)
Yeh project ke saray agents ko by default Gemini use karne pe set karta hai, bina har agent me alag se client pass kiye.

MATLAB, Aap apne poore project me Google Gemini ko default model bana dete ho, taake har agent, har run, bina bar bar Gemini model specify kiye, automatic Gemini use kare.

# 🔁 Fark kya hai Agent-Level se?

# Agent Level                   	    Global Level
Sirf ek agent Gemini use kare	        Saare agents Gemini use karein
Har agent me client dena padta hai	    Ek baar global config set kar do


# CODE LINE BY LINE UNDERSTANDING.

# from dotenv import load_dotenv
# import os
📌 Yeh lines .env file ko read karne ke liye hain — yeh file me Gemini ki API key hoti hai:
 GEMINI_API_KEY=your_gemini_api_key_here


# from openai import AsyncOpenAI
# from agents import Agent, Runner, set_default_openai_client, set_tracing_disabled, set_default_openai_api
📌 Yahan se hum sab zaroori cheezein import kar rahe hain:

AsyncOpenAI: Gemini client banane ke liye
Agent: Assistant banane ke liye
Runner: Us agent ko run karne ke liye
set_default_openai_client: Yeh sabse important hai — yeh Gemini ko global default client bana deta hai
set_tracing_disabled: Tracking band karne ke liye
set_default_openai_api: Batata hai ke hum chat wali API use kar rahe hain


# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
📌 Yeh .env file ko load karke aapki Gemini API key ko variable me store karta hai.


# set_tracing_disabled(True)
📌 Yeh tracing yaani internal logging ko disable kar deta hai — optional hai.


# set_default_openai_api("chat_completions")
📌 Hum Google Gemini ka chat model use kar rahe hain — isliye yeh batana zaroori hai.


# external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

📌 Yeh line Gemini client banati hai, jo API key aur URL ke zariye Google se baat karega.


# set_default_openai_client(external_client)
📌 💡 Yeh sabse important step hai!
Yeh line Google Gemini ko poore project ka default model provider bana deti hai. Ab aapko har agent me alag se client nahi dena padega.


# agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gemini-2.0-flash"
)
📌 Ab jab aap agent banate ho, to sirf model ka naam dete ho.
Gemini client already globally set hai — isliye woh wahi use karega.


# result = Runner.run_sync(agent, "What's recursion in programming?")
# print("👉 Global-Level Response:\n", result.final_output)
📌 Yahan hum agent se question kar rahe hain aur jo answer milega woh print kar denge.



# ✅ Summary (Super Easy Zubaan Me)
Kya Karta Hai	                Matlab
set_default_openai_client()	    Gemini ko default client bana deta hai poore project ke liye

set_default_openai_api()	    Batata hai ke hum chat API use kar rahe hain

agent = Agent(...)	            Simple agent ban jata hai, client separately dene ki zarurat nahi

Runner.run_sync(...)	        Agent se baat kar ke reply leta hai


