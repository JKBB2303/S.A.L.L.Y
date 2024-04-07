import time

def get_user_input(prompt, valid_responses):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() in valid_responses:
            return user_input.lower()
        else:
            print("Invalid input. Please try again.")

def get_daily_plan(risk_level):
    plans = {
        "Minimal": [
            "Engage in regular physical activity such as walking, jogging, or yoga for at least 30 minutes.",
            "Connect with a friend or family member for social support.",
            "Practice relaxation techniques such as deep breathing or meditation.",
            "Engage in activities you enjoy, such as hobbies or leisure activities.",
            "Get plenty of rest and maintain a regular sleep schedule."
        ],
        "Mild": [
            "Consider therapy sessions with a mental health professional.",
            "Maintain a healthy diet with plenty of fruits, vegetables, and whole grains.",
            "Limit alcohol consumption and avoid recreational drugs.",
            "Engage in regular exercise to boost mood and energy levels.",
            "Practice self-compassion and challenge negative thoughts."
        ],
        "Moderate": [
            "Seek therapy or counseling sessions to address underlying issues.",
            "Consider medication under the guidance of a psychiatrist.",
            "Create a daily routine to provide structure and stability.",
            "Engage in social activities to combat isolation and loneliness.",
            "Practice stress management techniques such as mindfulness or progressive muscle relaxation."
        ],
        "Severe": [
            "Seek immediate help from a mental health professional or a crisis helpline.",
            "Consider hospitalization or intensive outpatient treatment.",
            "Develop a safety plan to manage suicidal thoughts or urges.",
            "Involve trusted friends or family members in your support network.",
            "Follow treatment recommendations and attend therapy sessions regularly."
        ]
    }
    return plans.get(risk_level, [])

def remind_user(task):
    print(f"Reminder: Don't forget to {task.lower()}!")

def depression_screening():
    print("Welcome to the Depression Screening Questionnaire.")
    name = input("What is your name? ")
    print(f"Hello, {name}! Please answer the following questions with a number from 0 to 3, where:")
    print("0 - Not at all")
    print("1 - Several days")
    print("2 - More than half the days")
    print("3 - Nearly every day")
    print()

    questions = [
        "Little interest or pleasure in doing things?",
        "Feeling down, depressed, or hopeless?",
        "Trouble falling or staying asleep, or sleeping too much?",
        "Feeling tired or having little energy?",
        "Poor appetite or overeating?",
        "Feeling bad about yourself — or that you are a failure or have let yourself or your family down?",
        "Trouble concentrating on things, such as reading the newspaper or watching television?",
        "Moving or speaking so slowly that other people could have noticed?",
        "Thoughts that you would be better off dead or of hurting yourself in some way?"
    ]

    total_score = 0
    for i, question in enumerate(questions):
        while True:
            response = input(f"{i + 1}. {question} ").strip()
            if response.isdigit() and 0 <= int(response) <= 3:
                total_score += int(response)
                break
            else:
                print("Invalid response. Please enter a number from 0 to 3.")

    print("\nThank you for completing the questionnaire, " + name + ".")
    print("Your total score is:", total_score)

    risk_levels = [
        ("Minimal", "You are experiencing minimal depression symptoms. It's important to seek support if you are struggling. Consider talking to someone you trust or a mental health professional."),
        ("Mild", "You are experiencing mild depression symptoms. You may benefit from self-help strategies or talking to a mental health professional."),
        ("Moderate", "You are experiencing moderate depression symptoms. It is recommended to seek support from a mental health professional."),
        ("Severe", "You are experiencing severe depression symptoms. It's important to seek immediate support from a mental health professional or a crisis helpline.")
    ]

    for level, message in risk_levels:
        if total_score < 5:
            print("Based on your score, you are in the " + risk_levels[0][0] + " risk level.")
            print(message)
            break
        elif total_score < 10:
            print("Based on your score, you are in the " + risk_levels[1][0] + " risk level.")
            print(message)
            break
        elif total_score < 15:
            print("Based on your score, you are in the " + risk_levels[2][0] + " risk level.")
            print(message)
            break
        else:
            print("Based on your score, you are in the " + risk_levels[3][0] + " risk level.")
            print(message)
            break

    print("\nHere are some mental health resources that you can consider:")
    print("- National Suicide Prevention Lifeline: 1-800-273-TALK (8255)")
    print("- Crisis Text Line: Text HOME to 741741")
    print("- National Alliance on Mental Illness (NAMI): 1-800-950-NAMI (6264)")
    print("- SAMHSA National Helpline: 1-800-662-HELP (4357)")
    print("- Talk to your healthcare provider or a mental health professional for more support.")

    risk_level = next((level for level, _ in risk_levels if total_score < 5), risk_levels[-1][0])
    daily_plan = get_daily_plan(risk_level)
    print("\nHere is a daily plan tailored to your risk level:")
    for i, plan in enumerate(daily_plan, start=1):
        print(f"{i}. {plan}")
    set_reminders(daily_plan)

def set_reminders(daily_plan):
    print("\nSetting up your daily reminders...")
    for plan in daily_plan:
        task_time = input(f"At what time would you like to be reminded to {plan.lower()}? (e.g., 08:30 AM): ")
        while True:
            try:
                # Convert user input time to seconds since epoch
                reminder_time = time.mktime(time.strptime(task_time, "%I:%M %p"))
                current_time = time.time()
                if reminder_time < current_time:
                    print("Please enter a future time.")
                    task_time = input(f"At what time would you like to be reminded to {plan.lower()}? (e.g., 08:30 AM): ")
                else:
                    break
            except ValueError:
                print("Invalid time format. Please enter time in the format HH:MM AM/PM (e.g., 08:30 AM).")
                task_time = input(f"At what time would you like to be reminded to {plan.lower()}? (e.g., 08:30 AM): ")

        # Calculate delay until the reminder time
        delay = reminder_time - current_time

        # Sleep until the reminder time
        time.sleep(delay)

        # Display reminder
        remind_user(plan)

    print("Reminders set successfully!")

if __name__ == "__main__":
    depression_screening()




