file_name = input("Enter the file name")
file = open(file_name, 'r')
lines = file.readlines()

if len(lines) >= 3:
    third_line = lines[2].strip()
    words = third_line.split()
    for word in words:
        print(word)
else:
    print("Not enough lines in file")

file.close()