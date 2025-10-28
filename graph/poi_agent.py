# poi_agent.py
from data_feed import POI_DATA
import random


def poi_agent(state, override_pref=None):
    """
    Fetches Points of Interest for the given city and user preference.
    Pulls from data_feed.py. Adds cost, visit time, and travel time info.
    """
    try:
        # Extract info from current state
        pref = (override_pref or state.get("preference", "general")).lower()
        city = state.get("city", "Default")

        # Get city
        city_pois = POI_DATA.get(city, POI_DATA["Default"])

        # Get POIs based on user preference 
        pois = city_pois.get(pref, city_pois.get("general", []))

        # If no POIs found, fallback to default set
        if not pois:
            pois = POI_DATA["Default"]["general"]

        # Random shuffle for variety
        random.shuffle(pois)

        
        for p in pois:
            if "visit_time" not in p:
                p["visit_time"] = f"{random.randint(1, 3)} hrs"
            if "cost" not in p:
                p["cost"] = f"${random.randint(10, 50)}"
            if "travel_time_to_next" not in p:
                p["travel_time_to_next"] = f"{random.randint(10, 40)} mins"

        # Store results in state
        state["pois"] = pois

        # Print summary for clarity
        print("\n Points of Interest (based on your preference):")
        for p in pois:
            print(
                f"• {p['name']} – {p['desc']} | Visit Time: {p['visit_time']} | "
                f"Cost: {p['cost']} | Travel to next: {p['travel_time_to_next']}"
            )

    except Exception as e:
        state["poi_error"] = f"POI agent failed: {e}"
        state["pois"] = []
        print(f" POI agent encountered an error: {e}")

    return state
