import csv
import random

def load_questions_from_csv(filename):
    """Function to load questions and answers from a CSV file."""
    questions = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append({"question": row['Question'], "answer": row['Answer']})
    return questions

def assign_questions(grade):
    """Assign questions based on the student's grade and difficulty level."""
    
    # Load all questions from each category
    easy_questions = load_questions_from_csv('easy.csv')
    medium_questions = load_questions_from_csv('medium.csv')
    hard_questions = load_questions_from_csv('hard.csv')
    
    if 7.5 <= grade < 8:
        # 4 easy, 4 medium, 2 hard questions
        selected_easy = random.sample(easy_questions, 4)
        selected_medium = random.sample(medium_questions, 4)
        selected_hard = random.sample(hard_questions, 2)
    elif 8 <= grade < 9:
        # 3 easy, 4 medium, 3 hard questions
        selected_easy = random.sample(easy_questions, 3)
        selected_medium = random.sample(medium_questions, 4)
        selected_hard = random.sample(hard_questions, 3)
    elif 9 <= grade <= 10:
        # 4 hard, 4 medium, 2 easy questions
        selected_easy = random.sample(easy_questions, 2)
        selected_medium = random.sample(medium_questions, 4)
        selected_hard = random.sample(hard_questions, 4)
    else:
        return "Invalid grade! Please provide a grade between 7.5 and 10."
    
    # Combine all selected questions
    assigned_questions = selected_easy + selected_medium + selected_hard
    random.shuffle(assigned_questions)  # Shuffle to mix the difficulty levels
    
    return assigned_questions

# Main function to take grade input and assign questions
def main():
    grade = float(input("Enter the student's grade (7.5 - 10): "))

    questions = assign_questions(grade)
    if isinstance(questions, list):
        print("\nAssigned Questions:")
        for i, qa in enumerate(questions, start=1):
            print(f"{i}. Question: {qa['question']}")
            print('Answer:')
            x = input().lower()  # Get user answer
            if x == qa['answer'].lower():  # Compare answers (case insensitive)
                print("Correct answer!")
            else:
                print(f"Wrong answer. The correct answer is: {qa['answer']}\n")
    else:
        print(questions)

# Run the main function
if __name__ == "__main__":
    main()
