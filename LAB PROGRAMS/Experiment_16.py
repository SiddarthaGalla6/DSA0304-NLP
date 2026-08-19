import spacy

# Install model once if needed:
# python -m spacy download en_core_web_sm

nlp = spacy.load("en_core_web_sm")

text = input("Enter text: ")
doc = nlp(text)

print("Named Entities:")
for ent in doc.ents:
    print(ent.text, "->", ent.label_)

# Sample Input:
# Apple is in California.
#
# Sample Output:
# Named Entities:
# Apple -> ORG
# California -> GPE
