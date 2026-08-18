import re
from collections import Counter
lexicon={"the":"DT","a":"DT","an":"DT","student":"NN","teacher":"NN","book":"NN","books":"NNS","python":"NNP","code":"NN","he":"PRP","she":"PRP","they":"PRP","is":"VBZ","are":"VBP","am":"VBP","was":"VBD","likes":"VBZ","reads":"VBZ","writes":"VBZ","like":"VB","read":"VB","write":"VB","good":"JJ","intelligent":"JJ","hardworking":"JJ","quickly":"RB","in":"IN","on":"IN","to":"TO","and":"CC","but":"CC","very":"RB"}
train=[("the","DT"),("student","NN"),("is","VBZ"),("good","JJ"),("the","DT"),("teacher","NN"),("reads","VBZ"),("books","NNS"),("he","PRP"),("likes","VBZ"),("python","NNP"),("she","PRP"),("writes","VBZ"),("code","NN")]
wordtag=Counter(train)
trans=Counter()
for i in range(1,len(train)):
    trans[(train[i-1][1],train[i][1])]+=1
def rule_tag(words):
    tags=[]
    for i,w in enumerate(words):
        if w in lexicon:
            t=lexicon[w]
        elif w.endswith("ly"):
            t="RB"
        elif w.endswith("ing"):
            t="VBG"
        elif w.endswith("ed"):
            t="VBD"
        elif w.endswith("ous") or w.endswith("ful") or w.endswith("ive"):
            t="JJ"
        elif w.endswith("s"):
            t="NNS"
        else:
            t="NN"
        tags.append(t)
    return tags
def stochastic_tag(words):
    result=[]
    for w in words:
        choices=[t for x,t in train if x==w]
        if choices:
            result.append(Counter(choices).most_common(1)[0][0])
        else:
            result.append("NN")
    return result
def transform(words,tags):
    tags=tags[:]
    for i,w in enumerate(words):
        if i>0 and tags[i]=="NN" and tags[i-1] in ["PRP","VBZ","VBP","VB","VBD"]:
            tags[i]="VB"
        if i>0 and tags[i]=="NN" and tags[i-1]=="DT":
            tags[i]="NN"
    return tags
sentence=input("Enter sentence: ").lower()
words=re.findall(r'\b\w+\b',sentence)
r=rule_tag(words)
s=stochastic_tag(words)
t=transform(words,s)
print("\nRule-Based:")
print(list(zip(words,r)))
print("\nStochastic:")
print(list(zip(words,s)))
print("\nTransformation-Based:")
print(list(zip(words,t)))
print("\nTagset: Penn Treebank")
print("NN=Noun NNS=Plural NNP=Proper Noun")
print("VB=Verb VBZ=Verb JJ=Adjective RB=Adverb")
print("PRP=Pronoun DT=Determiner IN=Preposition CC=Conjunction")


Output:
Enter sentence: the student reads books

Rule-Based:
[('the', 'DT'), ('student', 'NN'), ('reads', 'VBZ'), ('books', 'NNS')]

Stochastic:
[('the', 'DT'), ('student', 'NN'), ('reads', 'VBZ'), ('books', 'NNS')]

Transformation-Based:
[('the', 'DT'), ('student', 'NN'), ('reads', 'VBZ'), ('books', 'NNS')]

Tagset: Penn Treebank
NN=Noun NNS=Plural NNP=Proper Noun
VB=Verb VBZ=Verb JJ=Adjective RB=Adverb
PRP=Pronoun DT=Determiner IN=Preposition CC=Conjunction
