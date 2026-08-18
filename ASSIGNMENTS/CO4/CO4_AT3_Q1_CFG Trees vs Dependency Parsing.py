print("CFG TREES VS DEPENDENCY PARSING")
sentence="The student reads a book"
cfg_structure={
"Sentence":"S",
"Subject":"The student",
"Verb":"reads",
"Object":"a book"
}
dependency_structure=[
("student","subject","reads"),
("reads","root","reads"),
("book","object","reads"),
("The","determiner","student"),
("a","determiner","book")
]
print("\nSentence:",sentence)
print("\nCFG Representation")
for key,value in cfg_structure.items():
    print(key,":",value)
print("\nDependency Representation")
for word,relation,head in dependency_structure:
    print(word,"->",relation,"->",head)
print("\nComparison")
print("CFG represents hierarchical phrase structure.")
print("Dependency parsing represents direct relationships between words.")
print("CFG is useful for grammar and syntactic structure.")
print("Dependency parsing directly captures word-to-word relationships.")
print("\nConclusion")
print("Dependency parsing is more effective for capturing relationships between words.")

Output:
CFG TREES VS DEPENDENCY PARSING

Sentence: The student reads a book

CFG Representation
Sentence : S
Subject : The student
Verb : reads
Object : a book

Dependency Representation
student -> subject -> reads
reads -> root -> reads
book -> object -> reads
The -> determiner -> student
a -> determiner -> book

Comparison
CFG represents hierarchical phrase structure.
Dependency parsing represents direct relationships between words.
CFG is useful for grammar and syntactic structure.
Dependency parsing directly captures word-to-word relationships.

Conclusion
Dependency parsing is more effective for capturing relationships between words.
