######Classical Reading of File
# file = open("example_grades.txt", mode="r")
# file_contents = file.read()
# print(file_contents)
# file.close()

#####The with statement.
with open("example_grades.txt", mode="r") as file:
	file_contents = file.read()
	print(file_contents)
