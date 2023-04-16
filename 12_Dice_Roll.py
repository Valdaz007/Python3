import random  # Module for Generating a Random Number

def roll_Dice() -> int:
	return random.randrange(1, 7, 1) # Generate a Random Number between 1 & 6

if __name__ == "__main__":
	print(roll_Dice())
