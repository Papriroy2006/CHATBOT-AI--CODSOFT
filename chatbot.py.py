import datetime
import os
import webbrowser
import random
import requests
import pyowm 

def open_website(website_name):
    supported_websites = {
        'google': 'https://www.google.com',
        'youtube': 'https://www.youtube.com',
        'github': 'https://github.com'
        # Add more supported websites here
    }
    try:
        if website_name in supported_websites:
            webbrowser.open(supported_websites[website_name])
            return f"Opening {website_name}..."
        else:
            return f"Sorry, I don't support opening {website_name} at the moment."
    except Exception as e:
        return f"Error opening {website_name}: {e}"

def open_software(software_name):
    supported_software = {
        'calculator': 'calc',
        'notepad': 'notepad.exe',
        'paint': 'mspaint.exe'
        # Add more supported software here
    }

    try:
        if software_name in supported_software:
            os.system(supported_software[software_name])
            return f"Opening {software_name}..."
        else:
            return f"Sorry, I don't support opening {software_name} as software at the moment."
    except Exception as e:
        return f"Error opening {software_name}: {e}"

def open_search_engine(query, search_engine):
    search_engine_urls = {
        'google': f"https://www.google.com/search?q={query.replace(' ', '+')}",
        'bing': f"https://www.bing.com/search?q={query.replace(' ', '+')}"
        # Add more search engines here
    }
    try:
        if search_engine in search_engine_urls:
            webbrowser.open(search_engine_urls[search_engine])
            return f"Searching for '{query}' on {search_engine.capitalize()}..."
        else:
            return f"Sorry, {search_engine.capitalize()} search is not supported at the moment."
    except Exception as e:
        return f"Error searching for '{query}' on {search_engine.capitalize()}: {e}"

def get_current_date_time():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")

def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(base_url)
        data = response.json()
        temperature = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        return f"The current temperature in {city} is {temperature}°C with {weather_desc}."
    except Exception as e:
        return f"Error fetching weather information for {city}: {e}"

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a fake noodle? An impasta!"
        # Add more jokes here
    ]
    return random.choice(jokes)

def set_reminder(reminder):
    # You can implement reminder functionality here
    return "Reminder set successfully!"

def papri_chatbot(user_input):

    if "hello" in user_input.lower():
        return "Hey there! How can I assist you today?"
    elif "how are you" in user_input.lower():
        return "I'm functioning perfectly fine, thank you! How about yourself?"
    elif "i am fine" in user_input.lower():
        return "Glad to hear that!"
    elif "what is your name" in user_input.lower():
        return "I am Papri, your Personal Chatbot. How can I be of service?"
    elif "who created you" in user_input.lower():
        return "I was brought into existence by a skilled developer. You can call it a collaborative effort!"
    elif "can you help me" in user_input.lower():
        return "Absolutely! Just tell me what you need assistance with."
    elif "what is today's date" in user_input.lower():
        return f"The current date is {get_current_date_time().split()[0]}."
    elif "what's the time now" in user_input.lower():
        return f"The current time is {get_current_date_time().split()[1]}."

    elif "open website" in user_input.lower():
        website_name = user_input.lower().replace("open website", "").strip()
        return open_website(website_name)
    elif "open software" in user_input.lower():
        software_name = user_input.lower().replace("open software", "").strip()
        return open_software(software_name)

    elif "search on" in user_input.lower():
        query = user_input.lower().split("search on")[-1].strip()
        search_engine = user_input.lower().split("search on")[0].strip()
        return open_search_engine(query, search_engine)

    elif "tell me a joke" in user_input.lower():
        return tell_joke()

    elif "what is the weather in" in user_input.lower():
        city = user_input.lower().replace("what is the weather in", "").strip()
        return get_weather(city)

    elif "set a reminder" in user_input.lower():
        reminder = user_input.lower().replace("set a reminder", "").strip()
        return set_reminder(reminder)
    
    else:
        return "I'm sorry, I didn't quite catch that. Can you please rephrase?"

while True:
    user_input = input("You: ")
        
    if user_input.lower() == "exit":
        print("Goodbye! Have a great day.")
        break

    response = papri_chatbot(user_input)
    print("Papri:", response)