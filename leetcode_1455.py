class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        
        for i,val in enumerate(sentence):
            if searchWord in val[:len(searchWord)]:
                return i+1
        return -1

        
