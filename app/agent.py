from google.adk.agents import Agent

agent = Agent(
    name="general_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about general subjects."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about general subjects in the world."
    ),
    # CAN HAVE HELPER FUNCTIONS!!!
    #tools=[get_weather, get_current_time],
)

# This is required for the ADK CLI to recognize and run the agent
if __name__ == "__main__":
    from google.adk.cli import run_agent
    run_agent(agent)