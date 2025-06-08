import string
import time
import random

has_looked_in_pockets = 0
key = 0
points = 0
looked_around_ship = 0 
climbed_to_crows_nest = 0
read_scrap = 0
name = "cat"

inventory = []
health = 10
points = 0

def add_to_inventory(item):
    global inventory
    if item not in inventory:
        inventory.append(item)
        print("")
        print(f"-- {item} has been added to your inventory --")
    else:
        print(f"-- You already have {item} --")

def show_inventory():
    if inventory:
        print("Your gathered artifacts:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("You have no artifacts.")

def get_menu(options):
    menu_text = "What action will you take:\n"
    letter_map = {}
    for idx, (desc, key) in enumerate(options):
        letter = string.ascii_uppercase[idx]
        menu_text += f"{letter}) {desc}\n"
        letter_map[letter] = key
    return menu_text, letter_map

def meet_npc():
    print("\nA figure sits by a flickering fire, their face obscured by the shadows.")
    typewriter("Stranger: 'Few travelers reach these shores... Choose your words wisely.'")
    
    options = [
        ("Seek wisdom from the figure", "advice"),
        ("Offer a trade", "trade"),
        ("Fade into the darkness", "leave")
    ]
    
    prompt, letter_map = get_menu(options)
    user_choice = input(prompt).upper()
    action = letter_map.get(user_choice)
    
    if action == "advice":
        typewriter("Figure: 'The golden compass reveals the way beyond.'")
    elif action == "trade":
        if "golden compass" in inventory:
            typewriter("Figure: 'A torch for your golden compass. Do you accept?'")
            inventory.remove("golden compass")
            add_to_inventory("torch")
        else:
            typewriter("Figure: 'You carry nothing of worth.'")
    elif action == "leave":
        typewriter("The fire dims as you step away, leaving only silence.")
    else:
        typewriter("The figure waits, unblinking.")

def lock_picking():
    correct_combo = str(random.randint(10, 99))
    attempts = 5

    print("\nA weathered chest stands before you. A two-digit lock seals its secrets.")

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}: Enter a 2-digit code: ")
        if guess == correct_combo:
            print("The lock clicks open! A **mystic amulet** lies inside.")
            add_to_inventory("mystic amulet")
            return True
        elif int(guess) < int(correct_combo):
            print("The mechanism resists... The code is **higher**.")
        else:
            print("The mechanism resists... The code is **lower**.")
    
    print("The chest remains locked, its secrets beyond your grasp.")
    return False

def combat_rewards():
    rewards = ["healing potion", "iron sword", "gold coins", "+2 skill points"]
    reward = random.choice(rewards)
    
    print(f"The defeated foe yields **{reward}**!")
    if "points" in reward:
        global points
        points += 2
    else:
        add_to_inventory(reward)

def combat(is_final_battle=False):
    global health, points
    # Make combat slightly easier: lower enemy health and/or lower their damage, increase dodge/special success, reduce miss chance
    enemy_health = random.randint(5, 10)  # Lowered min/max
    print("\nA shadowy creature watches you from the mist.")

    while health > 0 and enemy_health > 0:
        print(f"\nYour HP: {health} | Enemy HP: {enemy_health}")
        
        options = [
            ("Quick strike (Fast but low damage)", "light"),
            ("Heavy attack (Slow but high damage)", "heavy"),
            ("Try to dodge the next attack", "dodge"),
            ("Charge up a special move", "special"),
            ("Retreat into the shadows", "run")
        ]
        
        prompt, letter_map = get_menu(options)
        user_choice = input(prompt).upper()
        action = letter_map.get(user_choice)

        if action == "light":
            damage = random.randint(3, 6)  # raised minimum damage
            enemy_health -= damage
            print(f"You land a precise strike, dealing {damage} damage!")
        
        elif action == "heavy":
            if random.random() < 0.15:  # Lowered miss chance
                print("Your heavy swing misses completely!")
            else:
                damage = random.randint(5, 9)  # slightly higher damage
                enemy_health -= damage
                print(f"You unleash a crushing blow, dealing {damage} damage!")
        
        elif action == "dodge":
            if random.random() < 0.65:  # Higher chance to dodge
                print("You evade the attack completely!")
                continue  
            else:
                print("Your attempt to dodge fails!")

        elif action == "special":
            if random.random() < 0.20:  # Higher chance of success
                print("Your energy falters—the special move fails!")
            else:
                damage = random.randint(7, 12)  # Boosted damage
                enemy_health -= damage
                print(f"A surge of force deals {damage} damage!")

        elif action == "run":
            print("You vanish into the mist, escaping unseen.")
            return False
        
        if enemy_health > 0:
            enemy_damage = random.randint(1, 4)  # Lowered enemy damage
            health -= enemy_damage
            print(f"The creature strikes, dealing {enemy_damage} damage!")

    if health <= 0:
        print("\nYour strength fails. Darkness takes hold...\n")
        print("Your adventure ends here.")
        time.sleep(3)
        exit()  
    else:
        print("You have defeated the foe!")
        combat_rewards()
        if is_final_battle:
            print("\nThe Guardian falls. The path ahead clears.\n")
            print("You step forward, victorious.\n")
            print("Congratulations! You have completed the game.")
            time.sleep(5)
            exit()  
        return True

