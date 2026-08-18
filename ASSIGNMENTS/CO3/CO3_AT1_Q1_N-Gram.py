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
n=int(input("Enter N (1,2,3): "))
print("\nWord Counts and Probabilities")
if n==1:
    total=sum(uni.values())
    for w,c in uni.items():
        print(w,c,round(c/total,3))
elif n==2:
    for k,c in bi.items():
        p=c/uni[k[0]]
        print(k,c,round(p,3))
else:
    for k,c in tri.items():
        p=c/bi[k[:2]]
        print(k,c,round(p,3))
query=input("\nEnter incomplete sentence: ").lower().split()
pred={}
if n==1:
    total=sum(uni.values())
    for w,c in uni.items():
        pred[w]=c/total
elif n==2:
    last=query[-1]
    for (a,b),c in bi.items():
        if a==last:
            pred[b]=c/uni[a]
else:
    last=tuple(query[-2:])
    for (a,b,c),v in tri.items():
        if (a,b)==last:
            pred[c]=v/bi[(a,b)]
print("\nTop 5 Predictions")
for w,p in sorted(pred.items(),key=lambda x:x[1],reverse=True)[:5]:
    print(w,round(p,3))
print("\nUnseen N-gram probability = 0")


Output:
Enter N (1,2,3): 3

Word Counts and Probabilities
('the', 'student', 'is') 2 1.0
('student', 'is', 'intelligent') 1 0.5
('student', 'is', 'hardworking') 1 0.5
('student', 'likes', 'python') 1 1.0
('the', 'teacher', 'is') 1 1.0
('teacher', 'is', 'good') 1 1.0
('teacher', 'likes', 'students') 1 1.0
('student', 'reads', 'books') 1 1.0
('student', 'writes', 'code') 1 1.0

Enter incomplete sentence: the student is
Top 5 Predictions
intelligent 0.5
hardworking 0.5
Unseen N-gram probability = 0
