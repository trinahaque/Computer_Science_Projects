#Project 3
#Trina Haque
#This is programs solves a puzzle that is kind of like sudoko. But it also takes cages and sum. After that, it solves it

import math
from solverFuncs import *

def get_cages():
    #cage_num = 0
    cages_number = eval(input("Number of cages: "))
    cages = []


    for each_line in range(cages_number):
      #cage_num = cage_num + 1
      sequence = input("Cage number %s: " % each_line).split()
      #adds cage line number to the input
      
      new_list = []

      for number in sequence:
        new_number = int(number)
        new_list.append(new_number)
      cages.append(new_list)

    
    return cages




def solve_chudoko():
    cages = get_cages()
    grid = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    index = 0
 
    
    #for index in range(len(grid) + 1):
    while index >= 0 and index < 25:
        #need > 0. otherwise index becomes negative
        grid[index] = grid[index] + 1
        
        if check_valid(cages, grid) == True:
             index = index + 1
             continue
        else:
             if check_valid(cages, grid) == False and grid[index] < 5:
                 continue
                 
             elif check_valid(cages, grid) == False and grid[index]  >= 5:
                grid[index] = 0
                index = index - 1
                
             #elif check_valid(cages, grid) == True:
                #index = index + 1
                #this statement doesn't really do anything
   
##    #for i in range(len(grid)):
##    print_sol = *grid, sep= ' '
##    for the_numb in print_sol:
##    print(the_numb, "")
    #*grid, sep = '' gives numbers in the list without the bracket and comma, but no space
##    sol_format = *grid, end= " "
##    for i in range(len(sol_format)):
##        print(i)
##        if i % 5 == 0:
##            print("\n")
    print("")
    print("Solution:")
    print(grid[0], grid[1], grid[2], grid[3], grid[4])
    print(grid[5], grid[6], grid[7], grid[8], grid[9])
    print(grid[10], grid[11], grid[12], grid[13], grid[14])
    print(grid[15], grid[16], grid[17], grid[18], grid[19])
    print(grid[20], grid[21], grid[22], grid[23], grid[24])
    
    
    #print(*grid, end= " ")
    #line_one = str(grid)
    #line_two = line_one.replace(','
    #print(line_one)
            
    

           

def main():
    
    solve_chudoko()


if __name__ == "__main__":
    main()
