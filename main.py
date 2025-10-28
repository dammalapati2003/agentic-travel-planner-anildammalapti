# main.py

from graph.input_handler import input_handler
from graph.llm_decision import llm_decision_node
from graph.weather_agent import weather_agent
from graph.poi_agent import poi_agent
from graph.itinerary_creator import itinerary_creator, display_output
from graph.replan_agent import replan_if_weather_changes


def travel_graph():
    """Simulates the LangGraph orchestration of all nodes (agents)."""

    print("\n Welcome to the AI Travel Planner!\n")

    while True:
        try:
            # 1️ Input Handler Node
            state = input_handler()
            if not state or not state.get("user_input"):
                print(" No valid input provided. Please try again.\n")
                continue

            # 2️ LLM Decision Node
            state = llm_decision_node(state)

            # If no tools were selected, ask again
            if not state.get("next_agents"):
                print("\n Let's try again!\n")
                continue

            # 3️ Tool Invocation 
            if "weather_agent" in state["next_agents"]:
                state = weather_agent(state)
            if "poi_agent" in state["next_agents"]:
                state = poi_agent(state)
            if "itinerary_creator" in state["next_agents"]:
                state = itinerary_creator(state)
                display_output(state)
            if "replan_agent" in state["next_agents"]:
                state = replan_if_weather_changes(state)

            print("\n Workflow completed successfully.\n")

            # Ask user if they want to plan another trip
            again = input("Do you want to plan another trip? (yes/no): ").strip().lower()
            if again not in ["yes", "y"]:
                print("\n Thanks for using the AI Travel Planner. Safe travels!\n")
                break

        except Exception as e:
            print(f" An unexpected error occurred: {e}")
            continue


if __name__ == "__main__":
    travel_graph()
