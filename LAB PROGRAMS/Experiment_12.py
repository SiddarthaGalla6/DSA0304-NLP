import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'boy' | 'girl'
V -> 'sees' | 'likes'
""")
parser = EarleyChartParser(grammar)
sentence = input("Enter a sentence: ").lower().split()
trees = list(parser.parse(sentence))
if trees:
    print("Sentence Accepted")
    print(trees[0])
else:
    print("Sentence Rejected")


Output:
Enter a sentence: the boy sees a girl
Sentence Accepted
(S (NP (Det the) (N boy)) (VP (V sees) (NP (Det a) (N girl))))
