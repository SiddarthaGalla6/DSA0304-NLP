from collections import defaultdict, Counter
training_data = [
    ("I", "PRP"),
    ("play", "VB"),
    ("cricket", "NN"),
    ("I", "PRP"),
    ("play", "VB"),
    ("games", "NN"),
    ("play", "NN")
]
counts = defaultdict(Counter)
for word, tag in training_data:
    counts[word][tag] += 1
sentence = input("Enter a sentence: ").split()
for word in sentence:
    if word in counts:
        tag = counts[word].most_common(1)[0][0]
    else:
        tag = "NN"
    print(word, "->", tag)


Input :
Enter a sentence: I play cricket

Output :
I -> PRP
play -> VB
cricket -> NN
