from ai.engine.engine_factory import EngineFactory

class Assistant:

    def __init__(self):
        self.engine = EngineFactory.create()

    def introduce(self):
        print("Hello!")
        print("I am Ranga.")
        print("Status : ONLINE")
        print()
        print("Waiting for your command...")
    def test_engine(self):
        print("Current Engine :", self.engine.model_name())
        print("Available :", self.engine.is_available())
        print("Response :", self.engine.ask("Hello"))

    def chat(self):

        while True:

            command = input("\nYou > ").strip()

            if command.lower() == "exit":
                print("\nRanga > Shutting down...")
                break

            response = self.engine.ask(command)

            print("\nRanga >", response)