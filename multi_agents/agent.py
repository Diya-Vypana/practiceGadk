from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

AGENT_MODEL = "ollama/gemma4:12b"

root_agent = Agent(
    name="travel_planner",
    model=LiteLlm(AGENT_MODEL),
    description="A travel planning agent that helps users plan their trips, find destinations, and create itineraries.",
    instruction="You are a travel planning assistant. You can help users find destinations, create itineraries, and provide travel advice. Keep it brief."
)