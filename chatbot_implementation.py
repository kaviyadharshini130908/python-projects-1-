
import json
import csv
import os
from dotenv import load_dotenv
load_dotenv()
BOT_NAME = os.getenv("BOT_NAME", "ChatBot")
class ChatBot:
    def __init__(self):
        self.history = []
        self.load_history()
    def add_message(self, role, message):
        self.history.append({
            "role": role,
            "content": message
        })
    def get_reply(self, message):
        message = message.lower()
        if "hello" in message or "hi" in message:
            return "Hello! How can I help you?"
        elif "name" in message:
            return "My name is " + BOT_NAME
        elif "bye" in message:
            return "Goodbye!"
        else:
            return "Sorry, I don't understand."
    def save_history(self):
        with open("chat_history.json", "w") as file:
            json.dump(self.history, file, indent=4)
    def load_history(self):
        try:
            with open("chat_history.json", "r") as file:
                self.history = json.load(file)
        except FileNotFoundError:
            self.history = []
            print("No previous chat history found.")
bot = ChatBot()
print("Welcome to", BOT_NAME)
print("Type 'bye' to exit.")
while True:
    user_message = input("You: ")
    bot.add_message("user", user_message)
    reply = bot.get_reply(user_message)
    print(BOT_NAME + ":", reply)
    bot.add_message("bot", reply)
    bot.save_history()
    if user_message.lower() == "bye":
        break
print("\n--- Student Summary ---")
total_students = 0
total_marks = 0
with open("student.csv", "r") as file:
    reader = csv.DictReader(file)
    reader.fieldnames = [
        name.strip().lower()
        for name in reader.fieldnames
    ]
    for row in reader:
        row = {
            key.strip().lower(): value.strip()
            for key, value in row.items()
            if key is not None
        }
        total_students += 1
        total_marks += int(row["marks"])
        print(
            row["name"],
            "-",
            row["department"],
            "- Marks:",
            row["marks"]
        )
if total_students > 0:
    average = total_marks / total_students
    print("\nTotal Students:", total_students)
    print("Total Marks:", total_marks)
    print("Average Marks:", average)
else:
    print("No student records found.")
