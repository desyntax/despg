# SOLUS by DESYNTAX - VERSION indev_2 - CREATED 24/02/26 - LAST UPDATED  - 27/02/26
print("Starting CLI...")

# imports
try:
    import time
    import os
    import sys
except ModuleNotFoundError:
    print("""Solus has run into an error and cannot import certain necessary modules. Please ensure you have the following:
time
os
sys
On your machine's command line, run 'pip install <module>'.
Press RETURN to exit.""")
    input("> ")
    exit()
except MemoryError:
    print("Solus does not have enough memory to import necessary modules. Press RETURN to exit.")
    input("> ")
    exit()
bootStart = time.time()
print("Loaded necessary modules.")

# variables
solus_info = {
    "username": "desyntax",
    "password": "password",
    "osname": "Solus"
}
welcomeMessage = "Solus CLI indev_2, created by Desyntax on 24/02/2026."
command = ""
commandList = ["help", "logoff", "output", "page", "pencil", "username", "password", "osname"]
helpList = """Solus command line interface, build indev_2. Open-sourced project.
Command format:
command <necessary_arguments> [optional_arguments]    -- Short description of command

help [command]              -- Displays this help message or info about a command
logout                      -- Logs out of Solus
output <str>                -- Prints <str> to the screen
page <file>                 -- Prints text from <file>
pencil <file> [;a]          -- Writes text in <file>
username <str>              -- Sets a new username
password <str>              -- Sets a new password
osname <str>                -- Sets a new OS name
info                        -- Prints information about Solus

Use help [command] to view more details about a command (not yet implemented)."""
print("Loaded variables.")

# definitions
def login():
    global solus_info
    print("Please sign in below.")
    while True:
        tryUsername = input("USERNAME> ")
        tryPassword = input("PASSWORD> ")
        if tryUsername == solus_info["username"] and tryPassword == solus_info["password"]:
            print(f"Logged in. Welcome, {solus_info["username"]}")
            del tryUsername, tryPassword
            break
        else:
            print("Incorrect username or password.")
def write(mode):
    file = open(f"{command.removeprefix('pencil ')}", mode)
    if mode == "w":
        print(f"{command.removeprefix('pencil ')} opened in OVERWRITE mode")
    else:
        print(f"{command.removeprefix('pencil ')} opened in APPEND mode")
    print("Type <close> to end writing and save.")
    while True:
        newline = input()
        if newline == "<close>":
            print(f"Closed {command.removeprefix('pencil ')} and saved all changes.")
            break
        file.write(newline)
    file.close()
def modifyInfo(oldName):
    if command.startswith(f"{oldName} "):
        newName = command.removeprefix(f"{oldName} ")
        solus_info[oldName] = newName
        print(f"Updated {oldName} to {newName}.")
    else:
        print(f"'{oldName}' takes one argument, <str>.")
print("Loaded definitions.")

# initialise
print(f"Found {os.cpu_count()} CPU cores.")
try:
    fileStats = str(os.stat("solus.py")).split(", ")
    fileSize = str(fileStats[6]).removeprefix("st_size=")
    print(f"Solus occupies {fileSize} bytes of disk space.")
    del fileStats, fileSize
except FileNotFoundError:
    print("Solus couldn't locate itself to record its disk usage. Proceeding anyway...")
print(f"Solus is running on a {sys.platform} system.")
bootEnd = time.time()
bootTime = bootEnd - bootStart
print(f"Booted in {round((bootTime * 1000), 4)} milliseconds.")
del bootStart, bootEnd, bootTime, time, os, sys
print("No fatal errors encountered during boot.", end="\n\n")
print(welcomeMessage, end="\n\n")
login()

while True:
    command = input(f"{solus_info["username"].upper()}@{solus_info["osname"]}> ")
    if command == "help":
        print(helpList)
    elif command == "logout":
        print("You have successfully logged out.")
        login()
    elif command.startswith("output"):
        if command.startswith("output "):
            print(command.removeprefix("output "))
        else:
            print("'output' takes one argument, <str>.")
    elif command.startswith("page"):
        if command.startswith("page "):
            try:
                file = open(command.removeprefix('page '))
                file.close()
                try:
                    file = open(f"{command.removeprefix('page ')}", "r")
                    print(file.read())
                    file.close()
                except FileNotFoundError:
                    print(f"File '{command.removeprefix('page ')}' not found. Check your spelling, its existence, or your permissions.")
            except IsADirectoryError:
                print(f"'{command.removeprefix("page ")}' is a directory, not a file.")
            except FileNotFoundError:
                print(f"'{command.removeprefix("page ")}' does not exist.")
            except PermissionError:
                print(f"Solus doesn't have permissions to read '{command.removeprefix("page ")}'. Are you root?")
        else:
            print("'page' takes one argument, <file>.")
    elif command.startswith("username"):
        modifyInfo("username")
    elif command.startswith("password"):
        modifyInfo("password")
    elif command.startswith("osname"):
        modifyInfo("osname")
    elif command.startswith("pencil"):
        if command.startswith("pencil "):
            try:
                file = open(command.removeprefix('pencil '))
                file.close()
                try:
                    command.index(f"{command.removeprefix('pencil ')}", command.find(";"))
                    write("a")
                except ValueError:
                    write("w")
            except FileNotFoundError:
                print(f"File '{command.removeprefix('pencil ')}' cannot be accessed. You may not have permissions to modify it.")
        else:
            print("'pencil' takes at least one argument, <file>.")
    elif command.startswith("info"):
        if command.startswith("info "):
            if command == "info ":
                try:
                    file = open("info.txt", "r")
                    print(file.read(), end="")
                    file.close()
                except FileNotFoundError:
                    print("'info.txt' was not found. Are you in Solus' directory?")
            else:
                print(f"'info' takes zero arguments, found one: '{command.removeprefix("info ")}'")
        else:
            try:
                file = open("info.txt", "r")
                print(file.read(), end="")
                file.close()
            except FileNotFoundError:
                    print("'info.txt' was not found. Are you in Solus' directory?")
    else:
        print(f"'{command}' is not a recognised command. Use 'help' to view a list of commands.")

# like and subscribe for more epic code

