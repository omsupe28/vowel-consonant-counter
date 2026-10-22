"""Python mini project: Vowel & Consonant Counter (Sets & Strings).

Students: Parag Yewale (12) and Om Supe (11).
"""

VOWELS = set("aeiou")
LETTERS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


def count_letters(text):
    """Count English letters; ignore all other characters.

    Repeated letters count separately. Unique letters are also returned.
    The letter y is treated as a consonant.
    """
    vowels = 0
    consonants = 0
    unique_vowels = set()
    unique_consonants = set()

    for character in text:
        if character not in LETTERS:
            continue
        letter = character.lower()
        if letter in VOWELS:
            vowels += 1
            unique_vowels.add(letter)
        else:
            consonants += 1
            unique_consonants.add(letter)

    return {
        "vowels": vowels,
        "consonants": consonants,
        "ignored": len(text) - vowels - consonants,
        "unique_vowels": unique_vowels,
        "unique_consonants": unique_consonants,
    }


def display_result(text, result):
    """Display counts and alphabetically sorted unique letters."""
    print("\n--- ANALYSIS RESULT ---")
    print("Input text        :", text)
    print("Vowels            :", result["vowels"])
    print("Consonants        :", result["consonants"])
    print("Total letters     :", result["vowels"] + result["consonants"])
    print("Ignored characters:", result["ignored"])
    for label, key in [("Unique vowels     :", "unique_vowels"),
                       ("Unique consonants :", "unique_consonants")]:
        letters = ", ".join(sorted(result[key])) or "None"
        print(label, letters)


def main():
    """Run the menu until the user selects Exit."""
    while True:
        print("\n===== VOWEL & CONSONANT COUNTER =====")
        print("1. Analyze text")
        print("2. Exit")
        try:
            choice = input("Enter your choice (1-2): ").strip()
            if choice == "1":
                text = input("Enter a word or sentence: ")
                if not text.strip():
                    print("Please enter at least one non-space character.")
                    continue
                display_result(text, count_letters(text))
            elif choice == "2":
                print("Thank you for using the counter!")
                break
            else:
                print("Invalid choice! Please enter 1 or 2.")
        except (EOFError, KeyboardInterrupt):
            print("\nCounter closed.")
            break


if __name__ == "__main__":
    main()
