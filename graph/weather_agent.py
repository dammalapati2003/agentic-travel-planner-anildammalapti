# weather_agent.py
from datetime import datetime
from data_feed import WEATHER_DATA


def weather_agent(state):
    """
    Generates realistic weather data for the given city and dates.
    Uses static patterns from data_feed.py and formats results
    as required by the project (e.g., Day 1 (Sep 24, 2025): Sunny, 34°C).
    """
    try:
        city = state.get("city", "Default")
        dates = state.get("dates", [])

        # Fetch city weather pattern
        weather_info = WEATHER_DATA.get(city, WEATHER_DATA["Default"])

        pattern = weather_info["pattern"]
        avg_temp = weather_info["avg_temp"]

        weather_data = []

        for i, d in enumerate(dates):
            condition = pattern[i % len(pattern)]
            temp = avg_temp + ((i % 3) - 1) * 2  
            formatted_date = datetime.strptime(d, "%Y-%m-%d").strftime("%b %d, %Y")
            day_name = f"Day {i + 1} ({formatted_date})"
            weather_data.append({
                "day": day_name,
                "condition": condition,
                "temp": temp
            })

        # Save results in state
        state["weather"] = weather_data

    except Exception as e:
        state["weather_error"] = f"Weather agent failed: {e}"
        state["weather"] = []
        print(f" Weather agent encountered an error: {e}")

    return state
