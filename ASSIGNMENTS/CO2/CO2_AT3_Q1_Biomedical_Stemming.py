from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["infection","infectious","infected","infect","infective","infecting","infects"]
morph_types = {"infection":"Derivational (-ion)","infectious":"Derivational (-ious)","infected":"Inflectional (-ed)","infect":"Root","infective":"Derivational (-ive)","infecting":"Inflectional (-ing)","infects":"Inflectional (-s)"}
print("%-20s %-20s %-20s" % ("Word","Stem","Morphology Type"))
print("-" * 62)
for w in words:
    print("%-20s %-20s %-20s" % (w, ps.stem(w), morph_types[w]))
stems = [ps.stem(w) for w in words]
print("\nUnique stems : %s" % sorted(set(stems)))
print("Inconsistency: infection/infectious/infective all => same stem")
print("Root Cause   : Porter Stemmer strips derivational suffixes (-ion,-ious,-ive)")
print("Fix Required : Treat derivational morphemes separately from inflectional ones")


Output:
Word                 Stem                 Morphology Type
--------------------------------------------------------------
infection            infect               Derivational (-ion)
infectious           infecti              Derivational (-ious)
infected             infect               Inflectional (-ed)
infect               infect               Root
infective            infect               Derivational (-ive)
infecting            infect               Inflectional (-ing)
infects              infect               Inflectional (-s)

Unique stems : ['infect', 'infecti']
Inconsistency: infection/infectious/infective all => same stem
Root Cause   : Porter Stemmer strips derivational suffixes (-ion,-ious,-ive)
Fix Required : Treat derivational morphemes separately from inflectional ones
