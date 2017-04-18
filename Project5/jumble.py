#Project 5
#Name: Trina Haque
#Jumble word

def solve_jumble(dictionary):
    word_input = input("Please enter a jumbled word: ")
    s = word_input.lower()
    ans = anagrams(s)
    ans = list(set(ans))
    list_of_words = search_dict(dictionary)
    matched_word = []
    
    for each_combo in ans:
        for each_word in list_of_words:
            if each_combo == each_word:
                matched_word.append(each_combo)
   
    result_length = len(matched_word)
    
    if result_length == 1:
        print("Your word is", matched_word[0]+".")
    elif result_length > 1:
        print("Your words are:")
        for each_index in range(len(matched_word)):
            print(matched_word[each_index])
    else:
        print("Your word cannot be unjumbled.")
            
           

        
        
        
     
def anagrams(s):
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
        #print(len(ans))
        return ans


def search_dict(dictionary):
    words = open(dictionary, 'r')
    words = words.read()
    list_of_words = words.split()
    return list_of_words
   
 
     
def main():
    
    solve_jumble('words.txt')


if __name__ == "__main__":
    main()
