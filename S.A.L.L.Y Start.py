import requests


def ask_question(question):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": f"I am feeling {question}.",
        "max_tokens": 50
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    return response.json()["choices"][0]["text"].strip()

def get_user_answers():
    questions = [
        "Feeling nervous, anxious, or on edge?",
        "Not being able to stop or control worrying?",
        "Worrying too much about different things?",
        "Trouble relaxing?",
        "Being so restless that it's hard to sit still?",
        "Becoming easily annoyed or irritable?",
        "Feeling afraid as if something awful might happen?"
    ]
    answers = {}

    for question in questions:
        answer = input(question + " (yes/no): ").lower()
        while answer not in ['yes', 'no']:
            print("Please enter 'yes' or 'no'.")
            answer = input(question + " (yes/no): ").lower()
        answers[question] = answer

    return answers

def calculate_anxiety_level(answers):
    total_yes = sum(1 for answer in answers.values() if answer == 'yes')
    return total_yes

def generate_weekly_plan(anxiety_level):
    if anxiety_level <= 2:
        return [
            "Practice deep breathing exercises for 10 minutes daily.",
            "Engage in physical activity for at least 30 minutes every day.",
            "Write down three things you're grateful for each day.",
            "Limit caffeine intake.",
            "Ensure you get 7-9 hours of sleep each night.",
            "Reach out to a friend or loved one for support.",
            "Take a shower and practice self-care daily.",
            "Eat a balanced meal with plenty of fruits and vegetables daily.",
            "Listen to your favorite calming music or an uplifting song.",
            "Spend some time outdoors, even if it's just for a short walk daily."
        ]
    elif anxiety_level <= 4:
        return [
            "Practice deep breathing exercises for 15 minutes daily.",
            "Engage in physical activity for at least 45 minutes every day.",
            "Write down three things you're grateful for each day.",
            "Limit caffeine intake.",
            "Ensure you get 7-9 hours of sleep each night.",
            "Reach out to a friend or loved one for support.",
            "Take a shower and practice self-care daily.",
            "Eat a balanced meal with plenty of fruits and vegetables daily.",
            "Listen to your favorite calming music or an uplifting song.",
            "Spend some time outdoors, even if it's just for a short walk daily."
        ]
    else:
        return [
            "Practice deep breathing exercises for 20 minutes daily.",
            "Engage in physical activity for at least 60 minutes every day.",
            "Write down three things you're grateful for each day.",
            "Limit caffeine intake.",
            "Ensure you get 7-9 hours of sleep each night.",
            "Reach out to a friend or loved one for support.",
            "Take a shower and practice self-care daily.",
            "Eat a balanced meal with plenty of fruits and vegetables daily.",
            "Listen to your favorite calming music or an uplifting song.",
            "Spend some time outdoors, even if it's just for a short walk daily."
        ]

def main():
    print("Welcome to the Mental Health Improvement Bot!")

    # Get user's mental health questionnaire answers
    print("\nPlease answer the following questions:")
    user_answers = get_user_answers()

    # Calculate user's anxiety level
    anxiety_level = calculate_anxiety_level(user_answers)
    print("\nYour anxiety level is:", anxiety_level)

    # Generate weekly improvement plan based on anxiety level
    improvement_plan = generate_weekly_plan(anxiety_level)

    # Print the improvement plan
    print("\nHere's your weekly improvement plan:")
    for task in improvement_plan:
        print("-", task)

    print("\nTake care of yourself and have a great week!")


if __name__ == "__main__":
    main()
import time
import random
from plyer import notification

# Define reminder messages
reminders = [
    "Don't forget to take a shower!",
    "Time for a meal. Don't skip it!",
    "Remember to drink water and stay hydrated!"
]

# Function to display reminder notification
def remind(message):
    notification.notify(
        title="Self-Care Reminder",
        message=message,
        app_icon=None,  # You can specify an icon file if desired
        timeout=10  # Adjust the duration of the notification
    )

# Main loop for reminders
def main():
    while True:
        # Choose a random reminder message
        random_message = random.choice(reminders)
        remind(random_message)
        time.sleep(3600)  # Remind every hour (3600 seconds)

if __name__ == "__main__":
    main()
