import tkinter as tk
from tkinter import scrolledtext
import string

# Predefined responses (Rule-Based)
responses = {
    "hello": "Hi! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a great day.",
    "what is your name": "I am a simple chatbot.",
    "thank you": "You're welcome!"
}

# Chatbot Function
def chatbot_response(user_input):
    processed_input = user_input.lower().translate(str.maketrans('', '', string.punctuation))
    for key in responses:
        if key in processed_input:
            return responses[key]
    return "I'm sorry, I don't understand that."

# Function to send message
def send_message(event=None):
    user_text = entry.get()
    if not user_text.strip():
        return

    if user_text.lower() == "exit":
        root.quit()

    response = chatbot_response(user_text)

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_text + "\n", "user")
    chat_window.insert(tk.END, "Bot: " + response + "\n\n", "bot")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)  # Auto-scroll to the bottom
    entry.delete(0, tk.END)

# Function to clear chat
def clear_chat():
    chat_window.config(state=tk.NORMAL)
    chat_window.delete(1.0, tk.END)
    chat_window.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("Advanced Chatbot")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# Chat Window (Scrollable)
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=55, height=20, font=("Arial", 12))
chat_window.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
chat_window.tag_config("user", foreground="blue", font=("Arial", 12, "bold"))
chat_window.tag_config("bot", foreground="green", font=("Arial", 12))
chat_window.config(state=tk.DISABLED)  # Make it read-only

# Entry Field
entry = tk.Entry(root, width=40, font=("Arial", 14), bd=2, relief=tk.GROOVE)
entry.grid(row=1, column=0, padx=10, pady=10, ipady=5)
entry.bind("<Return>", send_message)  # Enter Key Support

# Send Button
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12), bg="#4CAF50", fg="white", relief=tk.RAISED, width=10)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Clear Chat Button
clear_button = tk.Button(root, text="Clear", command=clear_chat, font=("Arial", 12), bg="#FF5733", fg="white", relief=tk.RAISED, width=10)
clear_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()

