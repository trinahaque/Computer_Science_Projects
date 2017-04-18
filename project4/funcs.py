#Project 4
#Trina Haque
#Word Search Puzzle

###def solve_puzzle():
##   input_puzzle()
##   your_second_variable = input()


##def input_puzzle():
##    your_variable = input()
##    #inputs the 100 character strings
## #   your_second_variable = input()
##    #this inputs the words we are looking for in the puzzle
##    new_list = []
##    #for each_character in range(len(your_variable)):
##    for each_index in range(10):
##        puzzle = []
##        puzzle.append(your_variable[each_index * 10:each_index * 10 + 10])
##        #print(puzzle)
##        new_list = new_list + puzzle
##    #print(new_list)
##    return new_list

#input_puzzle()

        
        
def forward(new_list, word):
    
    row = -1
    for each_sub in new_list:
        row = row + 1
        
        if each_sub.find(word) > -1:
            column = each_sub.find(word)
            
            return (row, column)
            

    return -1

def backward(new_list, word):
    
    column = 9
    row = -1
    for each_sub in new_list:
        row = row + 1
        list_back = []
        for each_character in each_sub:
            list_back.append(each_character)
        list_back.reverse()
        #print(list_back)
        string_back = ""
        for each_value in list_back:
            string_back = string_back + each_value
        #print(string_back)
        if string_back.find(word) > -1:
            x = string_back.find(word)
            column = column - x
            return (row, column)
    return -1 


def down(new_list, word):
    for each_index in range(10):
        #list_back = []
        string_down = ""
        for each_sub in new_list:
            string_down = string_down + each_sub[each_index]
        #print(string_down)
        #string_down provides us all_row[index] in a string
        if string_down.find(word) > -1:
            row = string_down.find(word)
            column = each_index
            return (row, column)
    return -1
 


def up(new_list, word):
    #print(new_list)
    for each_index in range(10):
        list_up= []
        #string_down = ""
        for each_sub in new_list:
            list_up.append(each_sub[each_index])
        list_up.reverse()
        #print(list_up)
        string_up = ""
        for value in list_up:
            string_up = string_up + value
        #print(string_up)
        if string_up.find(word) > -1:
            x = string_up.find(word)
            row = 9 - x
            column = each_index
            return (row, column)
    return -1
            

        
            
    
##def check_everything(new_list, word):
##    if forward(new_list, word) != -1:
##        x = forward(new_list, word)
##        print(word+":", "(FORWARD) row:", x[0], "column:", x[1])
##    elif backward(new_list, word) != -1:
##        y = backward(new_list, word)
##        print(word+":", "(BACKWARD) row:", y[0], "column:", y[1])
##            
##    elif up(new_list, word) != -1:
##        z = up(new_list, word)
##        print(word+":", "(UP) row:", z[0], "column:", z[1])
##    elif down(new_list, word) != -1:
##        m = down(new_list, word)
##        print(word+":", "(DOWN) row:", m[0], "column:", m[1])
##
##    else:
##        print(word + ":", "word not found")
##            


        
    
    
    
    
    
        
            
   

    
