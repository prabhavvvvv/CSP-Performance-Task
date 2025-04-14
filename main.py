import random

def get_weather_history(days):
    history = []
    weather_options = ["sunny", "rainy", "cloudy", "snowy"]
    print("These are the available weather options: ", weather_options)
    print(f"Enter the weather for the last {days} days:")
    for i in range(days):
        weather = input(f"Day {i + 1} weather: ").lower() # copilot taught me how to increment each index by 1
        while weather not in weather_options:
            print("Invalid weather, please try again")
            weather = input(f"Day {i + 1} weather: ").lower()
        
        try:
            temperature_input = int(input(f"Day {i + 1} temperature (whole integer) in F: "))
            
        except ValueError:
            print("Invalid, please enter an appropriate number")
            temperature_input = int(input(f"Day {i + 1} temperature (whole integer): in F ")) # copy and pasted

        # conditionals that render selection
        if weather == "sunny":
            print("Don't forget to wear sunscreen")
        elif weather == "rainy":
            print("Bring an umbrella")
        elif weather == "cloudy":
            print("Prepare for ran")
        elif weather == "snowy":
            print("Wear a jacket")
        
        history.append({"weather": weather, "temperature": temperature_input})
    return history

def trends(history):
    # creates an empty list where the user's weather inputs are stored
    weather_occurences = {}
    for day in history:
        weather = day["weather"]
        if weather in weather_occurences:
            weather_occurences[weather] += 1 # <- used copilot to know how to increment the weather 
        else:
            weather_occurences[weather] = 1  # <- used copilot to know how to increment the weather
    return weather_occurences # end of copilot

def analyze(history):
    # takes the trend in the weather occurences and renders the most accurate prediction based on the previous history
    weather_occurences = trends(history)
    most_frequent_weather = max(weather_occurences, key=weather_occurences.get) # I didn't know how to get the info from the database, so I asked copilot and it gave me a key command to store it
    print(f"The most frequent weather is: {most_frequent_weather}") # end of copilot
    return most_frequent_weather

def random_weather():
    weather_options = ["sunny", "rainy", "cloudy", "snowy"]
    return random.choice(weather_options)

def calculate_temperature(history):
    return sum(day["temperature"] for day in history) / len(history)
    example = [30, 55, 45, 60, 80, 100, 45]
    example.append(45)


history = get_weather_history(5)
analyze(history)

predicted_weather = random_weather()
predicted_temperature = calculate_temperature(history)
