import speech_recognition as sr
import pyttsx3
import random

# Initialize text to speech engine
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet():
    responses = ["Hello! I'm Alexa. What can I do for you?",
                 "Hi there! How can I assist you today?",
                 "Hey! What do you need help with?"]
    speak(random.choice(responses))

# Function to respond to user command
def respond(command):
    command = command.lower()
    if "weather" in command:
        speak("The weather today is sunny.")
    elif "time" in command:
        speak("The current time is 10:00 AM.")
    elif "joke" in command:
        jokes = ["Why don't scientists trust atoms? Because they make up everything!",
                 "Parallel lines have so much in common. It’s a shame they’ll never meet.",
                 "I told my wife she was drawing her eyebrows too high. She looked surprised."]
        speak(random.choice(jokes))
    elif "bye" in command:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("I'm sorry, I didn't understand that.")

# Main function
def main():
    greet()
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            respond(command)
        except sr.UnknownValueError:
            print("Sorry, I didn't get that. Please try again.")
        except sr.RequestError:
            print("Sorry, I'm having trouble accessing the Google API. Please try again later.")

if __name__ == "__main__":
    main()
