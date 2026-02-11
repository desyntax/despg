# ROCK PAPER SCISSORS (RPS) - VERSION 0.3.4 ALPHA (25/11/2025) - CREATED: 26/09/2024 BY: desyntax

# If you're looking for some kick-ass code to borrow, you've come to the WRONG PLACE! This code is so out-of-the-box it feels like you've just stumbled across a GeeksforGeeks example.
# Python is the future of programming, so write the code before an AI does it faster than you.

# imports
import random as rng
import array as ar

# variables and tables
cpu = "" # cpu's rps choice
fullopt = ["rock", "paper", "scissors"] # list of all choices in FULL form
opt = ["r", "p", "s"] # list of all choices in ABBREVIATED form
usr = "" # user's rps choice
userscore = 0
cpuscore = 0
ans = "" # game end input response from user
streakHolder = None # who holds the streak
streak = 0 # current streak count
balance = 20 # user's current balance. UNUSED!!
draw = False # boolean for tied result
win = "" # string value for printing who won
cpuName = "cpu" # customised name for cpu
error = False # determines whether user inputted incorrect rps choice
evil = False # evil mode
update = "[UPDATE 0.3.4 ALPHA | 25/11/2025]: added username customisation and a few easter eggs >:3"
username = "" # username to display on results

# definitions
def game_end(winner):
    global streak, streakHolder, win
    print(win, " wins!", sep="")
    print()
    if(streakHolder != win):
        if(streakHolder is None):
            print("the first winner is ", win, "!", sep="")
        if(streakHolder is not None):
            print(streakHolder, "'s streak of ", streak, " has been beaten!", sep="")
            streak = 0
    streak += 1
    streakHolder = win
    if(streak >= 5):
        if(streak >= 10):
            print(streakHolder, " is on an incredible streak of ", streak, sep="")
        else:
            print(streakHolder, " is on an amazing streak of ", streak, sep="")
    if(streakHolder is not None):
        print(streakHolder, " is on a ", streak, " streak", sep="")
    else:
        print("no one has a streak yet")

def record():
    global usr, cpu, userscore, cpuscore, draw, win
    try:
        with open("rpsRecords.txt", "a") as file:
            file.write(f"{usr} vs {cpu}\n")
            if(draw == False):
                file.write(f"OUTCOME: {win}\n")
                file.write(f"SCORE: {username}: {userscore}, CPU: {cpuscore}\n")
                file.write("\n")
            if(draw == True):
                file.write("OUTCOME: DRAW\n")
                file.write(f"SCORE: {username}: {userscore}, CPU: {cpuscore}\n")
                file.write("\n")
    except FileNotFoundError:
        input("'rpsRecords.txt' not found. creating file...")

def init_record():
    try:
        with open("rpsRecords.txt", "a") as file:
            file.write("--- NEW GAME ---\n")
            file.write(f"USER NAME: {username}\n")
    except FileNotFoundError:
        input("'rpsRecords.txt' not found. creating file...")

# main code

# initialise
print("welcome to rock paper scissors, where you'll be going toe-to-toe with the computer at hand!")
print("you may use full form (rock, paper, scissors) or abbreviated form (r, p, s)! type 'update' in the round end prompt to view the most recent update")

print("firstly, if you'd like to give yourself a username, please do so below (leaving this blank will default your username to 'user')")
username = input("> ")
if username == "":
    username = "user"
elif username == "cpu":
    print("you can't have that as your name, silly!")
    print("defaulting your name to cutie! :3")
    username = "cutie"
else:
    print(f"hello, {username}! let the games commence.")

init_record()

# start permanent loop
while True:

# user makes choice
    print("rock paper scissors shoot!")
    usr = input("> ")
    if(usr in opt):
        if(usr == "r"):
            usr = "rock"
        elif(usr == "p"):
            usr = "paper"
        elif(usr == "s"):
            usr = "scissors"
    elif(usr not in fullopt):
        print("error: user listed invalid choice")
        with open("rpsRecords.txt", "a") as file:
            file.write("ERROR: INVALID PLAY BY USER\n")

# cpu makes random choice
    if(error == False):
        if(evil == False):
            cpu = rng.choice(fullopt)
            print(cpu)
        else:
            if(usr == "rock"):
                cpu = "paper"
            elif(usr == "paper"):
                cpu = "scissors"
            else:
                cpu = "rock"
# determine who wins
    if(error == False):
        if(usr == "rock" and cpu == "scissors"):
            win = username
            game_end(usr)
            userscore += 1
            draw = False
        if(usr == "rock" and cpu == "paper"):
            win = cpuName
            game_end(cpu)
            cpuscore += 1
            draw = False
        if(usr == "rock" and cpu == "rock"):
            print("draw!")
            draw = True
            print(streakHolder, " is on a ", streak, " streak", sep="")

        if(usr == "paper" and cpu == "rock"):
            win = username
            game_end(usr)
            userscore += 1
            draw = False
        if(usr == "paper" and cpu == "scissors"):
            win = cpuName
            game_end(cpu)
            cpuscore += 1
            draw = False
        if(usr == "paper" and cpu == "paper"):
            print("draw!")
            draw = True
            print(streakHolder, " is on a ", streak, " streak", sep="")

        if(usr == "scissors" and cpu == "paper"):
            win = username
            game_end(usr)
            userscore += 1
            draw = False
        if(usr == "scissors" and cpu == "rock"):
            win = cpuName
            game_end(cpu)
            cpuscore += 1
            draw = False
        if(usr == "scissors" and cpu == "scissors"):
            print("draw!")
            draw = True
            print(streakHolder, " is on a ", streak, " streak", sep="")

# print results
    if(error == False):
        record()
        print()
        print(f"{username}'s score: {userscore}, {cpuName}'s score: {cpuscore}")
        print("play again? (type quit to stop; update to view most recent update; clear to clear rpsRecords.txt; rename to customise the cpu's name)")
        ans = input("> ")
        if(ans == "quit"):
            quit()
        elif(ans == "update"):
            print(update)
        elif(ans == "clear"):
            with open("rpsRecords.txt", "w") as file:
                file.write("--- CLEARED ---\n")
        elif(ans == "rename"):
            print(f"rename the cpu (currently {cpuName}) to...")
            while True:
                cpuName = input("> ")
                if cpuName == "user" or cpuName == "usr":
                    print("you can't call it that!")
                elif cpuName == "command_reset":
                    print()
                    cpuscore = 0
                    userscore = 0
                    streak = 0
                    streakHolder = None
                    cpuName = "cpu"
                    break
                elif cpuName == "BIG MALLAH":
                    evil = True
                    print("THINE END IS NIGH.")
                    print("BIG MALLAH, THE WISE AND THE HOLY, SHALL JUDGE THOU THROUGH THIS INTERFACE.")
                    break
                elif cpuName == "command_endgame":
                    quit()
                elif cpuName == "coughing baby":
                    userscore += 1945
                    cpuscore = 0
                    break
                else:
                    print(f"success! the cpu is now called {cpuName}.")
                    evil = False
                    break
            print()
        elif(ans == "givemescore" and evil == True):
            print("no >:(")
            userscore -= 1
            print("-1 user score")
        elif(ans == "givemescore" and evil == False):
            print("okay! :3")
            userscore += 1
            print("+1 user score")

# like and subscribe for more epic code
