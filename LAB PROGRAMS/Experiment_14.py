import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V
Det -> 'the' | 'a'
N -> 'boy' | 'girl'
V -> 'runs' | 'walks'
""")

parser = ChartParser(grammar)
sentence = input("Enter a sentence: ").lower().split()

if list(parser.parse(sentence)):
    print("Sentence follows the grammar. Agreement is valid.")
else:
    print("Agreement is invalid.")

# Sample Output:
# Enter a sentence: the boy runs
# Sentence follows the grammar. Agreement is valid.
