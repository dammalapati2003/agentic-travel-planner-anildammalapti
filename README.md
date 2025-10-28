# AI Agent Challenge: Multi-Agent Travel Planning System

## 1. Setup Instructions

### Requirements
- Python 3.10  
- No external API keys needed  
- All modules are written using built in Python libraries  

### Steps to Run
1. Clone or download the project repository.  
   ```bash
   git clone https://github.com/<yourname>/agentic-travel-planner.git
   cd agentic-travel-planner
   ```

3. Install dependencies (if `requirements.txt` is present).  
   ```bash
   pip install -r requirements.txt
   ```

4. Run the main file.  
   ```bash
   python main.py
   ```



## 2. LangGraph Design

The project is designed using a **LangGraph inspired architecture**. Each component acts as a separate “agent” node, connected in a logical workflow.  

### Graph Nodes
| Node | Description |
|------|--------------|
| **Input Handler** | Reads and interprets user input. |
| **LLM Decision Node** | Decides which agents to call based on the prompt. |
| **Weather Agent** | Fetches weather information for given travel dates. |
| **POI Agent** | Retrieves city specific points of interest. |
| **Itinerary Creator** | Builds the final travel itinerary. |
| **Replan Agent** | Adjusts plans if weather conditions change. |

### Flow Diagram
```
User Input
   ↓
Input Handler
   ↓
LLM Decision Node
   ↓
 ┌──────────────┬──────────────┐
 │ Weather Agent│ POI Agent    │
 └──────┬───────┴──────┬───────┘
        ↓               ↓
        → Itinerary Creator
               ↓
           Replan Agent
               ↓
           Final Output
```

Each agent updates a shared `state` dictionary, ensuring smooth data exchange between nodes.

---

## 3. Example Runs and Outputs

### Example 1
**User Input:**  
```
Plan a 2-day trip to New Delhi starting tomorrow.
```

**Output:**
```
Weather Info:
• Day 1 (Oct 28, 2025): Sunny, 34°C
• Day 2 (Oct 29, 2025): Cloudy, 31°C

Points of Interest:
• Red Fort – Historic site
• India Gate – Famous landmark
• Qutub Minar – UNESCO monument
• Lotus Temple – Iconic modern temple
• Connaught Place – Shopping and food hub

Travel Itinerary:
Day   Morning                Afternoon              Evening               Weather
1     Red Fort               India Gate             Connaught Place        Sunny, 34°C
2     Qutub Minar            Lotus Temple           Free Time              Cloudy, 31°C
```

---

### Example 2
**User Input:**  
```
Plan a 3-day trip to Paris for culture.
```

**Output:**
```
Weather Info:
• Day 1 (Oct 28, 2025): Sunny, 25°C
• Day 2 (Oct 29, 2025): Cloudy, 26°C
• Day 3 (Oct 30, 2025): Rainy, 24°C

Points of Interest:
• Eiffel Tower – Iconic landmark
• Louvre Museum – Art museum
• Notre-Dame Cathedral – Gothic masterpiece
• Montmartre – Cultural district
• Seine River Cruise – Scenic water tour

Travel Itinerary:
Day   Morning                Afternoon              Evening               Weather
1     Eiffel Tower           Louvre Museum          Montmartre            Sunny, 25°C
2     Notre-Dame Cathedral   Seine River Cruise     Free Time             Cloudy, 26°C
3     Free Time              Free Time              Free Time             Rainy, 24°C
```

---

## 4. Notes on Assumptions, Limitations, and Possible Improvements

### Assumptions
- Input follows a pattern like “Plan a 3 day trip to Tokyo starting tomorrow.”  
- Weather and POI data are from static, predefined datasets.  
- Dates are automatically generated based on the current system date.

### Limitations
- No live data from external APIs.  
- Only one city per query.  
- Weather and POIs are mock values for demonstration purposes.  
- LLM decision making is simulated through rule based logic.

### Possible Improvements
1. Integrate real APIs (OpenWeather, Google Places).  
2. Support multi city or multi country trips.  
3. Add cost and time optimization between POIs.  
4. Include user preferences for budget or travel style.  
5. Build a web or Streamlit UI for easier interaction.

