import random

inventory = []
score = 0

def intro():
    print("Welcome Traveller!")
    print("Today we will be going through a survival game")
    print("Your job is to get through the building and make it to the end without dying")
    print ("The user with the most points wins!")
    intro_start = input("Are you ready to start? (yes or no)").lower()
    if intro_start == "yes":
        starting_room()
    else:
        print("Maybe next time you will be ready to go") 

def starting_room():
    random_bits = random.getrandbits(1)
    random_bool = bool(random_bits)
    if random_bool == True:
        answer = "yes"
    else:
        answer = "no"
    if answer == "yes":
        print("You got a special room! You have a couple of other options first")
        box_option()
    else:
        room()

def box_option():
    global inventory
    global score
    print("-------------------------------------")
    box = input("You have found a small box, a big box and a blue box, which box would you like to pick?: (small box, big box, or blue box) ")
    if box == "small box":
        print("Congratualtions! You now have a gun! The gun has no bullets though")        
        print("Now what door would you like to go through?: ")
        score += 1
        inventory.append("gun")
        room()
    elif box == "big box":
        print("Congratulations! You found a small med pack, you can save this for late if anything was to happen")
        print("Now what door would you like to go through?")
        score += 2
        inventory.append("med pack")
        room()
    elif box == "blue box":
        print("You have found bullets! I hope you have a gun to put those into?")
        score += 1
        inventory.append("bullets")
        room()
    else:
        print("Input not accepted please try again")
        box_option()

def enemy_room():
    print("-----------------------------")
    print("You encounter a Zombie!")
    print("You have ", inventory, " items in your inventory")
    action = input("What will you do?: (options: attack, use item.)").lower()
    if action =="use item":
        print("The items in your inventory are", inventory)
        if "gun" in inventory:
            use_gun = input("Would you like to use the gun? (yes or no?): ").lower()
            if use_gun == "yes" and "bullets" in inventory:
                print("You shoot the zombie and kill it")
                inventory.remove("gun")
                room()
            elif use_gun == "yes" and "bullets" not in inventory:
                print("You can't use the gun")
                print("Try Again")
                enemy_room()
            elif use_gun == "no":
                print("You chose not to use the gun")
                you_lose()
            else:
                print("Input not accepted try again")
                enemy_room()
        elif "med pack" in inventory:
            use_med_pack = input("Would you like to use the med pack? (yes or no?): ").lower()
            if use_med_pack == "yes":
                print("You throw the med pack and get away")
                inventory.remove("med pack")
                room()
            else:
                you_lose()
        elif "bullets" in inventory:
            use_bullets = input("Would you like to use the bullets? (yes or no?): ").lower()
            if use_bullets == "yes":
                print("You throw the bullets causing a distraction and get away")
                inventory.remove("bullets")
            else:
                you_lose()
        else:
            print("You have no items in your inventory to deter the zombie")
            you_lose()
    elif action  == "attack":
        print("You chose to attack!")
        print("You have nothing to deter the zombie")
        you_lose()
    
def room():
    print("----------------------------")
    number = random.randint(1,6)
    random_choice = random.getrandbits(1)
    random_bool = bool(random_choice)
    if random_bool == True:
        answer = "yes"
    else:
        answer = "no"
    if answer == "yes":
        enemy_room()
    else:
        print("You missed out on the special items")
    print("You stumble into the next room")
    print("You look around your surroundings and see no windows")
    print("You have the choice of 3 doors")
    print("left door, right door, and front door")
    room = input("What door will you go through?")
    if number == 5:
        final_room()
    elif room == "left door" or "right door" or "front door":
        starting_room()
    else: 
        print("Input not accepted please enter either left door, right door or front door")
        room()

def final_room():
    print("You have entered the final room!")
    print("BOSS FIGHT!!!!!!!")
    print("Just kidding thank you for playing the game!")
    print("Your score is ", score)
    print("if you want to play again you can do so by refreshing the game")
    exit()

def you_lose():
    print("Unfortunately you lost the game!")
    print("The zombie bit you and you ended up turning")
    play_again = input("Would you like to play again?: ")
    if play_again == "yes":
        intro()
    else:
        print("See you next time!")
        exit()
intro()