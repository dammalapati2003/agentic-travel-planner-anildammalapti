# llm_decision.py

import re

def llm_decision_node(state):
    """
    Decides which agents to call based on user's natural language input.
    Prevents accidental triggers like 'hi' matching 'trip' or 'poi'.
    """
    user_input = state.get("user_input", "").strip().lower()
    state["next_agents"] = []

    print("\n LLM Decision: Analyzing your input...")

    # Tokenize input data
    words = re.findall(r"\b\w+\b", user_input)

    # Define intent keywords
    intents = {
        "plan_trip": {"plan", "trip", "travel", "vacation"},
        "weather": {"weather", "temperature", "forecast"},
        "poi": {"places", "poi", "spots", "tourist", "attractions", "visit"},
        "replan": {"replan", "change", "adjust", "update", "modify"}
    }

    matched = []

    for intent, keywords in intents.items():
        if any(word in words for word in keywords):
            matched.append(intent)

    # Decision logic 
    if "plan_trip" in matched:
        state["next_agents"].extend(["weather_agent", "poi_agent", "itinerary_creator", "replan_agent"])
    elif "weather" in matched:
        state["next_agents"].append("weather_agent")
    elif "poi" in matched:
        state["next_agents"].append("poi_agent")
    elif "replan" in matched:
        state["next_agents"].append("replan_agent")
    else:
        print("\n I didn’t detect a travel-related request.")
        print("Try one of these examples:")
        print('    "Plan a 2-day trip to New Delhi starting tomorrow."')
        print('    "What’s the weather in Paris next week?"')
        print('    "Show me tourist attractions in Tokyo."')
        print('    "Replan my Dubai trip if the weather changes."')
        return state  

    print(f" Tools selected by LLM: {', '.join(state['next_agents'])}")
    return state
