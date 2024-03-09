class Anagram:
    def __init__(self,word) -> None:
        self.word = word
    
    
    def match(self,anagrams):
        """returns all matches in a list"""
        matches = []  #initialize an empty list to store matching  anagrams
        sorted_word = sorted(self.word) #use sorted function to sort the original word
        for anagram in anagrams:  #iterate over each word in list 
            #check if sorted anagram is same as sorted original word and ensure anagram isn't the same as original word to avoid duplicates
            if sorted(anagram) == sorted_word and anagram != self.word:
                matches.append(anagram) #anagram is appended to list of matches

        return matches        


listen = Anagram("listen")
result = listen.match(['enlist', 'google', 'inlets', 'banana'])        
print(result)
        

        
