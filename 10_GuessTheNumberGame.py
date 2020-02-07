import random #In-Built Module
import VCode  #Very Own Module
def main(): #Main Function
	print("\n\nWelcome to the Guess the Number Game!") #Prompt User On CMD
	while True:		#While Loop
		rand_number = random_Gen() #Generate A Random Number & Store In Variable
		var = input("Press Enter Key to Continue or Press Q to Quit\n") #Get Input From User
		if var == "q" or var == "Q": #Check If Input Is 'Q' or 'q'
			break	#If So Break Out Of Loop Ending Program
		else: #Else
			compare_Rand(rand_number)
		#End If-Else Statements
	#End While Loop
#End Main Function
def random_Gen(): #Function To Generate A Random Number
	return random.randrange(0, 101, 1) #Using Random Module Generate A Random Number Between 0 & 101
def compare_Rand(rand_input):
	counter = 6
	while counter > 0: 
		rand = VCode.getInt("\nEnter Your Guess: ")
		counter -= 1
		if rand == rand_input:
			print("You Have Successfully Guess The Random Generated Number")
			break
		elif counter == 0:
			print(f"\nRandom Number = {rand_input}. Your Number of Choices are Up. Try Again!")
			break
		elif rand < rand_input:
			print(f"Input is Less Than The Random Number! Number of Choices Left {counter}")
			continue
		elif rand > rand_input:
			print(f"Input is Greater Than The Random Number! Number of Choices Left {counter}")
			continue
		#End If Statements
	#End While Loop
if __name__ == "__main__": #Check If There Is A Function Call Main
	main() 	#If So Then Call The Main Function