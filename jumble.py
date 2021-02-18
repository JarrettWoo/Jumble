from english_words import english_words_lower_alpha_set as words
from itertools import permutations

jumble_word = input("Enter jumbled word: ")

possible_words = list(map("".join, permutations(jumble_word)))

for i in possible_words:
    if i.lower() in words:
        print(i.lower())
