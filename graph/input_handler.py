# input_handler.py
from datetime import datetime, timedelta
import re

def input_handler():
    """Handles user input and extracts city, dates, and preferences from a natural prompt."""
    while True:
        try:
            user_input = input("\n Enter your travel request: ").strip()

            # Handle empty or greeting-only inputs
            if not user_input or user_input.lower() in ["hi", "hello", "hey"]:
                print("\n Hi there! I can help you plan your trip.")
                print("Try something like:")
                print('    "Plan a 3-day trip to Tokyo starting after 2 days."')
                print('    "What’s the weather in London next week?"')
                print('    "Show me tourist attractions in Paris."')
                continue  # ask again

            # Make sure the input sounds travel related
            if not re.search(r"\b(trip|travel|plan|vacation|to)\b", user_input, re.IGNORECASE):
                print("\n That doesn’t sound like a travel request.")
                print("Try one of these examples:")
                print('    "Plan a 2-day trip to New Delhi starting tomorrow."')
                print('    "Check weather in Paris next week."')
                print('    "Show me tourist attractions in Tokyo."')
                continue  # re-ask

            state = {"user_input": user_input}

            # Try to extract city 
            city_match = re.search(r"to ([A-Za-z\s]+?)(?: starting| for| after|$)", user_input, re.IGNORECASE)
            city = city_match.group(1).strip().title() if city_match else None

            # Extract number of days
            days_match = re.search(r"(\d+)[-\s]*day", user_input)
            num_days = int(days_match.group(1)) if days_match else 2  # default 2 days

            # Extract offset 
            offset_match = re.search(r"after (\d+)", user_input)
            offset = int(offset_match.group(1)) if offset_match else 0

            # Determine start date
            start_date = datetime.now() + timedelta(days=offset)
            dates = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(num_days)]

            # Extract preference from text if mentioned
            preference_match = re.search(
                r"(food|nature|culture|historic|adventure|shopping)",
                user_input,
                re.IGNORECASE
            )
            preference = preference_match.group(1).lower() if preference_match else None

            # Ask for preference if not found
            if not preference:
                while True:  
                    print("\n Travel Preference Options:")
                    print("   1. Food")
                    print("   2. Nature")
                    print("   3. Culture")
                    print("   4. Historic")
                    print("   5. Adventure")
                    print("   6. Shopping")
                    choice = input("\nPlease choose your travel preference (1-6 only): ").strip()

                    if choice in ["1", "2", "3", "4", "5", "6"]:
                        options = {
                            "1": "food",
                            "2": "nature",
                            "3": "culture",
                            "4": "historic",
                            "5": "adventure",
                            "6": "shopping"
                        }
                        preference = options[choice]
                        break
                    else:
                        print(" Invalid input. Please enter a number between 1 and 6 only.\n")

            # Validate city
            if not city or len(city) < 2 or not city.replace(" ", "").isalpha():
                print("\n Couldn’t find a valid city in your request. Try again (e.g., 'trip to Paris').")
                continue  # re-ask

            # Store everything in the state
            state.update({
                "city": city,
                "dates": dates,
                "num_days": num_days,
                "preference": preference
            })

            return state

        except Exception as e:
            print(f" Error reading input: {e}")
            continue  # re-ask if any error
