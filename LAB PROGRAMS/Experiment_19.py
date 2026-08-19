from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
import nltk
nltk.download("wordnet")
sentence = input("Enter sentence: ").split()
word = input("Enter ambiguous word: ")
sense = lesk(sentence, word)
if sense:
    print("Selected Sense:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No sense found.")


Input:
Enter sentence: I went to the bank to deposit money
Enter ambiguous word: bank

Output:
Selected Sense: bank.n.09
Definition: a container for holding papers and money
