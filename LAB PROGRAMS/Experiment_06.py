import random
text = "I love python because python is easy to learn"
words = text.split()
bigrams = {}
for i in range(len(words) - 1):
    if words[i] not in bigrams:
        bigrams[words[i]] = []
    bigrams[words[i]].append(words[i + 1])
word = words[0]
result = [word]
for i in range(7):
    if word in bigrams:
        word = random.choice(bigrams[word])
        result.append(word)
    else:
        break
print("Generated Text:")
print(" ".join(result))


Output :
Generated Text:
I love python is easy to learn
