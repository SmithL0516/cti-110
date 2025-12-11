# La'Darius Smith
# 12/11/25
# Final Project
# Simple car racing game

import random
import time


# Display Introduction

def display_intro():
    print("🏎️💨Welcome to Street Racers!🏎️💨")
    print("Is your car built for speed... who will win?")
    print("GET READY!")
    print("-" * 40)
    time.sleep(1) # Tells the program to pause for 1 second before continuing

# Countdown Function
def countdown(start=3):
    print("Race starting in...")
    for i in range(start, 0, -1):
        print(i)
        time.sleep(1)
    print("GO!!!🏎️💨")
    time.sleep(0.5)

# Display the rcae track with cars
def display_positions(cars, positions, finish_line):
    print("Current Track:")
    for i in range(len(cars)):
        cars_pos = min(positions[i], finish_line) # prevent car from going past finish line
        track = "-" * cars_pos # track before the car
        space = " " * (finish_line - cars_pos) #empty space until finish
        print(f"{cars[i]}: {track}🏎️{space}|🏁")


# Function to start the race
def run_race():
    cars = ["YOU", "AI 1", "AI 2", "AI 3"]
    positions = [0,0,0,0] # starting positions of each car pre race

    finish_line = 50 # length of the race

    countdown()

    winner = None # this tracks who wins the race

    while winner is None:
        # --- Build speed by pressing ENTER ---
        print("Press ENTER as fast as you can to move foward")
        print("Press ENTER multiple times quickly to gain more speed!")
        input("Ready? Press ENTER to start your move...")

        # Counts how many times the user presses ENTER in 3 seconds
        print("GO! Start spamming ENTER!")
        start_time = time.time()
        presses = 0 

        while time.time() - start_time <3: # The 3 second window
            input()
            presses += 1

        # Players movement = number of presses + random bonus
        player_move = presses + random.randint(1,3)
        positions[0] += player_move

        # --- AI ---
        for i in range(1, 4):
            ai_move = random.randint(7, 12)
            positions[i] += ai_move

        # Display current positions
        display_positions(cars, positions, finish_line)
        
        time.sleep(0.5)

        # --- Check for winner ---
        for i in range(4):
            if positions[i] >= finish_line:
                winner = cars[i]
                break

        print("🏁 Winner:", winner, "!!! 🏁")


display_intro()
run_race()