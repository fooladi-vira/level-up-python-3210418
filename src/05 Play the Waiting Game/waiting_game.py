import time
import random

def waiting_game():
    target_time = random.randint(2, 4)
    print(f"Your target time is {target_time} seconds.")
    
    input("Press Enter to start the timer...")
    start_time = time.time()
    
    input(f"Press Enter again after {target_time} seconds...")
    elapsed_time = time.time() - start_time
    
    print(f"Elapsed time: {elapsed_time:.3f} seconds.")
    
    if elapsed_time == target_time:
        print("You're right on target! Congratulations!")
    elif elapsed_time < target_time:
        print(f"You were {target_time - elapsed_time:.3f} seconds too fast. Try again!")
    else:
        print(f"You were {elapsed_time - target_time:.3f} seconds too slow. Try again!")

# Run the game
waiting_game()
