import spacy
nlp = spacy.load("en_core_web_sm")
text = input("Enter text: ")
doc = nlp(text)
print("Named Entities:")
for ent in doc.ents:
    print(ent.text, "->", ent.label_)


Input:
Apple is in California.

Output:
Named Entities:
Apple -> ORG
California -> GPE
