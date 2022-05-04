import re
import random
import requests
from bs4 import BeautifulSoup
from player import Player


def get_title():
    """ Returns a multiline string that acts as a title screen. """
    return """
    ==========================================================+
     _    _          _   _  _____ __  __          _   _ _     |
    | |  | |   /\\   | \\ | |/ ____|  \\/  |   /\\   | \\ | | |    O
    | |__| |  /  \\  |  \\| | |  __| \\  / |  /  \\  |  \\| | |   /|\\
    |  __  | / /\\ \\ |     | | |_ | |\\/| | / /\\ \\ |     | |   / \\
    | |  | |/ ____ \\| |\\  | |__| | |  | |/ ____ \\| |\\  |_|
    |_|  |_/_/    \\_\\_| \\_|\\_____|_|  |_/_/    \\_\\_| \\_(_)
    =============================================================
    """


def get_gallows(incorrect_guess_count):
    """ Returns a multiline string that acts as a visual for the gallows. 'gallows' is a dictionary acting as a switch
    statement to satisfy project requirements (it looks cleaner as a tuple). No validation here since the only argument
    passed in is the length of a list. """

    gallows = {
        0:
            """
        +---+
        |
        |
        |
        |
        |
        =======\n""",
        1:
            """
        +---+
        |   |
        |
        |
        |
        |
        =======\n""",
        2:
            """
        +---+
        |   |
        |   O
        |
        |
        |
        =======\n""",
        3:
            """
        +---+
        |   |
        |   O
        |   |
        |
        |
        =======\n""",
        4:
            """
        +---+
        |   |
        |   O
        |  /|
        |
        |
        =======\n""",
        5:
            """
        +---+
        |   |
        |   O
        |  /|\\
        |
        |
        =======\n""",
        6:
            """
        +---+
        |   |
        |   O
        |  /|\\
        |  /
        |
        =======\n""",
        7:
            """
        +---+
        |   |
        |   O
        |  /|\\
        |  / \\
        |
        =======\n"""
    }
    return gallows.get(incorrect_guess_count, "Key not found in get_gallows().")


def display_game_board(word, hint, correct_letters, incorrect_letters):
    """ Displays the gallows, underscores & correct guesses, incorrect guesses, and hint. """

    # Displays the gallows.
    print(get_gallows(len(incorrect_letters)))

    # Creates underscore placeholders for the letters being guessed.
    underscores = []
    for i in word:
        underscores.append("_")

    # Displays the underscores, correct guesses, and hint.
    for i in range(len(underscores)):
        if word[i] in correct_letters:
            underscores[i] = word[i]
    for i in range(len(underscores)):
        print(underscores[i] + " ", end="")
    print("\nHint " + hint)

    # Displays the incorrect guesses.
    print("Incorrect guesses: ", end="")
    for letter in incorrect_letters:
        print(letter + " ", end="")
    print()


def scrape_words():
    """ Scrapes current and archived words from Merriam-Webster's 'Word of the Day' page and returns them as a list. """
    # TODO: Call this outside of play_game() so it only runs once per session. No need to grab 300+ words every round.

    # Scrapes the URL and creates a BeautifulSoup object.
    source_url = "https://www.merriam-webster.com/word-of-the-day/calendar"
    try:
        page = requests.get(source_url)
    except requests.RequestException as e:
        print("Requesting words from Merriam-Webster.com failed.")
        exit()
    if page.status_code != 200:
        print(f"Requesting words from Merriam-Webster.com failed. HTTP status code: {page.status_code}")
        exit()
    soup = BeautifulSoup(page.content, "html.parser")

    # Locates the words of the day and adds them to a list.
    results_list = []
    ul_list = soup.find_all("ul", "more-wod-items")
    for ul in ul_list:
        li_anchors = ul.find_all("a")
        for anchor in li_anchors:
            if "î" in anchor.text:
                # TODO: Find a better way to accommodate special characters (e.g. MAÎTRE D')
                results_list.append(anchor.text.replace("î", "i").upper())
                continue
            results_list.append(anchor.text.upper())
    # print(results_list)  # For testing only
    return results_list


def scrape_hint(word):
    """ Scrapes and returns definitions from Merriam-Webster to use as hints """

    source_url = f"https://www.merriam-webster.com/dictionary/{word}"
    try:
        page = requests.get(source_url)
    except requests.RequestException as e:
        print("Requesting a hint/definition from Merriam-Webster.com failed.")
        exit()
    if page.status_code != 200:
        print(f"Requesting hint/definition from Merriam-Webster.com failed. HTTP status code: {page.status_code}")
        exit()
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("span", "dtText")
    return results.text


def get_guess(existing_guesses):
    """ Prompts the user for input then validates and returns it. """

    valid_guess_length = 1
    while True:
        guess = input("Enter guess: ").upper()
        if len(guess) != valid_guess_length or re.search("[^A-Z- ']", guess):
            print("Invalid input. Please enter one character.")
        elif guess in existing_guesses:
            print(f"{guess} has already been guessed!")
        else:
            return guess


def celebrate():
    """ Provides the user with a Certificate of Excellence """

    # Determines if user would like to receive a certificate.
    celebrate_decision = input("Would you like a certificate to memorialize this very special occasion (Y/N): ").upper()
    if celebrate_decision != "Y" and celebrate != "YES":
        return

    # Gathers input for the certificate and creates a Player object.
    name = input("Enter your name: ")
    player = Player(name)

    # Writes a certificate file using the Player object.
    with open("Certificate of Excellence.txt", "a") as file:
        file.write(f"\n{str(player.name)} was excellent on {str(player.date)}.")


def play_game():
    """ The primary function. This calls the other functions to set up variables and determines whether the user has
    won or lost. """

    # Sets up variables for a new game.
    word_list = scrape_words()
    random_index = random.randint(0, len(word_list))
    word = word_list[random_index]
    hint = scrape_hint(word)
    correct_letters = []
    incorrect_letters = []

    # print(f"The word is {word}")  # For testing only.

    # Starts the main loop.
    while True:
        # Displays the board and gets user input.
        display_game_board(word, hint, correct_letters, incorrect_letters)
        guessed_letter = get_guess(correct_letters + incorrect_letters)

        # Adds correct input to the correct_letters list.
        if guessed_letter in word:
            correct_letters.append(guessed_letter)

            # Checks to see if the word has been correctly guessed.
            word_completed = True
            for letter in word:
                if letter not in correct_letters:
                    word_completed = False
                    break
            if word_completed:
                print("You win!")
                celebrate()
                break

        # Adds incorrect input to the incorrect_letters list.
        else:
            incorrect_letters.append(guessed_letter)

            # Checks to see if the user is out of guesses.
            max_attempts = 7
            if len(incorrect_letters) == max_attempts:
                display_game_board(word, hint, correct_letters, incorrect_letters)
                print(f"GAME OVER\nThe word was {word}")
                break
