sentence = input("Enter a sentence: ")
words = sentence.split()
tags = ["NN"] * len(words)
for i in range(len(words)):
    word = words[i].lower()
    if word.endswith("ing"):
        tags[i] = "VBG"
    elif word.endswith("ed"):
        tags[i] = "VBD"
    elif word.endswith("ly"):
        tags[i] = "RB"
print("POS Tags:")
for word, tag in zip(words, tags):
    print(word, "->", tag)


Input :
Enter a sentence: boy played happily

Output :
POS Tags:
boy -> NN
played -> VBD
happily -> RB
