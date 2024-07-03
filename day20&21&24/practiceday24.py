# working with files
# file  = open("file.txt")   # opens the file and saves it in file variable
# contents = file.read()    #stores the contents in the file in content variable
# file.close()        # closes the file



# can also open using with keyword:

# with open("file.txt") as file:   # with 'with' keyword, you dont need to close the file manually using close()
#     contents = file.read()


# with open("file.txt", mode = "w") as file:    # w = write mode, a = append mode, r = read mode, 
#     file.write("New Text")

# if a file doesnt exist, it creates the file, only works in write mode
