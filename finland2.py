# FINLAND by DESYNTAX - VERSION 0.9.1 - CREATED 08/10/25 - LAST UPDATED 15/10/25 - 

# import stuff
import random as rng

# declare variables
player_hp = 100
max_player_hp = 100
day = 1 # day count
inventory = ["PVC pipe", "1998 Small hatchback", "Diesel tank", "Tourniquet"] # player inventory
distance = 0 # distance travelled (wins at 50,000)
carFuel = 10000 # current car fuel (ml)
action = None # action NOT in battle
player_attack = 0 # player's attack damage
thugChoices = ["attack", "defend", "flee"] # thug battle options
thugWeapons = ["PVC pipe", "Pocket knife", "Nunchuks", "Pipe wrench", "Flyswatter", "Fire extinguisher"] # weapons that a thug may use
weaponNames = ["PVC pipe", "Pocket knife", "Nunchuks", "Chainsaw",  "Machete", "Pipe wrench", "Brass knuckles", "Fire extinguisher", "Plate shard", "Used toilet paper", "Flyswatter"]
carNames = ["1998 Small hatchback", "2005 Pickup truck", "2020 Hybrid Kia", "2021 Mercedes Benz", "2024 Lamborghini", "F-16 Fighting Falcon", "Fisher Price car"]
healthNames = ["Plaster", "Tourniquet", "Anti-biotics", "Morphine", "Anaesthetics", "First aid kit"]
rng_num = 0 # random number generator
cash = 0 # current player bank balance
battles = 0 # battles the player engaged in
battlesWon = 0 # battles the player won
dieselUsed = 0 # ml of diesel the player consumes in a game
score = 0 # score calculated at the end of the game
rank = "" # rank by each score
playstyle = "" # how the player wants to play
health = True
current_healing_item = rng.choice(healthNames)
inventory.append(current_healing_item)

# dictionaries (help)
weapons = {
    "PVC pipe": 11,
    "Pocket knife": 19,
    "Nunchuks": 17,
    "Chainsaw": 48,
    "Machete": 35,
    "Pipe wrench": 24,
    "Brass knuckles": 22,
    "Fire extinguisher": 20,
    "Plate shard": 29,
    "Used toilet paper": 100,
    "Flyswatter": 1
    }
cars = {
    "1998 Small hatchback": 1500,
    "2005 Pickup truck": 2000,
    "2020 Hybrid Kia": 2500,
    "2021 Mercedes Benz": 3000,
    "2024 Lamborghini": 4000,
    "F-16 Fighting Falcon": 9750,
    "Fisher Price car": 100
    }
healthItems = {
    "Plaster": 5,
    "Tourniquet": 10,
    "Anti-biotics": 12,
    "Morphine": 17,
    "Painkillers": 24,
    "First aid kit": 35
}

# assign functions
def dieselCar():
    global inventory, carFuel, distance
    if "Fisher price car" in inventory:
        print("You can't fill this up with diesel, dumbass.")
    else:
        carFuel += 1000
        print(f"Used the diesel tank. Your car now has {carFuel} ml of diesel.")

