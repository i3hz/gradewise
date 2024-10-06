from flask import Flask, render_template, request
import csv
import random

app = Flask(__name__)

def load_questions_from_csv(filename):
    """Function to load questions and answers from a CSV file."""
    questions = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append({"question": row['Question'], "answer": row['Answer']})
    return questions

def assign_questions(grade,subject):
    """Assign questions based on the student's grade and difficulty level."""
    
    # Load all questions from each category
    easy_questions = load_questions_from_csv(subject+'/easy.csv')
    medium_questions = load_questions_from_csv(subject+'/medium.csv')
    hard_questions = load_questions_from_csv(subject+'/hard.csv')
    
    if 7.5 <= grade < 8:
        selected_easy = random.sample(easy_questions, 4)
        selected_medium = random.sample(medium_questions, 4)
        selected_hard = random.sample(hard_questions, 2)
    elif 8 <= grade < 9:
        selected_easy = random.sample(easy_questions, 3)
        selected_medium = random.sample(medium_questions, 4)
        selected_hard = random.sample(hard_questions, 3)
    elif 9 <= grade <= 10:
        selected_easy = random.sample(easy_questions, 2)
        selected_medium = random.sample(medium_questions, 4)
        selected_hard = random.sample(hard_questions, 4)
    else:
        return "Invalid grade! Please provide a grade between 7.5 and 10."
    
    # Combine all selected questions
    assigned_questions = selected_easy + selected_medium + selected_hard
    random.shuffle(assigned_questions)
    
    return assigned_questions  # Ensure the list is returned

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz', methods=['POST'])
def quiz():
    grade = float(request.form['grade'])
    subject = request.form['subject']
    subject= subject.lower()
    
    questions = assign_questions(grade,subject)

    if isinstance(questions, list):
        enumerated_questions = list(enumerate(questions, start=1))
        return render_template('quiz.html', questions=enumerated_questions)
    else:
        return questions

if __name__ == '__main__':
    app.run(debug=True)
