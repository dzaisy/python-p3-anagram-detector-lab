# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, list):
        matches = []
        for candidate in list:
            if self.anagram(candidate): # check if the candidate word is an anagram of self.word
                matches.append(candidate)
        return matches
    
    def anagram(self, candidate):
        return sorted(self.word.lower()) == sorted(candidate.lower()) # check if sorted letters of self.word and the candidate word are equal