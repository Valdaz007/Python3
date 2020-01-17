import VCode

def main():
	print("Hello World")
	
	name = VCode.getString("Enter Name: ")
	print("Hello {}!".format(name))
	
if __name__ == "__main__":
	main()