def battle(maxhealth):
    global player_hp, inventory, cash, battles, battlesWon, healthNames, health,current_healing_item
    battles += 1
    thugHealth = maxhealth
    playerFleeBattle = False
    thugFleeBattle = False
    foundHealingItem = False
    print("BATTLE!")
    print("You're under attack! A thug is trying to kill you for your possessions!")
    playerWeaponChoice = inventory[0]
    playerWeaponDamage = weapons.get(playerWeaponChoice)
    thugWeaponChoice = rng.choice(thugWeapons)
    thugWeaponDamage = weapons.get(thugWeaponChoice)
    print(f"Your weapon: {playerWeaponChoice} (deals {playerWeaponDamage} dmg on hit)")
    print(f"Thug's weapon: {thugWeaponChoice} (deals {thugWeaponDamage} dmg on hit)")
    
    while True:
        thugDefend = False
        print(f"Your health: {player_hp}HP/{max_player_hp}HP")
        print(f"Thug's health: {thugHealth}HP/{maxhealth}HP")
        print("What do you do? (fight/defend/flee/heal)")
        battle_action = input("> ").casefold()
        if battle_action == "fight":
            print(f"You swing your {playerWeaponChoice} at the thug!")
        elif battle_action == "defend":
            print(f"You held back and positioned yourself defensively with your {playerWeaponChoice}.")
        elif battle_action == "flee":
            print("You tried to run away...")
        elif battle_action == "heal":
            for item in inventory:
                while health == True:
                    if player_hp == max_player_hp:
                        print("Can't use a healing item at max HP, dumbass.")
                        break
                    elif player_hp + healthItems[inventory[3]] >= max_player_hp:
                        print("Recovered to max HP.")
                        player_hp = max_player_hp
                        inventory.pop(current_healing_item)
                        health = False
                        break
                    else:
                        print(f"You used your {inventory[3]} and recovered {healthItems[inventory[3]]}HP.")
                        player_hp += healthItems[inventory[3]]
                        inventory.pop(current_healing_item)
                        health = False
                        break
        else:
            print("You did nothing. The thug did nothing too. An awkward staring contest ensues.")
        # thug makes a choice
        thugAction = rng.choice(thugChoices)
        if thugAction == "attack": # thug attack
            if battle_action == "fight":
                print("You traded hits with the thug.")
                thugHealth -= playerWeaponDamage
                print(f"Dealt {playerWeaponDamage}HP")
                player_hp -= thugWeaponDamage
                print(f"Lost {thugWeaponDamage}HP")
            elif battle_action == "defend":
                rng_battle = rng.randint(1, 100)
                if rng_battle > 33:
                    print(f"The thug swung his {thugWeaponChoice} at you, and you dodged him!")
                if rng_battle > 50:
                    print("You countered his attack!")
                    thugHealth -= playerWeaponDamage
                    print(f"Dealt {playerWeaponDamage}HP")
                elif rng_battle < 34:
                    print("You tried to avoid his attack, but he hit you anyway.")
                    player_hp -= round(thugWeaponDamage / 2)
                    print(f"Lost {round(int(thugWeaponDamage / 2))}HP")
            elif battle_action == "flee":
                print(f"The thug caught up to you before you could escape, and struck you with his {thugWeaponChoice}.")
                player_hp -= round(thugWeaponDamage / 2)
                print(f"Lost {round(int(thugWeaponDamage / 2))}HP")
            elif battle_action == "heal":
                print(f"The thug struck you with his {thugWeaponChoice} while you were healing yourself!")
                print(f"Lost {thugWeaponDamage}HP")
                player_hp -= thugWeaponDamage
        elif thugAction == "defend": # thug defend
            if battle_action == "fight":
                print("He dodged your attack.")
                rng_battle = rng.randint(1, 100)
                if rng_battle > 70:
                    print("He countered your attack!")
                    player_hp -= round(thugWeaponDamage / 2)
                    print(f"Lost {round(thugWeaponDamage / 2)}HP")
            elif battle_action == "defend":
                print("The thug expected an attack from you... but neither of you swung.")
                print("No outcome.")
            elif battle_action == "flee":
                playerFleeBattle = True
        elif thugAction == "flee": # thug flee
            if battle_action == "fight":
                print("The thug tried to escape, but you got to him in time!")
                thugHealth -= playerWeaponDamage
                print(f"Dealt {playerWeaponDamage}HP")
            elif battle_action == "defend":
                thugFleeBattle = True
            elif battle_action == "flee":
                print("You both ran away from each other. Cowards.")
                playerFleeBattle = True
            elif battle_action == "heal":
                print("The thug ran away while you were healing yourself.")
                thugFleeBattle == True
        if thugHealth < 1:
            print("YOU WON!")
            cash += thugWeaponDamage * 3
            print(f"Gained £{thugWeaponDamage * 3}!")
            battlesWon += 1
            break
        elif thugFleeBattle == True:
            print("The thug ran away...")
            print("Gained no cash.")
            break
        elif playerFleeBattle == True:
            print("YOU ESCAPED!")
            print("Gained no cash.")
            break
        elif player_hp < 1:
            print("You lost...")
            print("Please restart the game to try again.")
            input("> ")
            exit()
    print("Press RETURN to continue.")
    input("> ")

def carDealership():
    global rng_num, inventory, cars, carNames, action
    print("You stopped off at a car dealership. The salesman there tells you that their stock is low because of thugs stealing and trashing their cars.")
    rng_num = rng.randint(1, 100)
    if rng_num >= 33:
        print("However, he tells you that there's still a vehicle for sale.")
        rng_choice = rng.choice(carNames)
        print(f"Vehicle: {rng_choice}. Max distance this vehicle can travel in one day: {cars[rng_choice]}. Price: £{cars[rng_choice] / 10}.")
        print("Purchase? (Y/N)")
        action = input("> ").casefold()
        if action == "y":
            if cash >= cars[rng_choice] / 10:
                print(f"You bought the {rng_choice}!")
                inventory.insert(1, rng_choice)
            else:
                print("You're too poor to buy this. Lmao.")
        elif action == "n":
            print("You told the salesman you didn't like it. He nods and wishes you a good day.")
    else:
        print("Unfortunately, he doesn't have any vehicles in good condition to sell you. Come back later.")

# intro
print("Greetings, traveller. First, let's get your name.")
name = input("> ")
print(f"Hello, {name}. Today is the first day of your adventure to the fictional country of Finland.")
print("What playstyle do you like? (tactical OR brute)")
playstyle = input("> ")
if playstyle == "tactical":
    print("An excellent choice. Your attacks will deal less damage but will have greater odds of landing.")
elif playstyle == "brute":
    print("Feisty! I like it. Your attacks will deal much greater damage but will have lesser odds of landing.")
else:
    print("Not sure what that means, but I reckon Brute will be best for you.")
    playstyle = "brute"
print("Press RETURN to start your journey.")
input("> ")