def face_the_trial():
    global points
    
    print("\nA towering stone arch looms ahead.")
    typewriter("A cloaked guardian stands unmoving, their form lost in the night.")
    
    options = [
        ("Listen to the guardian's challenge", "listen"),
        ("Attempt to bypass unnoticed", "bypass"),
        ("Challenge the guardian in combat", "challenge"),
    ]
    
    prompt, letter_map = get_menu(options)
    user_choice = input(prompt).upper()
    action = letter_map.get(user_choice)

    if action == "listen":
        typewriter("Guardian: 'Only those who unravel riddles may proceed.'")
        riddle = input("A voice echoes: 'I speak without a mouth and hear without ears. What am I?' ").lower()
        if riddle == "echo":
            typewriter("The guardian steps aside, allowing passage.")
            points += 3
            return True
        elif riddle == "an echo":
            typewriter("The guardian steps aside, allowing passage.")
            points += 3
            return True
        else:
            typewriter("The guardian vanishes, and so does your path.")
            return False
    
    elif action == "bypass":
        typewriter("You attempt to slip past unnoticed.")
        return bool(random.randint(0, 1))
    
    elif action == "challenge":
        typewriter("You lock eyes with the Guardian, ready for battle.")
        return combat(is_final_battle=True)

def level4():
    global points
    print("\n-- LEVEL 4: THE ISLAND --")
    print("You survey the new world in front of you.\nA stranger sits by a fire, staring at the flickering tongues of the blaze.\nA strange humanoid animal sharpens a dagger on a stone.\nThe dense jungle shuffles, unforgiving and unwanting to share its secrets.")
    actions_taken = set()

    while True:
        options = []
        if "jungle" not in actions_taken:
            options.append(("Venture into the dense jungle", "jungle"))
        if "map" not in actions_taken and "jungle" in actions_taken:
            options.append(("Search ancient markings for clues", "map"))
        if "trial" not in actions_taken and "map" in actions_taken:
            options.append(("Approach the guardian's archway", "trial"))
        if "npc" not in actions_taken:
            options.append(("Meet the strange figure by a fire", "npc"))
        if "inventory" not in actions_taken:
            options.append(("Review your gathered artifacts", "inventory"))
        if "fight" not in actions_taken:
            options.append(("Face an unknown threat", "fight"))
        if "lockpick" not in actions_taken:
            options.append(("Attempt to unlock a hidden chest", "lockpick"))

        prompt, letter_map = get_menu(options)
        user_choice = input(prompt).upper()
        action = letter_map.get(user_choice)

        if action == "jungle":
            typewriter("You step into the tangled maze of vines and trees.")
            actions_taken.add("jungle")
        elif action == "map":
            typewriter("Symbols carved into ancient stones tell a cryptic story.")
            actions_taken.add("map")
            add_to_inventory("ancient map")
        elif action == "trial":
            if face_the_trial():
                return True
        elif action == "npc":
            meet_npc()
            actions_taken.add("npc")
        elif action == "inventory":
            show_inventory()
            actions_taken.add("inventory")
        elif action == "fight":
            combat()
            actions_taken.add("fight")
        elif action == "lockpick":
            lock_picking()
            actions_taken.add("lockpick")
        else:
            typewriter("The island whispers, urging you forward.")

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 7
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == number_to_guess:
            return True
        elif guess < number_to_guess:
            print("Too low")
        else:
            print("Too high")

    print("-- You have not guessed the strangers number in 7 tries.\nYou sink in to the deeps to your watery demise.\nIt seems you are not ready "+name+".")
    return False

def typewriter(input_string, delay=0.1):
    for char in input_string:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Newline at the end

def door():
    global name, points
    if key == 1:
        points = points + 1
        points_str = str(points) 
        print(f"You advance to level 2 with {points_str} points, {name}!")
        return 1
    else:
        print("You grip the door handle with two hands and pull to no avail, it is locked!")
        return  0

def add_point():
    global points
    print("-- +1 point --")
    points += 1

def symbol():
    print(" ____ ")
    print("/ ___|")
    print("\\____\\")
    print(" ___) |")
    print("|____/")

def get_menu(options):
    menu_text = "What would you like to do:\n"
    letter_map = {}
    for idx, (desc, key) in enumerate(options):
        letter = string.ascii_uppercase[idx]
        menu_text += f"{letter}) {desc}\n"
        letter_map[letter] = key
    return menu_text, letter_map

