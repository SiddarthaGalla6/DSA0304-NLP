import nltk
from nltk import CFG
from nltk.parse import ChartParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'boy' | 'girl'
V -> 'sees' | 'likes'
""")
parser = ChartParser(grammar)
sentence = input("Enter a sentence: ").lower().split()
trees = list(parser.parse(sentence))
if trees:
    print("Parse Tree:")
    print(trees[0])
else:
    print("No parse tree found")


Output:
Enter a sentence: the boy sees a girl
Parse Tree:
(S (NP (Det the) (N boy)) (VP (V sees) (NP (Det a) (N girl))))
