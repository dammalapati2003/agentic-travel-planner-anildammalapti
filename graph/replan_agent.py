# replan_agent.py
from graph.poi_agent import poi_agent
from graph.itinerary_creator import itinerary_creator

def replan_if_weather_changes(state):
    """Detects rain and replans itinerary with indoor POIs."""
    if not state.get("weather"):
        return state

    if any(w["condition"] in ["Rainy", "Stormy"] for w in state["weather"]):
        print("\n Weather alert: Rainy days detected!")
        choice = input("Would you like to replan with indoor activities? (yes/no): ").strip().lower()
        if choice == "yes":
            print("\n Replanning with indoor-friendly POIs (Historic / Shopping)...\n")
            state["pois"], state["itinerary"] = [], []  
            state = poi_agent(state, override_pref="Historic")
            state = itinerary_creator(state)
    return state