def level1():
    global has_looked_in_pockets, looked_around_ship, key, read_scrap, climbed_to_crows_nest, points
    while True:
        if has_looked_in_pockets == 0 and looked_around_ship == 0:
            options = [
                ("Look around the ship", "look_ship"),
                ("Check your pockets", "pockets"),
                ("Call out for help", "help")
            ]
            prompt, letter_map = get_menu(options)
            user_choice = input(prompt).upper()
            action = letter_map.get(user_choice)
            if action == "look_ship":
                print("Above you the crow's nest sways in the wind, to your left there is an enormous door.")
                looked_around_ship = 1
            elif action == "pockets":
                print("Inside your pockets, there is a single torn piece of paper and a key.")
                print("-- The key has been added to your inventory. --")
                add_point()
                has_looked_in_pockets = 1
                key = 1
            elif action == "help":
                print("You call out for help and see a hatch open on the deck. A huge man emerges and runs towards you.\nThe man slams into you, knocking the air out of your chest.\nEverything fades to black...")
                time.sleep(3)
                return False
            else:
                print("Please enter a valid option.")
                continue
        elif has_looked_in_pockets == 1 and looked_around_ship == 0:
            options = [("Look around the ship", "look_ship")]
            if not read_scrap:
                options.append(("Read the scrap of paper", "read_scrap"))
            options.append(("Call out for help", "help"))
            prompt, letter_map = get_menu(options)
            user_choice = input(prompt).upper()
            action = letter_map.get(user_choice)
            if action == "look_ship":
                print("Above you the crow's nest sways in the wind, to your left there is an enormous door.")
                looked_around_ship = 1
            elif action == "read_scrap":
                print("On one side of the paper is illegible writing and on the other just a symbol:")
                symbol()
                add_point()
                read_scrap = 1
            elif action == "help":
                print("You call out for help and see a hatch open on the deck. A huge man emerges and runs towards you.\nThe man slams into you, knocking the air out of your chest.\nEverything fades to black...")
                time.sleep(3)
                return False
            else:
                print("Please enter a valid option.")
                continue
        elif looked_around_ship == 1 and has_looked_in_pockets == 0:
            options = []
            if not climbed_to_crows_nest:
                options.append(("Climb to the crow's nest", "crows_nest"))
            options += [
                ("Open the door", "door"),
                ("Look in your pockets", "pockets"),
                ("Call out for help", "help")
            ]
            prompt, letter_map = get_menu(options)
            user_choice = input(prompt).upper()
            action = letter_map.get(user_choice)
            if action == "crows_nest":
                print('You climb up to the crow\'s nest and feel the sea breeze.')
                print('Scratched into the wood, you see a strange symbol:')
                symbol()
                add_point()
                climbed_to_crows_nest = 1
            elif action == "door":
                won = door()
                if won == 0:
                    continue
                else:
                    return True
            elif action == "pockets":
                print("Inside your pockets, there is a single torn piece of paper and a key.")
                add_to_inventory("Key")
                add_point()
                has_looked_in_pockets = 1
                key = 1
            elif action == "help":
                print("You call out for help and see a hatch open on the deck. A huge man emerges and runs towards you.\nThe man slams into you, knocking the air out of your chest.\nEverything fades to black...")
                time.sleep(3)
                return False
            else:
                print("Please enter a valid option.")
                continue
        elif looked_around_ship == 1 and has_looked_in_pockets == 1:
            options = []
            if not climbed_to_crows_nest:
                options.append(("Climb to the crow's nest", "crows_nest"))
            options.append(("Open the door", "door"))
            if not read_scrap:
                options.append(("Read what it says on the scrap of paper", "read_scrap"))
            options.append(("Call out for help", "help"))
            prompt, letter_map = get_menu(options)
            user_choice = input(prompt).upper()
            action = letter_map.get(user_choice)
            if action == "crows_nest":
                print('You climb up to the crow\'s nest and feel the sea breeze.')
                print('Scratched into the wood, you see a strange symbol:')
                symbol()
                add_point()
                climbed_to_crows_nest = 1
            elif action == "door":
                won = door()
                if won == 0:
                    continue
                else:
                    return True
            elif action == "read_scrap":
                print("On one side of the paper is illegible writing and on the other just a symbol:")
                symbol()
                add_point()
                read_scrap = 1
            elif action == "help":
                print("You call out for help and see a hatch open on the deck. A huge man emerges and runs towards you.\nThe man slams into you, knocking the air out of your chest.\nEverything fades to black...")
                time.sleep(3)
                return False
            else:
                print("Please enter a valid option.")
                continue

