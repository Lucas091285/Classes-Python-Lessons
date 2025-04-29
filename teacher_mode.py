import json

flashcard = {"What is the capital of France?": "Paris"}


with open("FlashCards.json", "w") as file:
    json.dump(flashcard, file, indent=4)


with open("FlashCards.json", "r") as file:
    flashcards = json.load(file)

score = 0
streak = 0

for question, answer in flashcards.items():
    user_input = input(f"{question} ").strip()

    if user_input.lower() == answer.lower():
        score += 1
        streak += 1
        print(f" Correct, Score: {score}, Streak: {streak}\n")
    else:
        streak = 0
        print(f" Wrong, The correct answer was: {answer}")
        print(f"Score: {score}, Streak: {streak}\n")

for question, answer in flashcards.items():
    user_input = input(f"{question} ").strip()

    if user_input.lower() == answer.lower():
        score += 1
        streak += 1
        print(f" Correct, Score: {score}, Streak: {streak}\n")
    else:
        streak = 0
        print(f" Wrong, The correct answer was: {answer}")
        print(f"Score: {score}, Streak: {streak}\n")

print(f"Final Score: {score} | Final Streak: {streak}")

dhchhd