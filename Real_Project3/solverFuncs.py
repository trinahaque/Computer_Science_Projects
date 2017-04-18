#Project3
# Trina Haque
#Check validity



def check_cages_valid(cages, grid):


   for each_list in cages:
      new_var = 0
      partial = False
      for each_numb in range(2, len(each_list)):
         #ignore the first two index
         numb_list = each_list[each_numb]
         #numb_list gives me the number in list_list that is the index of grid
         new_var = new_var + grid[numb_list]
         #adds up the values of that cell
         if grid[numb_list] == 0:
            partial = True
      if partial == False and each_list[0] != new_var:
         return False
      elif partial == True and each_list[0] <= new_var:
         return False
      #positions of the if statement inside the for loop is very important

   return True
      

         

      
def check_rows_valid(grid):

       
    for each_row in range(5):
       #gives row from 0 through 4
      new_list = []
      for i in range(each_row*5, each_row*5+5):
         var = grid[i]
         new_list.append(var)
         #gives me a list of 5, 6, 7, 8, 9
      for index in range(len(new_list)):
         if new_list.count(new_list[index]) > 1 and new_list[index] != 0:
            return False
    return True
##            elif new_list[index] == 0:
##               return False
                



def check_columns_valid(grid):

   
    for each_col in range(5):
      new_list = []
      for i in range(each_col, 4*5+1+each_col, 5):
         #5 at the end gives every 5 cell in the grid
         var = grid[i]
         new_list.append(var)
             
      for index in range(len(new_list)):
         if new_list.count(new_list[index]) > 1 and new_list[index] != 0:
            return False
    return True
##            elif new_list[index] == 0:
##               return False
          

def check_valid(cages, grid):
   if check_rows_valid(grid) == True and check_columns_valid(grid) == True and check_cages_valid(cages, grid) == True:
      return True
   else:
      return False
   #else is a faster way of checking than elif
 
  

