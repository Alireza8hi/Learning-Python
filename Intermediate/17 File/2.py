with open("practice.txt", "w") as file1:
    file1.write("hi ali\nhi mohammad\n hi reza")

# we can read information on file in 3 ways

# first way
with open("practice.txt", "r") as file1:
    file1_content = file1.readlines()  # get every line from file in a list of lines

print("first way\n")
print(file1_content)
print(file1_content[1])

# second way
with open("practice.txt", "r") as file1:
    file1_content = file1.read()  # get all file in a string object

print("\n\nsecond way\n")
print(file1_content)

# third way
with open("practice.txt", "r") as file1:
    line1 = file1.readline()  # get a line in file
    line2 = file1.readline()  # get next line in file
    line3 = file1.readline()  # get next line in file

print("\n\nthird way\n")
print(line1, line2, line3)

# third wqy(again)
with open("practice.txt", "r") as file1:
    print("\n\nthird way(again)\n")
    for line in file1:
        print(line)


# you can get n first characters this way:
with open("practice.txt", "r") as file1:
    file1_content = file1.readlines(6)  # it means get me 6 first characters of that
    file1_content2 = file1.readline(5)  # it means get me 5 next characters of that
    file1_content3 = file1.readline(7)  # it means get me 7 next characters of that

print("\n\nfinal way\n")
print(file1_content)
print(file1_content2)
print(file1_content3)
