###Classical write
# py_file = open('example.txt', 'w')
# py_file.write ("Now you see me" + '\n')
# py_file.close()

###Using the 'With' statement
# with open("example_write.txt", "w") as py_file2:
#     py_file2.write("Sorry I'm gone")

###Sample code taking Inputs and writing to file
# py_file = open('example_grades.txt', 'w')
# print ('Enter grade (q to quit)')  #prints on bash not on py_file
# grade = input()
# while grade != 'q':
#     py_file.write (grade + '\n')   #prints on py_file
#     print ('Enter grade (q to quit)')
#     grade = input()
# py_file.close()

###Sample code taking Inputs and writing to file using with statement
with open('example_grades.txt', 'w') as py_file:
    print ('Enter grade (q to quit)')         #prints on bash not on py_file
    grade = input()
    while grade != 'q':
        py_file.write (grade + '\n')   #prints on py_file
        print ('Enter grade (q to quit)')
        grade = input()
