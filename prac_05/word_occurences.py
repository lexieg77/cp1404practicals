"""
Word Occurences
Estimate: 20 mins
Actual: 28 mins
"""
word_to_count = {}

words = input("Please enter a string of words: ").split(" ")

for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

max_length = max(len(word) for word in words)
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")






