from nltk.corpus import wordnet as wn
import nltk

nltk.download("wordnet")

word = input("Enter a word: ")
synsets = wn.synsets(word)

if synsets:
    for syn in synsets[:3]:
        print("Synset:", syn.name())
        print("Definition:", syn.definition())
else:
    print("No synsets found.")

# Sample Input:
# Enter a word: bank
#
# Sample Output:
# Synset: bank.n.01
# Definition: sloping land (especially the slope beside a body of water)