# forever loop and display current stats
while True:
    if player_hp > max_player_hp:
        player_hp = max_player_hp

    print()
    print(f"DAY {day}.")
    print("Your current stats:")
    print(f"Health: {player_hp}HP/{max_player_hp}HP")
    print(f"Inventory: {inventory}")
    print(f"So far, you have travelled {distance} metres towards Finland's borders. Distance to travel: {50000 - distance}")
    print(f"Bank balance: £{cash}")

# pick daily action
    print(f"Your car has {carFuel} ml of fuel remaining (Travelling consumes 500 ml per round).")
    print("What do you do? (travel/refill car/gas station/car dealership/pharmacy)")
    action = input("> ").casefold()
    if action == "travel":
        rng_num = rng.randint(1, 100)
        if rng_num >= 80:
            battle(rng_num)
        else:
            if carFuel < 500:
                print("You don't have enough fuel to drive. Get fuel at the gas station.")
            else:
                print(f"You travelled a bit in your {inventory[1]}. Just some smooth sailing for today.")
                distance += rng.randint(int(cars[inventory[1]] / 2), int(cars[inventory[1]]))
                carFuel -= 500
                dieselUsed += 500
    elif action == "refill car":
        if "Diesel tank" not in inventory:
            print("You don't have any diesel tanks to refill your car.")
        else:
            carFuel += 1500
            print("Refueled your car with the diesel tank.")
            print(f"Car fuel: {carFuel} ml")
            inventory.remove("Diesel tank")
    elif action == "gas station":
        print("You went to the gas station.")
        rng_num = rng.randint(1, 100)
        if rng_num >= 50:
            if "Diesel tank" in inventory:
                print("You already have a diesel tank for your car. You don't need two, fatass.")
            else:
                print("You found a diesel tank for your car.")
                inventory.append("Diesel tank")
        else:
            print("You didn't find anything for your car.")
        print("Search the store? (Y/N)")
        action = input("> ").casefold()
        if action == "y":
            print("You entered the gas station convenience store.")
            rng_num = rng.randint(1, 100)
            if rng_num >= 33:
                if rng_num >= 80:
                    print("Uh oh! Someone else is looting the store!")
                    battle(rng_num)
                else:
                    rng_weapon = rng.choice(weaponNames)
                    print(f"You found a {rng_weapon}! (Damage output: {weapons[rng_weapon]} DMG)")
                    print(f"Current weapon: {inventory[0]} (Damage output: {weapons[inventory[0]]} DMG)")
                    print("Take it? (Y/N)")
                    action = input("> ").casefold()
                    if action == "y":
                        print("You threw away your old weapon and wielded this one anew.")
                        inventory[0] = rng_weapon
                    else:
                        print("You thought against it. Why take it after all?")
            else:
                print("You didn't find anything useful.")
        else:
            print("You left the gas station store alone. Could have been a thug in there for all you know.")
    elif action == "car dealership":
        carDealership()
    elif action == "pharmacy":
        print("You went to the pharmacy.")
        print("")
        rng_num = rng.randint(1, 100)
        if rng_num >= 50:
            print("The pharmacist luckily had something for you.")
            rng_choice = rng.choice(healthNames)
            print(f"OFFER: {rng_choice}")
            print(f"Recovers: {healthItems[rng_choice]}HP")
            print(f"Price: £{healthItems[rng_choice] / 2}")
            print(f"Purchase {rng_choice}? (Y/N)")
            action = input("> ").casefold()
            if action == "y":
                if cash < healthItems[rng_choice] / 2:
                    print("You're too poor to buy that, idiot.")
                else:
                    inventory.append(rng_choice)
                    print(f"You bought the {rng_choice}. The pharmacist wishes you well.")
            elif action == "n":
                print("You decline the offer. The pharmacist tells you to have a good day.")
            else:
                print("You tried to utter something, but gibberish came out. The pharmacist looks at you weird. Out of sheer embarrassment, you hastily leave the pharmacy.")
		
        else:
            print("The pharmacist tells you that the store has been looted by thugs. He doesn't have anything for sale.")
    else:
        print("You got confused that day and forgot what you were doing. You spent the night doing nothing, and by the next morning you remembered what it is you were meant to do.")
    
    day += 1
    if distance > 49999:
        break

print("CONGRATULATIONS!")
print(f"Reached Finland in {day} days.")
print(f"Remaining health: {player_hp}")
print(f"Battles fought: {battles}")
print(f"Battles won: {battlesWon}")
print(f"Total diesel consumed: {dieselUsed}ml")
score = player_hp + battles + (battlesWon * 10) + (dieselUsed / 100)
print(f"FINAL SCORE: {score}")
if score < 39:
    rank = "D"
elif score >= 40 and score < 49:
    rank = "C"
elif score >= 50 and score < 59:
    rank = "B"
elif score >= 60 and score < 69:
    rank = "A"
elif score >= 70 and score < 79:
    rank = "A*"
else:
    rank = "S"
print(f"GRADE: {rank}")
if rank == "S":
    print("WOW! INCREDIBLE!")
elif rank == "A*":
    print("Phenomenal job!")
elif rank == "A":
    print("Nice work!")
elif rank == "D":
    print("At least you made it out alive.")
else:
    print("Well done!")
print()
print("Press RETURN to quit.")
input("> ")


# like and subscribe for more cool code like this
