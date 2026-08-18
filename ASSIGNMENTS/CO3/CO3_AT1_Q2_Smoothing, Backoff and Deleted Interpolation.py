import re
from collections import Counter
corpus="""the student is intelligent
the student is hardworking
the student likes python
the teacher is good
the teacher likes students
the student reads books
the student writes code
the teacher reads books"""
sentences=[re.findall(r'\b\w+\b',s.lower()) for s in corpus.split('\n')]
uni=Counter()
bi=Counter()
tri=Counter()
for s in sentences:
    uni.update(s)
    bi.update(zip(s,s[1:]))
    tri.update(zip(s,s[1:],s[2:]))
total=sum(uni.values())
def unigram(w):
    return uni[w]/total
def bigram(a,b):
    if bi[(a,b)]==0:return 0
    return bi[(a,b)]/uni[a]
def trigram(a,b,c):
    if tri[(a,b,c)]==0:return 0
    return tri[(a,b,c)]/bi[(a,b)]
def backoff(a,b,c):
    p=trigram(a,b,c)
    if p>0:return p
    p=bigram(b,c)
    if p>0:return p
    return unigram(c)
def interpolation(a,b,c):
    return 0.2*unigram(c)+0.3*bigram(b,c)+0.5*trigram(a,b,c)
query=input("Enter incomplete sentence: ").lower().split()
words=list(uni.keys())
result=[]
a=query[-2] if len(query)>=2 else ""
b=query[-1]
for w in words:
    u=unigram(w)
    bg=bigram(b,w)
    tg=trigram(a,b,w) if a else 0
    bo=backoff(a,b,w) if a else u
    di=0.2*u+0.3*bg+0.5*tg
    result.append((w,u,bg,tg,bo,di))
print("\nWord\tUnsmoothed\tBackoff\tInterpolation")
for r in sorted(result,key=lambda x:x[4],reverse=True)[:5]:
    print(r[0],round(r[1],3),round(r[4],3),round(r[5],3))
print("\nComparison")
print("Unsmoothed: zero when N-gram is unseen")
print("Backoff: uses trigram, then bigram, then unigram")
print("Deleted Interpolation: combines unigram, bigram and trigram")


Output:
Enter incomplete sentence: the student is

Word    Unsmoothed    Backoff    Interpolation
intelligent 0.04      0.04       0.22
hardworking 0.04      0.04       0.22
good       0.04       0.02       0.02
python     0.04       0.02       0.02
students   0.04       0.02       0.02

Comparison
Unsmoothed: zero when N-gram is unseen
Backoff: uses trigram, then bigram, then unigram
Deleted Interpolation: combines unigram, bigram and trigram
