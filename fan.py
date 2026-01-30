import random
import json
import os
from datetime import datetime
QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Everything you've ever wanted is on the other side of fear. - George Addair",
    "Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine. - Roy T. Bennett",
    "I learned that courage was not the absence of fear, but the triumph over it. - Nelson Mandela",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn't just find you. You have to go out and get it."
]
MOOD_FILE = "mood_history.json"
def display_banner():
    """Display a welcome banner"""
    print("\n" + "="*50)
    print("  DAILY MOTIVATION APP  ".center(50))
    print("="*50 + "\n")
def get_random_quote():
    """Return a random motivational quote"""
    return random.choice(QUOTES)
def display_quote():
    """Display a motivational quote"""
    quote = get_random_quote()
    print(" Your Daily Motivation:\n")
    print(f"   \"{quote}\"\n")
def track_mood():
    """Allow user to track their mood"""
    print("How are you feeling today?")
    print("1 - Not great")
    print("2 - Okay")
    print("3 - Good")
    print("4 - Great")
    print("5 - Amazing!")
    while True:
        try:
            mood = input("\nEnter your mood (1-5): ").strip()
            mood_num = int(mood)
            if 1 <= mood_num <= 5:
                save_mood(mood_num)
                mood_messages = {
                    1: "I'm sorry you're not feeling great. Remember, tough times don't last, but tough people do! ",
                    2: "That's okay! Every day is a new opportunity to feel better. Keep going! ",
                    3: "That's good to hear! Keep up the positive vibes! ",
                    4: "Great! Ride that wave of positivity! ",
                    5: "Amazing! Share that energy with the world! "
                }
                print(f"\n{mood_messages[mood_num]}\n")
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
def save_mood(mood):
    """Save mood to history file"""
    mood_data = load_mood_history()
    today = datetime.now().strftime("%Y-%m-%d")
    mood_data[today] = mood
    with open(MOOD_FILE, 'w') as f:
        json.dump(mood_data, f, indent=2)
def load_mood_history():
    """Load mood history from file"""
    if os.path.exists(MOOD_FILE):
        with open(MOOD_FILE, 'r') as f:
            return json.load(f)
    return {}
def show_mood_history():
    """Display mood history"""
    mood_data = load_mood_history() 
    if not mood_data:
        print("No mood history yet. Start tracking today!\n")
        return
    print("\n📊 Your Mood History:\n")
    mood_emoji = {1: "😔", 2: "😐", 3: "🙂", 4: "😊", 5: "🤩"}
    for date, mood in sorted(mood_data.items(), reverse=True)[:7]:
        print(f"   {date}: {mood_emoji.get(mood, '❓')} ({mood}/5)")
    if len(mood_data) > 0:
        avg_mood = sum(mood_data.values()) / len(mood_data)
        print(f"\n   Average mood: {avg_mood:.1f}/5")
    print()
def main():
    """Main application loop"""
    display_banner()
    while True:
        print("\nWhat would you like to do?")
        print("1. Get motivated! (Random quote)")
        print("2. Track my mood")
        print("3. View mood history")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            print()
            display_quote()
        elif choice == "2":
            print()
            track_mood()
        elif choice == "3":
            show_mood_history()
        elif choice == "4":
            print("\n🌟 Keep shining! See you tomorrow! 🌟\n")
            break
        else:
            print("\nPlease enter a valid option (1-4).")
if __name__ == "__main__":
    main()