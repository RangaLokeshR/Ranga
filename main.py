from ai.core.assistant import Assistant


def main():

    print("=" * 45)
    print("        RANGA AI COMPANION")
    print("=" * 45)

    print("\nInitializing...\n")

    ranga = Assistant()

    ranga.introduce()

    ranga.chat()


if __name__ == "__main__":
    main()