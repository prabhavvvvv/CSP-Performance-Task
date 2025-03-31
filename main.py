import random

# I used copilot to give me a general function layout for this function
def get_weather_history(days):
    history = []
    weather_options = ["sunny", "rainy", "cloudy", "snowy"]
    print("These are the available weather options: ", weather_options)
    print(f"Enter the weather for last {days} days:")
    for i in range(days):
        weather = input(f"Day {i + 1} weather: ").lower()
        while weather not in weather_options:
            print("Invalid weather, please try again")
            weather = input(f"Day {i + 1} weather: ").lower()

        try:
            temperature_input = int(input(f"Day {i + 1} temperature (whole integer): "))
        except:
            print("Invalid, please enter an appropriate number")
            temperature_input = int(input(f"Day {i + 1 } temperature (whole integer): "))
        history.append(weather)
    return history

def trends(history):
    weather_occurences = {}
    for weather in history:
        if weather in weather_occurences:
            weather_occurences[weather] +=1
        else:
            weather_occurences[weather] = 1
        return weather_occurences
        
        
def analyze(history):
    weather_occurences = trends(history)
    most_frequent_weather = max(weather_occurences, key = weather_occurences.get)
    print(f"The most frequent weather is: {most_frequent_weather}")
    return most_frequent_weather

def random_weather():
    weather_options = ["sunny", "rainy", "cloudy", "snowy"]
    return random.choices(weather_options)

def calculate_temperature(history):
    return sum(temp for i, temp in histoy)

history = get_weather_history(5)
analyze(history)
predicted_weather = random_weather()
predicted_temperature = random_temperature()
print(f"The expected weather for tomorrow: {random_weather()} with a temperature of {random_temperature}")
