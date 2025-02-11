class Memory:
    def __init__(self):
        self.history = []

    def add_message(self, user_input, ai_response):
        self.history.append({"user": user_input, "ai": ai_response})

    def get_history(self):
        return "\n".join([f"User: {msg['user']}\nAI: {msg['ai']}" for msg in self.history])

memory = Memory()
