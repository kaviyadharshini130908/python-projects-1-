
# python-projects-1-

Calculator and Greeting Bot

## Projects

### 1. Calculator
A simple Python calculator that performs addition, subtraction, multiplication, and division using if-else statements.

### 2. Greeting Bot
A Python program that asks the user's name and displays a welcome message using f-strings.

## Technologies Used
- Python
- Git
- GitHub
### Day 1 – Calculator and Greeting Bot
- Developed a simple calculator.
- Created a greeting bot.
- Practiced basic Python programming.

### Day 2 – Python Concepts and Implementation

#### Python Topics Practiced
1. Loops – for, range(), while, break, continue
2. Lists – indexing, slicing, append(), remove(), sort()
3. Dictionaries – key-value pairs, get(), items(), update()
4. Tuples and Sets
5. String Methods – lower(), strip(), split(), join(), replace(), in
6. Functions – parameters, default values, return
7. List of Dictionaries
8. List and Dictionary Comprehensions
9. Built-in Functions – len(), sum(), min(), max(), sorted(), enumerate(), zip()

#### Implementation
- Built a console chatbot that runs until the user types `bye`.
- Used a dictionary to match keywords with replies.
- Stored conversation history as a list of dictionaries.
- Created a student marks function to calculate average, highest, and lowest marks.

### Technologies Used
- Python
- Visual Studio Code
- Git and GitHub

## Day 3 - Python Advanced Basics

### Topics Practiced
1. Classes and Objects
2. Inheritance
3. Exception Handling
4. File Handling
5. JSON Files
6. CSV Files
7. Python Modules
8. pip and requirements.txt
9. Environment Variables
10. Type Hints

### Implementation Project
ChatBot with Chat History and Student CSV Summary

Features:
- Created a ChatBot class
- Added add_message() and get_reply() methods
- Saved chat history to chat_history.json
- Loaded previous chat history
- Handled missing chat history file
- Read student details from student.csv
- Printed student marks summary and average
- Stored bot name in .env file

### Technologies Used
- Python
- JSON
- CSV
- python-dotenv

### Run the Project
python chatbot_implementation.py

## Day 4: NumPy and Pandas

### Topics Covered
1. Jupyter Notebook and Google Colab basics
2. NumPy arrays: creation, shape, indexing, and slicing
3. Vectorised operations and broadcasting
4. NumPy statistics: mean, median, standard deviation, minimum, and maximum
5. Pandas Series and DataFrame
6. Reading CSV and Excel files
7. Data inspection using `head()`, `info()`, and `describe()`
8. Filtering, sorting, and adding columns
9. GroupBy and aggregation
10. Handling missing values using `isnull()`, `fillna()`, and `dropna()`

### Implementation: Student Performance Data Analysis

- Loaded a public student performance CSV dataset using Pandas.
- Cleaned missing values.
- Added derived columns: `Total_Marks`, `Average_Marks`, and `Result`.
- Answered five questions using filtering and `groupby()`.
- Saved the cleaned dataset as a CSV file.

### Files
- `student_performance (1).ipynb` – Implementation notebook
- `clean.csv` – Cleaned dataset

