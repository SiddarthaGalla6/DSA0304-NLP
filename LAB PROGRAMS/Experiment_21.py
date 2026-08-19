import re

sentence = input("Enter a sentence: ")
matches = re.findall(r"\b(?:the|a|an)\s+\w+", sentence, re.IGNORECASE)

print("Noun Phrases:")
for phrase in matches:
    print(phrase)

# Sample Input:
# Enter a sentence: The boy plays a game
#
# Sample Output:
# Noun Phrases:
# The boy
# a game
