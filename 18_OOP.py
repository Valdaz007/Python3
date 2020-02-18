from TrialCode01 import Student

def main():
	li_std = [] # Create An Empty List
	li_std.append(Student(20161232, "Victor", "Volsavai", "Physics", "SNPS", 2016))
	li_std.append(Student(20161004, "Tyran", "Ainui", "Geology", "SNPS", 2016))
	
	display_all(li_std)
	
def display_all(list):
	for student in list:
		student.display()
	
if __name__ == "__main__":
	main()