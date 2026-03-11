# SOLUS by DESYNTAX - VERSION indev_3 - CREATED 24/02/26 - LAST UPDATED 10/03/26
print("Starting CLI...")
dangerousProceed = ""

# imports
try:
    import time, os, sys, shutil, configparser
    from pathlib import Path
except ModuleNotFoundError:
    print("""Solus has run into an error and cannot import certain necessary modules. Please ensure you have the following:
time
os
sys
shutil
pathlib
configparser
On your machine's command line, run 'pip install <module>'.
You should be able to run Solus without these modules imported, but some functionalities could be broken because of this.
Proceed? (y/N)""")
    dangerousProceed = input("> ")
    if dangerousProceed == "y".casefold():
        print("Skipping module imports.")
    else:
        exit()
except MemoryError:
    print("Solus does not have enough memory to import necessary modules. Press RETURN to exit.")
    input("> ")
    exit()
bootStart = time.time()
print("Loaded necessary modules.")

# config
config = configparser.ConfigParser()
config.read("config.txt")
solus_info = {
    "username": config['SOLUS_INFO']['username'],
    "password": config['SOLUS_INFO']['password'],
    "solusname": config['SOLUS_INFO']['solusname']
}
print("Loaded configuration file.")

# variables
welcomeMessage = "Solus CLI indev_3, created by Desyntax on 24/02/2026."
command = ""
cwd = __file__.removesuffix("solus.py")
inSolusDirectory = "$"
helpList = """Solus command line interface, build indev_3. Open-sourced project.
Command format:
command <necessary_arguments> [;optional_arguments] -- Description [modules_necessary]
Interpreter format:
(USERNAME)@(Solusname)(directory)>

help [command]          -- Displays this help message
logout                  -- Logs out of Solus
output <str>            -- Prints <str> to the screen
ls                      -- Prints files and dirs in CWD to the screen [os]
cwd <dir>               -- Changes current working directory to <dir> [os]
page <file>             -- Prints text from <file>
nano <file> [;a]        -- Writes text in <file>
banana <dir>            -- Creates a directory called <dir> [os]
touch <file>            -- Creates a file called <file> [pathlib]
boom <file              -- Deletes <file> from current directory [shutil, os]
rep <file> <str>        -- Renames <file> to <str>
username <str>          -- Sets a new username
password <str>          -- Sets a new password
solusname <str>         -- Sets a new name for Solus
info                    -- Prints information about Solus
copyright               -- Prints copyright information about Solus

Use help [command] to view more details about a command."""
copyr = "Solus indev_2, created by Desyntax. All content, including code, are public domain."
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
    file = open(f"{command.removeprefix('nano ')}", mode)
    if mode == "w":
        print(f"{command.removeprefix('nano ')} opened in OVERWRITE mode")
    else:
        print(f"{command.removeprefix('nano ')} opened in APPEND mode")
    print("Type <close> to end writing and save.")
    while True:
        newline = input()
        if newline == "<close>":
            print(f"Closed {command.removeprefix('nano ')} and saved all changes.")
            break
        file.write(newline + "\n")
    file.close()
def modifyInfo(part):
    global config, solus_info
    if command.startswith(f"{part} "):
        newName = command.removeprefix(f"{part} ")
        config['SOLUS_INFO'][part] = newName
        print(f"Updated {part} to {newName}.")
    else:
        print(f"'{part}' takes one argument, <str>.")
print("Loaded definitions.")

# initialise
if dangerousProceed != "y":
    print(f"Found {os.cpu_count()} CPU threads.")
    try:
        fileStats = str(os.stat(__file__)).split(", ")
        fileSize = str(fileStats[6]).removeprefix("st_size=")
        fileSize = int(fileSize)
        print(f"Solus occupies {fileSize:,d} bytes of disk space.")
        del fileStats, fileSize
    except FileNotFoundError:
        print("Solus couldn't locate itself to record its disk usage. Proceeding anyway...")
    print(f"Solus is running on a {sys.platform} system.")
    bootEnd = time.time()
    bootTime = bootEnd - bootStart
    print(f"Booted in {round((bootTime * 1000), 4)} milliseconds.")
    del bootStart, bootEnd, bootTime
else:
    print("Skipped checking OS due to missing modules.")
del dangerousProceed
print("No fatal errors encountered during boot.", end="\n\n")
print(welcomeMessage, end="\n\n")
login()

