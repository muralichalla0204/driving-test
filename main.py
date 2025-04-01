def driving_test():
    print("🚗 Welcome to the Driving Test!")
    
    score = 0  # Initialize score
    
    # List of questions and correct answers
    questions = [
        ("Is it okay to use a phone while driving?", "no"),
        ("Should you stop at a red light?", "yes"),
        ("Can you drive without wearing a seatbelt?", "no"),
        ("Is it legal to drive above the speed limit?", "no"),
        ("Do you need to signal before turning?", "yes")
    ]
    
    # Loop through the questions
    for question, correct_answer in questions:
        answer = input(f"{question} (Yes/No): ").strip().lower()
        
        # Check if the user entered 'yes' or 'no' and compare
        if answer == correct_answer:
            score += 1
        elif answer != "yes" and answer != "no":
            print("⚠️ Invalid input! Please answer with 'Yes' or 'No'.")
    
    # Result
    if score >= 3:  # Change condition for passing to a score of 3 or more
        print(f"Your score is {score}/5. 🎉 You passed the test!")
    else:
        print(f"Your score is {score}/5. ❌ You failed the test.")

if __name__ == "__main__":
    driving_test()
