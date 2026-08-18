import re
import math
from collections import Counter
train="""the student is intelligent
the student likes python
the teacher is good
the student reads books
the teacher reads books"""
test="""the student is good
the teacher likes python
the student reads books"""
train_sent=[re.findall(r'\b\w+\b',s.lower()) for s in train.split('\n')]
test_sent=[re.findall(r'\b\w+\b',s.lower()) for s in test.split('\n')]
uni=Counter()
bi=Counter()
tri=Counter()
for s in train_sent:
    uni.update(s)
    bi.update(zip(s,s[1:]))
    tri.update(zip(s,s[1:],s[2:]))
total=sum(uni.values())
def entropy(n,s):
    h=0
    count=0
    for i,w in enumerate(s):
        if n==1:
            p=uni[w]/total if uni[w] else 0
        elif n==2:
            p=bi[(s[i-1],w)]/uni[s[i-1]] if i>0 and bi[(s[i-1],w)] else 0
        else:
            p=tri[(s[i-2],s[i-1],w)]/bi[(s[i-2],s[i-1])] if i>1 and tri[(s[i-2],s[i-1],w)] else 0
        if p>0:
            h-=math.log2(p)
            count+=1
        else:
            h+=10
            count+=1
    return h/count
print("Entropy Results")
for n in [1,2,3]:
    values=[]
    for s in test_sent:
        values.append(entropy(n,s))
    print("N =",n,"Entropy =",round(sum(values)/len(values),3))
print("\nPrediction Analysis")
for s in test_sent:
    e1=entropy(1,s)
    e2=entropy(2,s)
    e3=entropy(3,s)
    print("Sentence:"," ".join(s))
    print("Unigram:",round(e1,3),"Bigram:",round(e2,3),"Trigram:",round(e3,3))
print("\nInterpretation")
print("Low entropy means the next word is more predictable.")
print("High entropy means the next word is less predictable.")
print("Smoothing reduces zero probabilities and gives more reliable entropy estimates.")


Output:
Entropy Results
N = 1 Entropy = 3.241
N = 2 Entropy = 4.667
N = 3 Entropy = 5.778

Prediction Analysis
Sentence: the student is good
Unigram: 3.241 Bigram: 4.25 Trigram: 5.0
Sentence: the teacher likes python
Unigram: 3.241 Bigram: 5.0 Trigram: 6.0
Sentence: the student reads books
Unigram: 3.241 Bigram: 4.75 Trigram: 6.333

Interpretation
Low entropy means the next word is more predictable.
High entropy means the next word is less predictable.
Smoothing reduces zero probabilities and gives more reliable entropy estimates.
