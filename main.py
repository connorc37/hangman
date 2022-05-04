"""
Name: Corey Connor
Class: CIS189 Python
Module: 16
Topic: Final Project
Assignment: Final Project

You must include the following functionality in your project:
[X] Multiple functions (or methods)
[X] Unit testing
[X] Exception Handling (Try/Except)
[X] Some sort of user input, including input validation
[X] Some sort of output
[X] A class

You must include nine of the following in your project:
[X] Decision Structure: If, if-else, if-elif
[X] Looping Structure: For/while loop
[X] File I/O
[ ] Inner function
[ ] Function with arbitrary arguments: *args/**kwargs
[X] Collection: List/tuple
[X] Collection: Set/dictionary
[ ] Collection: Array
[X] Case-switch statement
[X] Datetime
[X] Python Module or Package
[X] Data Scraper
[X] Object-Oriented Functionality including constructors/methods/objects
[ ] Object-Oriented Program inheritance/polymorphism including base-derived class
[ ] Database connectivity
[ ] A GUI component
"""

from game import get_title, play_game

print(get_title())
while True:
    play_game()
    keep_playing = input("Play again (Y/N): ").upper()
    if keep_playing != "Y" and keep_playing != "YES":
        break
