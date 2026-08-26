# read and write file with txt format:

file1 = open("practice.txt", "w")  # filename = open("directory and name file", "mode file")
# file modes:r(read), w(write), a(append)

# use file object between open and close functions
print(file1.name)  # give file name
print(file1.mode)  # give file mode
file1.write("hi")  # how to write in txt file

file1.close()  # when our use is finished, we close file object


# if we want to use easier way for use file, we use with
with open("practice.txt", "r") as file1:  # with open("file directory and name", "mode file") as name of file:
    file_content = file1.read()  # read txt file and save it in string object
    print(file_content)
    print(file1.closed)  # show file is open or close with boolean
# after with, file closing

print(file1.closed)
print(file_content)
