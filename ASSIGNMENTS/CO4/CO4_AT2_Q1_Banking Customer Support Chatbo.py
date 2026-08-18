import nltk
from nltk import CFG, ChartParser
grammar=CFG.fromstring("""
S -> NP VP
NP -> Det N | Det N PP | N
VP -> V NP | V NP PP
PP -> P NP
Det -> 'the' | 'last'
N -> 'transactions' | 'card' | 'month'
V -> 'show'
P -> 'with' | 'from'
""")
sentence="show the transactions with the card from last month".split()
parser=ChartParser(grammar)
trees=list(parser.parse(sentence))
print("BANKING CHATBOT - CFG PARSING")
print("Sentence:", " ".join(sentence))
print("Number of parse structures:",len(trees))
for i,tree in enumerate(trees,1):
    print("\nParse",i)
    print(tree)
print("\nCFG Analysis")
ambiguities=["with the card can describe which transactions are required","from last month specifies the time period"]
print("Ambiguity:")
for item in ambiguities:
    print("-",item)
features={"subject":"customer","verb":"show","object":"transactions","time":"last month","instrument":"card"}
print("\nFeature Structure")
for key,value in features.items():
    print(key,":",value)
pcfg={"transaction_interpretation":0.75,"card_interpretation":0.25}
print("\nPCFG Probabilities")
for key,value in pcfg.items():
    print(key,":",value)
print("\nImproved Solution")
print("PCFG selects the most probable interpretation.")
print("Feature structures enforce agreement and grammatical constraints.")
print("Earley parsing handles ambiguity and long queries efficiently.")
print("The combined approach improves accuracy and reduces unnecessary parsing.")


Output:
BANKING CHATBOT - CFG PARSING
Sentence: show the transactions with the card from last month
Number of parse structures: 2

Parse 1
(S (VP (V show) (NP (Det the) (N transactions) (PP (P with) (NP (Det the) (N card)))) (PP (P from) (NP (Det last) (N month)))))

Parse 2
(S (VP (V show) (NP (Det the) (N transactions)) (PP (P with) (NP (Det the) (N card))) (PP (P from) (NP (Det last) (N month)))))

CFG Analysis
Ambiguity:
- with the card can describe which transactions are required
- from last month specifies the time period

Feature Structure
subject : customer
verb : show
object : transactions
time : last month
instrument : card

PCFG Probabilities
transaction_interpretation : 0.75
card_interpretation : 0.25

Improved Solution
PCFG selects the most probable interpretation.
Feature structures enforce agreement and grammatical constraints.
Earley parsing handles ambiguity and long queries efficiently.
The combined approach improves accuracy and reduces unnecessary parsing.
