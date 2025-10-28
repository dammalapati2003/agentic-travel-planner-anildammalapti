# itinerary_creator.py

def itinerary_creator(state):
    """Creates a daily itinerary based on POIs and weather info."""
    try:
        pois = state.get("pois", [])
        weather = state.get("weather", [])
        dates = state.get("dates", [])

        itinerary = []
        poi_index = 0
        total_pois = len(pois)

        for i, date in enumerate(dates, start=1):
            w = weather[i - 1] if i - 1 < len(weather) else {"condition": "N/A", "temp": "--"}

            # Select 3 POIs morning, afternoon, evening
            day_pois = []
            for _ in range(3):
                if poi_index < total_pois:
                    day_pois.append(pois[poi_index])
                    poi_index += 1
                else:
                    day_pois.append({"name": "Free Time"})

            itinerary.append({
                "day": i,
                "date": date,
                "morning": day_pois[0]["name"],
                "afternoon": day_pois[1]["name"],
                "evening": day_pois[2]["name"],
                "notes": f"{w['condition']}, {w['temp']}°C"
            })

        state["itinerary"] = itinerary
    except Exception as e:
        state["itinerary_error"] = str(e)
        state["itinerary"] = []
    return state


def display_output(state):
    """Prints all results neatly with cost and time estimates."""
    print("\n Weather Info:")
    if "weather" in state and state["weather"]:
        for w in state["weather"]:
            print(f"• {w['day']}: {w['condition']}, {w['temp']}°C")
    else:
        print("   Weather data unavailable.")

    print("\n Points of Interest (with Time & Cost):")
    if "pois" in state and state["pois"]:
        for p in state["pois"]:
            print(
                f"• {p['name']} – {p['desc']} | Visit Time: {p.get('visit_time','N/A')} | "
                f"Cost: {p.get('cost','N/A')} | Travel to next: {p.get('travel_time_to_next','N/A')}"
            )
    else:
        print("   No POIs found.")

    print("\n Travel Itinerary:\n")
    print(f"{'Day':<5}{'Morning':<30}{'Afternoon':<30}{'Evening':<30}{'Notes':<25}")
    print("-" * 130)

    for i in state.get("itinerary", []):
        print(f"{i['day']:<5}{i['morning']:<30}{i['afternoon']:<30}{i['evening']:<30}{i['notes']:<25}")

    print("\n Travel plan generated successfully!\n")
