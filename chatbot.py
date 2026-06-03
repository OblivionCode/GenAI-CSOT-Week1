from call_model import call_model

# Main chatbot class
class ChatAgent:


    # Constructor initializes model and memory
    def __init__(self, model, max_turns=5):

        self.model = model
        self.max_turns = max_turns

        # Stores chat history
        self.messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]


    # Adds messages to conversation history
    def add_message(self, role, content):

        self.messages.append({
            "role": role,
            "content": content
        })


    # Keeps only recent conversation turns
    def compact_history(self):

        # Preserve system prompt
        system_message = self.messages[0]

        # Keep only latest turns
        recent_messages = self.messages[-(self.max_turns * 2):]

        self.messages = [system_message] + recent_messages


    # Main conversation loop
    def chat(self):

        print("\nType 'exit' to quit.")
        print("Type '/compact' to compact memory.\n")

        while True:

            user_input = input("You: ")

            # Exit command
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            # Manual memory compaction
            if user_input.lower() == "/compact":
                self.compact_history()
                print("Memory compacted.")
                continue

            # Store user message
            self.add_message("user", user_input)

            # Generate assistant response
            response = call_model(
                self.messages,
                self.model
            )

            print("\nAssistant:", response, "\n")

            # Store assistant response
            self.add_message("assistant", response)

            # Auto compact if memory exceeds limit
            if len(self.messages) > (self.max_turns * 2 + 1):
                self.compact_history()

#Model Selection
MODELS = {
    "1": "openai/gpt-4o-mini",
    "2": "deepseek/deepseek-chat",
    "3": "meta-llama/llama-3.1-8b-instruct"
}

print("Choose a model:\n")

for key, value in MODELS.items():
    print(f"{key}. {value}")

choice = input("\nEnter choice: ")

selected_model = MODELS.get(choice)

if not selected_model:
    print("Invalid choice.")
    exit()

# Create chatbot object
agent = ChatAgent(selected_model)

# Start chatbot
agent.chat()