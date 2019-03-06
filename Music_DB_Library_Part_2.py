import json
import MusicDB

# Copied and pasted from my Music Library

while ():
    command = input("Please enter one of the listed commands: ")
    if command == "add":
        add_song()
        big_count = big_count + 1
    elif command == "save" and big_count <=8:
        save_song()
    elif command == "save" and big_count > 8:
        print("your file is full")
    elif command == "list":
        list_song()
    elif command == "help":
        call_menu()
    elif command == "exit":
        break
    else:
        print("You have done an error, that is not a valid command")
        continue



 