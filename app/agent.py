from google.adk.agents import Agent
from google.adk.tools import google_search 


agent = Agent(
   # A unique name for the agent.
   name="basic_search_agent",
   model="gemini-2.0-flash-exp", 
   description="Agent to answer questions using Google Search.",
   instruction="You are an expert researcher. You always stick to the facts.",
   tools=[google_search]
)

# This is required for the ADK CLI to recognize and run the agent
if __name__ == "__main__":
    from google.adk.cli import run_agent
    run_agent(agent)