while True:
    command = input(f"{solus_info['username'].upper()}@{solus_info['solusname']}{inSolusDirectory}> ")
    if command == "help": # help
        print(helpList)
    elif command == "logout": # logout
        print("You have successfully logged out.")
        login()
    elif command.startswith("output"): # output
        if command.startswith("output "):
            print(command.removeprefix("output "))
        else:
            print("'output' takes one argument, <str>.")
    elif command.startswith("page"): # page
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
                print(f"'{command.removeprefix('page ')}' is a directory, not a file.")
            except FileNotFoundError:
                print(f"'{command.removeprefix('page ')}' does not exist.")
            except PermissionError:
                print(f"Solus doesn't have permissions to read '{command.removeprefix('page ')}'. Are you root?")
            except OSError:
                print(f"Solus couldn't open '{command.removeprefix('page ')}'.")
            except UnicodeDecodeError:
                print(f"'{command.removeprefix('page ')}' can't be read because of a Unicode decode error.")
            except MemoryError:
                print("There isn't enough memory on this system to read this file.")
        else:
            print("'page' takes one argument, <file>.")
    elif command.startswith("username"): # username
        modifyInfo("username")
    elif command.startswith("password"): # password
        modifyInfo("password")
    elif command.startswith("solusname"): # solusname
        modifyInfo("solusname")
    elif command.startswith("nano"): # pencil
        if command.startswith("nano "):
            try:
                file = open(command.removeprefix('nano '))
                file.close()
                try:
                    command.index(f"{command.removeprefix('nano ')}", command.find(";"))
                    write("a")
                except Exception:
                    write("w")
            except FileNotFoundError:
                print(f"File '{command.removeprefix('nano ')}' cannot be accessed. You may not have permissions to modify it.")
            except PermissionError:
                print(f"File '{command.removeprefix('nano ')}' cannot be accessed due to unqualified permission.")
        else:
            print("'nano' takes at least one argument, <file>.")
    elif command.startswith("info"): # info
        if command.startswith("info "):
            if command == "info ":
                try:
                    file = open("info.txt", "r")
                    print(file.read(), end="\n")
                    file.close()
                except FileNotFoundError:
                    print("'info.txt' was not found. Are you in Solus' directory?")
                except PermissionError:
                    print("'info.txt' could not be read.")
            else:
                print(f"'info' takes zero arguments.")
        else:
            try:
                file = open("info.txt", "r")
                print(file.read(), end="")
                file.close()
            except FileNotFoundError:
                    print("'info.txt' was not found. Are you in Solus' directory?")
    elif command.startswith("rep"): # retitle
        if command.startswith("rep "):
            rep()
            os.rename(rep[1], rep[2])
            print(f"Successfully renamed {rep[1]} to {rep[2]}.")
        else:
            print("'rep' takes at least two arguments, <file> and <name>.")
    elif command.startswith("ls"): # ls
        if command.startswith("ls "):
            print("'ls' takes zero arguments.")
        else:
            print(f"All in '{cwd}':")
            print(os.listdir(cwd))
    elif command.startswith("cwd"):  # cwd
        if command.startswith("cwd "):
            try:
                new_dir = command.removeprefix("cwd ")
                os.chdir(new_dir)
                cwd = os.getcwd()
                print(f"Changed directory to '{cwd}'")
                del new_dir
            except FileNotFoundError:
                print(f"Directory '{command.removeprefix('cwd ')}' doesn't exist.")
            except NotADirectoryError:
                print(f"'{command.removeprefix('cwd')}' is a file, not a directory.")
            except PermissionError:
                print(f"Solus doesn't have permission to change to this directory.")
            except OSError:
                print(f"Your operating system ran into an issue trying to perform this task.")
        else:
            print("'cwd' takes at least one argument, <dir>.")
    elif command.startswith("copyright"):
        if command.startswith("copyright "):
            print("'copyright' takes zero arguments.")
        else:
            print(copyr)
    elif command.startswith("boom"):
        if command.startswith("boom "):
            try:
                os.remove(command.removeprefix("boom "))
                print(f"Successfully deleted '{command.removeprefix('boom ')}'.")
            except Exception:
                print(f"'{command.removeprefix('boom ')}' is a directory. Would you like to remove it? (y/N)")
                choice = input("> ")
                if choice == "y":
                    try:
                        shutil.rmtree(command.removeprefix('boom '))
                        print(f"Successfully removed '{command.removeprefix('boom ')}'")
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print("Aborted.")
        else:
            print("'rm' takes at least one argument, <file>")
    elif command.startswith("banana"):
        if command.startswith("banana "):
            try:
                os.mkdir(command.removeprefix("banana "))
                print(f"Created directory '{command.removeprefix('banana ')}' in '{cwd}'.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("'banana' takes at least one argument, <dir>")
    elif command.startswith("touch"):
        if command.startswith("touch "):
            try:
                Path(f"{command.removeprefix('touch ')}").touch()
                print(f"Sucessfully created '{command.removeprefix('touch ')}' at '{cwd}'")
            except FileExistsError:
                print(f"'{command.removeprefix('touch ')}' already exists in '{cwd}'.")
            except PermissionError:
                print("Solus doesn't have the necessary permissions to perform this.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("'touch' takes at least one argument, <file>.")
                
    else:
        print(f"'{command}' not a recognised command. Use 'help' to view a list of commands.")
    if cwd == __file__.removesuffix("solus.py"):
        inSolusDirectory = "$"
    else:
        inSolusDirectory = "~"

# like and subscribe for more epic code

