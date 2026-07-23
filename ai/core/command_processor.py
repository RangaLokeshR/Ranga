class CommandProcessor:
    """
    Handles user commands.
    """

    def process(self, command):

        command = command.lower()

        if command == "hello":
            return "Hello! Nice to meet you."

        elif command == "who are you":
            return "I am Ranga, your personal AI companion."

        elif command == "bye":
            return "Goodbye! Have a great day."

        else:
            return "Sorry, I don't understand that command yet."