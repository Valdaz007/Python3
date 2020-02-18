class Student:
	#Constructor
	def __init__(self, id, fname, sname, major, school, yr_entered):
		self.__std_id = id
		self.__std_fname = fname
		self.__std_sname = sname
		self.__std_major = major
		self.__std_school = school
		self.__std_yr_entered = yr_entered
		
	#Setter Methods
	def set_std_id(self, id):
		__std_id = id
		
	def set_std_fname(self, fname):
		__std_fname = fname
		
	def set_std_sname(self, sname):
		__std_sname = sname
		
	def set_std_major(self, major):
		__std_major = major
		
	def set_std_school(self, school):
		__std_school = school
		
	def set_std_yr_entered(self, yr_entered):
		__std_yr_entered = yr_entered
		
	#Getter Methods
	def get_std_id():
		return __std_id
	
	def get_std_fname():
		return __std_fname
		
	def get_std_sname():
		return __std_sname
	
	def get_std_major():
		return __std_major
	
	def get_std_school():
		return __std_school
	
	def get_std_yr_entered():
		return __std_yr_entered
		
	#Class Methods
	def display(self):
		print("{} {} {} {} {} {}\
		".format(self.__std_id, self.__std_sname, self.__std_fname, 
		self.__std_major, self.__std_school, self.__std_yr_entered))





































		

