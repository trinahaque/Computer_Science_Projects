#wordFinder
#It runs the main
from funcs import *

def solve_puzzle():
    new_list = input_puzzle()
    your_second_variable = input()
    list_of_words = your_second_variable.split()
  #  length = len(list_of_words)
    print("Puzzle:")
    for every_word in new_list:
        print(every_word)
    #print("\n")
    
    for word in list_of_words:
        check_everything(new_list, word)


def input_puzzle():
    your_variable = input()
    #print(len(your_variable))
    #inputs the 100 character strings
 #   your_second_variable = input()
    #this inputs the words we are looking for in the puzzle
    new_list = []
    #for each_character in range(len(your_variable)):
    for each_index in range(10):
        puzzle = []
        puzzle.append(your_variable[each_index * 10:each_index * 10 + 10])
        #print(puzzle)
        new_list = new_list + puzzle
    #print(new_list)
    return new_list


def check_everything(new_list, word):
    if forward(new_list, word) != -1:
        x = forward(new_list, word)
        print(word+":", "(FORWARD) row:", x[0], "column:", x[1])
    elif backward(new_list, word) != -1:
        y = backward(new_list, word)
        print(word+":", "(BACKWARD) row:", y[0], "column:", y[1])
            
    elif up(new_list, word) != -1:
        z = up(new_list, word)
        print(word+":", "(UP) row:", z[0], "column:", z[1])
    elif down(new_list, word) != -1:
        m = down(new_list, word)
        print(word+":", "(DOWN) row:", m[0], "column:", m[1])

    else:
        print(word + ":", "word not found")


def main():
    
    solve_puzzle()


if __name__ == "__main__":
    main()
