import time
import random
from plyer import notification

# Define reminder messages
reminders = {
    "shower": "Don't forget to take a shower!",
    "eat": "Time for a meal. Don't skip it!",
    "water": "Remember to drink water and stay hydrated!"
}

# Function to display reminder notification
def remind(message):
    notification.notify(
        title="Self-Care Reminder",
        message=message,
        app_icon=None,  # You can specify an icon file if desired
        timeout=20  # Adjust the duration of the notification
    )

# Main loop for reminders
def main():
    while True:
        # Choose a random reminder message
        random_task, random_message = random.choice(list(reminders.items()))
        remind(random_message)
        # Remind every hour (3600 seconds)
        time.sleep(3600)
        # Allow the user to exit the loop by pressing a key
        exit_choice = input("Press 'q' to quit reminders: ")
        if exit_choice.lower() == 'q':
            break

if __name__ == "__main__":
    main()

