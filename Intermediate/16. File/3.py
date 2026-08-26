lines = ["This is line B\n", "This is line C\n", "This is line A\n", "This is line D\n"]

with open("example.txt", "w") as File1:
    for line in lines:
        File1.write(line)

# we have nested open with
with open("example.txt", "r") as File1:
    File1_content = File1.readlines()

    with open("example2.txt", "w") as File2:
        for line in File1_content:
            File2.write(line)

print(File1_content)

with open("example.txt", "a") as File1:
    File1.write("This is line E")

with open("example.txt", "r") as File1:
    File1_content = File1.readlines()

with open("example2.txt", "r") as File2:
    File2_content = File2.readlines()

print(File1_content)
print(File2_content)
