def main() :
    userInput=input("Enter Anything")
    print ("the number of spaces is", count_spaces(userInput))
def count_spaces(string):
    spaces = 0
    for char in string :
        if char == " " :
            spaces = spaces + 1
    return spaces

main()

