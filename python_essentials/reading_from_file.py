######Classical Reading of File
# file = open("example_grades.txt", mode="r")
# file_contents = file.read()
# print(file_contents)
# file.close()

#####The with statement.
with open("example_grades.txt", mode="r") as file:     #Complete file path not used means python script is run from the folder 
	file_contents = file.read()
	print(file_contents)
