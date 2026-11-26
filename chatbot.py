
replies = {
    "hello": "Hello! Welcome.",
    "hi": "Hi! How are you?",
    "python": "Python is a programming language.",
    "help": "I can answer simple questions.",
    "bye": "Goodbye!"
}
conversation = []
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_message = input("You: ").strip().lower()
    if user_message == "":
        continue
    conversation.append({
        "role": "user",
        "content": user_message
    })
    if user_message == "bye":
        bot_reply = replies.get("bye")
        print("Chatbot:", bot_reply)

        conversation.append({
            "role": "assistant",
            "content": bot_reply
        })
        break
    words = user_message.split()
    bot_reply = "Sorry, I don't understand."
    for keyword, reply in replies.items():
        if keyword in words:
            bot_reply = reply
            break
    print("Chatbot:", bot_reply)
    conversation.append({
        "role": "assistant",
        "content": bot_reply
    })
print("\nConversation History:")
for message in conversation:
    print(message["role"], ":", message["content"])
