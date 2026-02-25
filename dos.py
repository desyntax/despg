# "Solus OS" created 24/02/2026
print("Starting OS...")

# imports
import time
bootStart = time.time()
import random as rng
import math
print("Loaded imports.")

# variables
username = "desyntax"
password = "password"
welcomeMessage = "Solus OS indev_1, created by Desyntax on 24/02/2026."
command = ""
commandList = ["help", "logoff", "output", "cat", "username", "password", "osname"]
osname = "Solus"
arg1 = ""
arg2 = ""
arg3 = ""
helpList = """Solus OS command line. Copyright 2026. All rights reserved.
help                 -- Displays this help message.
logoff               -- Logs out of this computer.
output <str>         -- Prints <str> to the screen.
page <file>          -- Prints text from <file>.
pencil <file> [;a]   -- Writes text for <file>.
username <str>       -- Sets a new username.
password <str>       -- Sets a new password.
osname <str>         -- Sets a new OS name.

Use help <command> to view more details about a command."""
print("Loaded variables.")

# definitions
def login():
    print("Please sign in below.")
    while True:
        tryUsername = input("USERNAME> ")
        tryPassword = input("PASSWORD> ")
        if tryUsername == username and tryPassword == password:
            print(f"Logged in. Welcome, {username}")
            del tryUsername
            del tryPassword
            break
        else:
            print("Incorrect username or password. Try again, noob.")
print("Loaded definitions.")
bootEnd = time.time()
bootTime = bootEnd - bootStart
print(f"Booted in {round((bootTime * 1000), 4)} milliseconds.")
print("No fatal errors encountered during boot.")

print()
print(welcomeMessage)
login()

while True:
    command = input(f"{username.upper()}@{osname}> ")
    if command == "help":
        print(helpList)
    elif command == "logoff":
        print("You have successfully logged off.")
        login()
    elif command.startswith("output"):
        if command.startswith("output "):
            print(command.removeprefix("output "))
        else:
            print("'output' takes one argument, <str>.")
    elif command.startswith("page"):
        if command.startswith("page "):
            try:
                file = open(f"{command.removeprefix('page ')}")
                print(file.read())
            except FileNotFoundError:
                print(f"File '{command.removeprefix('page ')}' not found. Check your spelling or its existence.")
        else:
            print("'page' takes one argument, <file>.")
    elif command.startswith("username"):
        if command.startswith("username "):
            username = command.removeprefix("username ")
            print(f"Updated username to {username}.")
        else:
            print("'username' takes one argument, <str>.")
    elif command.startswith("password"):
        if command.startswith("password "):
            password = command.removeprefix("password ")
            print(f"Updated password to {password}.")
        else:
            print("'password' takes one argument, <str>.")
    elif command.startswith("osname"):
        if command.startswith("osname "):
            osname = command.removeprefix("osname ")
            print(f"Updated OS name to {osname}.")
        else:
            print("'osname' takes one argument, <str>.")
    elif command.startswith("pencil"):
        if command.startswith("pencil "):
            try:
                file = open(f"{command.removeprefix('pencil ')}")
                print(file.write())
            except FileNotFoundError:
                print(f"File '{command.removeprefix('pencil ')}' does not exist. Create it? (y/N)")
                choice = input("{username.upper()}@{osname}> ")
                if choice == "y".casefold():
                    print("File has been created.")
                else:
                    print("Aborted.")
        else:
            print("'pencil' takes one argument, <file>.")
    else:
        print(f"'{command}' not a recognised command. Use 'help' to view a list of commands.")

# like and subscribe for more epic code
