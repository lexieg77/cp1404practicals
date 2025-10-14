"""
Word Occurences
Estimate: 20 mins
Actual:
"""
word_to_count = {}

words = input("Please enter a string of words: ").split(" ")

for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1
    print(word_to_count[word])

# keys = words, values = counts





