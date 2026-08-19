import re

text = input("Enter text: ")
sentences = re.split(r"(?<=[.!?])\s+", text)

previous = None

for sentence in sentences:
    words = sentence.split()
    for word in words:
        if word.lower() in ["he", "she", "they"]:
            if previous:
                print(word, "->", previous)
        elif word.lower() not in ["the", "a", "an"]:
            previous = word.strip(".,!?")

# Sample Input:
# Enter text: John went home. He was happy.
#
# Sample Output:
# He -> John
