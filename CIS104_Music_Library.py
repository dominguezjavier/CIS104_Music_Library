import json
# I am listing the functions to where the songs are located on.
Song = {
    "Title": None,
    "Artist": None,
    "Album": None,
    "Track": None,
    "Year": None,
    "Genre": None}
# I followed the set up from the calculator project
def add_song():
    Song["Title"] = input("enter song tile: ")
    Song["Artist"] = input("enter artist name ")
    Song["Album"] = input("enter album title ")
    Song["Track"] = input("enter track number ")
    Song["Year"] = input("enter the Year")
    Song["Genre"] = input("enter the Genre ")

def save_song():
    if Song["Title"] != None:
        writefile = open("MusicDB.txt", "a")
        writefile.write(json.dumps(Song))
    elif Song["Title"] == None:
        print("Please, you must add a song! ")
# I had to watch you tube videos and ask others for help on this part. I understand the while loop.
# I have to ask lindsey to recommend a chapter to read on this.
def clear_file():
    file = open("MusicDB.TXT", "w")
    file.truncate(0)
# Look up videos on dictionaries and ask Lindsey for information on dictionaries.
def list_song():
    count = 0
    f = open("MusicDB.txt", "r")
    for entry in f:
        clean = []
        clean_entry = entry.replace('"', '').strip("{").strip("}").strip(",").split("}{")
    for s in clean_entry:
        count = count + 1 
        print("Song #",count,":",s,"\n")

def call_menu():
    print("add : Add a new song to the music database\n"
     "list : List the songs in the music database\n"
     "save : Save the music datatbase\n"
     "help : Display this menu\n"
     "exit : Exit the Program\n")
clear_file()
call_menu()
big_count = 0

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