def level2():
    global points
    
    print("\n-- LEVEL 2: BELOW DECK --")
    found_lantern = False
    opened_chest = False
    investigated_noise = False
    while True:
        options = []
        if not found_lantern:
            options.append(("Pick up the lantern", "lantern"))
        if found_lantern and not opened_chest:
            options.append(("Open the chest", "chest"))
        options.append(("Investigate a strange noise", "noise"))
        options.append(("Go back upstairs", "upstairs"))
        prompt, letter_map = get_menu(options)
        user_choice = input(prompt).upper()
        action = letter_map.get(user_choice)
        if action == "lantern":
            print("You pick up the lantern. Its light reveals a small chest in the corner.")
            found_lantern = True
        elif action == "chest":
            print("You open the chest and find a golden compass. -- +2 points --")
            add_to_inventory("Golden Compass")
            opened_chest = True
            points = points + 2
            print("A bat flies out of the chest and lunges at you!")
            final_decision = input("What would you like to do?\nA) Run\nB) Attack!\nC) Call out for help\n").upper()
            if final_decision == "A":
                print("You run from the bat but it is too fast.\nIt sinks it's teeth into you and you pass out.")
                print("This is the end of your adventure today "+name+".")
                time.sleep(3)
                break
            elif final_decision == "B":    
                print("You swing at the bat but it is too fast.\nYou end up punching the wall of the cabin, your fist going through the side of the boat.\nYou sink into the icy depths.")
                print("This is the end of your adventure today "+name+".")
                time.sleep(3)
                break
            elif final_decision == "C" :
                print("You call out for help and see a hatch open. A huge man emerges and runs towards you.\nYou side step quickly and the man barrels past you.\nThe man slams into the bat.")
                points_str = str(points)
                print("You advance to Level 3 with "+points_str+" points "+name+"!")
                time.sleep(2)
                return True
        elif action == "noise":
            print("A rat scurries by. It seems harmless.")
            investigated_noise = True
        elif action == "upstairs":
            print("You head back upstairs. You are not ready for this adventure " + name +".")
            time.sleep(3)
            exit()
        else:
            print("Please enter a valid option.")
            continue

def level3():
    print("\n-- LEVEL 3: THE STRANGER --")
    print("With a jolt the ship comes to a sudden stop and water begins to fill up around your feet.\nYou rush to the door but a shadowy figure guards it.")
    print("Stranger:",end=" ")
    typewriter("Beware, for passage shall only be granted to those who unravel my secret.\nA number, veiled in obscurity, known only to me. Take heed, and may your guess be true.\n",delay = 0.1)
    print("-- The stranger has chosen a number beetween 1 and 100. You have 7 chances to guess it --")
    win = guess_the_number()
    if win == True:
        global points
        
        print("Stranger:",end=" ")
        typewriter("You have beaten me",delay=0.1)
        print("\nThe stranger steps into the shadows, and when you blink she is gone.\nYou rush to the deck and see the ship has hit land and cracked it's hull.\nYou step onto the strange island and watch the ship sink.")
        print("-- You advance to Level 4 --\n")
        time.sleep(2)
        finale = level4()
        if finale == True:
            print("__   _____  _   _  __        _____ _   _ ")
            print(r"\ \ / / _ \| | | | \ \      / /_ _| \ | |")
            print(r" \ V / | | | | | |  \ \ /\ / / | ||  \| |")
            print(r"  | || |_| | |_| |   \ V  V /  | || |\  |")
            print(r"  |_| \___/ \___/     \_/\_/  |___|_| \_|")
            points_str = str(points + 3)
            print("With "+points_str+" points "+name+"!")
            time.sleep(6)
        else:
            time.sleep(3)
            exit()
    else:
        time.sleep(3)
        exit()


print(r" ____  _____ _     _____        __  ____  _____ ____ _  __",)
print(r"| __ )| ____| |   / _ \ \      / / |  _ \| ____/ ___| |/ /",)
print(r"|  _ \|  _| | |  | | | \ \ /\ / /  | | | |  _|| |   | ' /",)
print(r"| |_) | |___| |__| |_| |\ V  V /   | |_| | |__| |___| . \ ",)
print(r"|____/|_____|_____\___/  \_/\_/    |____/|_____\____|_|\_\ ")


print("         Those who walk the watery depths...\n")
print("         Developed by Cassius Wignarajah")
print("                 A Fibonnaci Game\n")
if input("Would you like to play the game? (Y/n) ").upper() == "Y":
    name = input('What is your name adventurer? ').capitalize()
    print("\n-- LEVEL 1: THE DECK --")
    print('You awake lying on the deck of a huge ship.\nYou can only remember a feeling of intense fear and a drop.')
    result = level1()
    if result is True:
        result = level2()
        if result is True:
            level3()
else:
    print('Maybe another time!')
    time.sleep(2)
