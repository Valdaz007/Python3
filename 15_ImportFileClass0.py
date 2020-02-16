import VCode

class ExportClass:
	def __init__(self): //Constructor
		name = None
		id = None

	def createName(self):
		self.name = VCode.getString("Enter Name: ")
		
	def displayName(self):
		return self.name
		
	def displayId(seld):
		return self.id
	
	def saying(self):
		print("Hello {}".format(self.name))