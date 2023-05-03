# your code goes here!

import ipdb

class Anagram:
    def __init__(self, word = 'test'):
        self.word = word
        pass

    def get_word(self):
        return self._word
    
    def set_word(self, word):
        self._word = word
    
    word = property(get_word, set_word)

    def match(self, list):
        anagrams = []
        for list_word in list:

            if(len(list_word) != len(self._word)):
                continue

            matched_indices = []
            for char in list_word:
                for word_index, word_char in enumerate(self._word):
                    if word_char == char and word_index not in matched_indices:
                        matched_indices.append(word_index)

            if len(matched_indices) == len(self._word):
                anagrams.append(list_word)

        return anagrams
