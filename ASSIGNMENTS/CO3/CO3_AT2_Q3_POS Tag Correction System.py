import math
print("CASE STUDY 3: News Analytics and POS Tag Correction System")
words=["economic","growth","increases","employment"]
tags=["JJ","NN","NNS","NN"]
print("\n1. Initial POS Tags")
print(list(zip(words,tags)))
if tags[2]=="NNS" and tags[1]=="NN":
    tags[2]="VBZ"
print("After Transformation")
print(list(zip(words,tags)))
print("Correction: increases becomes VBZ because it is the main verb after the noun growth.")
freq={"economic":120,"growth":450,"increases":210,"employment":380}
total=sum(freq.values())
print("\n3. Word Frequency Distribution")
for w,c in freq.items():
    print(w,c,round(c/total,3))
print("Total frequency =",total)
print("Frequency information helps probabilistic taggers select likely word and tag combinations.")
print("\n4. Transformation-Based Tagging")
print("Initial tagging may contain errors.")
print("Transformation rules correct tags using contextual information.")
print("Entropy can measure uncertainty before and after correction.")
p_before=[0.5,0.5]
p_after=[0.9,0.1]
h_before=-(p_before[0]*math.log2(p_before[0])+p_before[1]*math.log2(p_before[1]))
h_after=-(p_after[0]*math.log2(p_after[0])+p_after[1]*math.log2(p_after[1]))
print("Entropy before transformation =",round(h_before,3),"bits")
print("Entropy after transformation =",round(h_after,3),"bits")
print("Lower entropy after transformation indicates greater tagging confidence.")


Output:
CASE STUDY 3: News Analytics and POS Tag Correction System

1. Initial POS Tags
[('economic', 'JJ'), ('growth', 'NN'), ('increases', 'NNS'), ('employment', 'NN')]
After Transformation
[('economic', 'JJ'), ('growth', 'NN'), ('increases', 'VBZ'), ('employment', 'NN')]
Correction: increases becomes VBZ because it is the main verb after the noun growth.

3. Word Frequency Distribution
economic 120 0.103
growth 450 0.388
increases 210 0.181
employment 380 0.328
Total frequency = 1160
Frequency information helps probabilistic taggers select likely word and tag combinations.

4. Transformation-Based Tagging
Initial tagging may contain errors.
Transformation rules correct tags using contextual information.
Entropy can measure uncertainty before and after correction.
Entropy before transformation = 1.0 bits
Entropy after transformation = 0.469 bits
Lower entropy after transformation indicates greater tagging confidence.
