import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
text = input("Enter a sentence: ")
words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)
print("POS Tags:")
for word, tag in tags:
    print(word, "->", tag)


Input :
Enter a sentence: The boy is playing cricket

Output:
POS Tags:
The -> DT
boy -> NN
is -> VBZ
playing -> VBG
cricket -> NN
