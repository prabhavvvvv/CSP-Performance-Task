import random

# I used copilot to give me a general function layout for this function
def get_weather_history(days):
    history = []
    print("Enter the weather for last {days} days:")
    for i in range(days):
        weather = input(f"Day {i + 1}: ")
        history.append(weather)
    return history

def trends(history):
    weather_occurences = []
    for weather in history:
        if weather in history:
            weather_occurences[weather] +=1
        else:
            weather_occurences[weather] = 1
        return weather_occurences
        
        
def anaylyze(history):
    weather_occurences = trends(history)
    
