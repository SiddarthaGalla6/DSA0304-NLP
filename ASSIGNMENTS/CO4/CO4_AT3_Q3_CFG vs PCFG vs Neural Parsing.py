print("AMBIGUITY HANDLING IN NLP PARSING")
sentence="She saw the man with a telescope"
interpretations=[
"She used a telescope to see the man.",
"The man had a telescope."
]
methods={
"CFG":"Generates multiple valid parse structures.",
"PCFG":"Assigns probabilities to different parse structures.",
"Neural Parser":"Uses learned contextual representations to select the most likely interpretation."
}
print("\nSentence:",sentence)
print("\nPossible Interpretations")
for i,item in enumerate(interpretations,1):
    print(i,item)
print("\nParsing Methods")
for method,description in methods.items():
    print(method,":",description)
print("\nComparison")
print("CFG handles grammatical ambiguity but does not rank interpretations.")
print("PCFG ranks parses using learned probabilities.")
print("Neural parsing uses contextual information and large training datasets.")
print("\nConclusion")
print("Neural parsing is generally most effective for real-world applications.")
print("PCFG is useful when probabilistic grammar interpretation is required.")

Output:
AMBIGUITY HANDLING IN NLP PARSING

Sentence: She saw the man with a telescope

Possible Interpretations
1 She used a telescope to see the man.
2 The man had a telescope.

Parsing Methods
CFG : Generates multiple valid parse structures.
PCFG : Assigns probabilities to different parse structures.
Neural Parser : Uses learned contextual representations to select the most likely interpretation.

Comparison
CFG handles grammatical ambiguity but does not rank interpretations.
PCFG ranks parses using learned probabilities.
Neural parsing uses contextual information and large training datasets.

Conclusion
Neural parsing is generally most effective for real-world applications.
PCFG is useful when probabilistic grammar interpretation is required.
