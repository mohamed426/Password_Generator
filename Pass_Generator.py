from itertools import permutations, product
import pyfiglet
import os
import string

try:
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display a welcome message using pyfiglet
    welcome_message = pyfiglet.figlet_format("Password Generator")
    author = "- Made by: MO KHALED\n"
    description = "- This script generates a list of potential passwords based on user input."
    respect_notice = "- Respect the privacy of others and use this script responsibly."
    print(welcome_message)
    print(description)
    print(respect_notice)
    print(author)

    print("'To exit, press Ctrl+C'")
    # Ask the user to enter all known information
    user_input = input("Enter all known information (names, dates, numbers, symbols) separated by spaces:\n")

    # Convert input string into a list
    base_items = user_input.strip().split()

    # Generate combinations
    # Single item + another item (excluding identical pairs)
    single_combos = [w + n for w, n in product(base_items, base_items) if w != n]

    # Two-item combinations (order matters)
    two_word_combos = [''.join(p) for p in permutations(base_items, 2)]

    # Two-item + another item combinations
    two_word_with_number = [w + n for w, n in product(two_word_combos, base_items)]

    # Combine all and remove duplicates
    all_passwords = list(set(base_items + single_combos + two_word_combos + two_word_with_number))

    # Add reversed versions
    reversed_passwords = [p[::-1] for p in all_passwords]
    all_passwords = list(set(all_passwords + reversed_passwords))

    # Filter out passwords that contain only symbols
    symbols = set(string.punctuation)
    def is_only_symbols(password):
        return all(char in symbols for char in password)

    filtered_passwords = [p for p in all_passwords if not is_only_symbols(p)]

    # Save to file
    with open("passwords.txt", "w") as f:
        for password in filtered_passwords:
            f.write(password + "\n")

    print(f"{len(filtered_passwords)} passwords generated and saved to 'passwords.txt'")
except KeyboardInterrupt:
    print("\nExiting the script. Goodbye!")
except Exception as e:
    print(f"An error occurred: {e}")
