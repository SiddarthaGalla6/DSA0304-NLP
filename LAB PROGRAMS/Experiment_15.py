import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser
grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [1.0]
VP -> V NP [1.0]
Det -> 'the' [0.5] | 'a' [0.5]
N -> 'boy' [0.5] | 'girl' [0.5]
V -> 'sees' [0.5] | 'likes' [0.5]
""")
parser = ViterbiParser(grammar)
sentence = input("Enter a sentence: ").lower().split()
try:
    tree = next(parser.parse(sentence))
    print("Most Probable Parse:")
    print(tree)
except StopIteration:
    print("Sentence cannot be parsed.")


Output:
Enter a sentence: the boy sees a girl
Most Probable Parse:
(S (NP (Det the) (N boy)) (VP (V sees) (NP (Det a) (N girl))))
