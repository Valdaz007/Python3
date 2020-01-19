import random

def main():
	print("Welcome To Ezekiel's Brain Thinking Game!\n")
	print("\nPress Enter To Continue... ")
	input()
	while True:
		print("\nThink Of A Number Less Than 20")
		input("Press Enter To Continue... ")
		print("\nAdd This Number With Itself")
		input("Press Enter To Continue... ")
		numberToAdd = random.randrange(0, 100, 2)
		print("\nAdd {} To Your Answer".format(numberToAdd))
		input("Press Enter To Continue... ")
		print("\nDivide Your Answer By 2")
		input("Press Enter To Continue... ")
		print("\nMinus Your Answer By The Number You Have Chosen")
		input("Press Enter To Continue... ")
		numberToAdd /= 2
		print("\nYour Answer Is: {}".format(numberToAdd))
		print()
		cont_end = input("Press Enter To Continue or Press 'Q' To Quit The Game! => ")
		if cont_end == "Q" or cont_end == "q":
			break;
if __name__ == "__main__":
	main()