Pseudocode:
FUNCTION generate_sentence(frame):
    subject_np <- 'the ' + lexicalize(frame.Agent)
    object_np  <- 'a '   + lexicalize(frame.Object)
    verb <- inflect(lexicalize(frame.Action), frame.Tense)
    RETURN capitalise(subject_np) + verb + object_np


Python Code:
python
IRREGULAR_VERBS = {"buy": "bought", "go": "went", "eat": "ate"}
def inflect(verb, tense):
    if tense == "Past":
        return IRREGULAR_VERBS.get(verb, verb + "ed")
    elif tense == "Present":
        return verb + "s"
    return verb
def generate_sentence(frame):
    subject_np = "The " + frame["Agent"].lower()
    object_np = "a " + frame["Object"].lower()
    verb = inflect(frame["Action"].lower(), frame["Tense"])
    return f"{subject_np} {verb} {object_np}."
frame = {"Action": "Buy", "Agent": "Student", "Object": "Book", "Tense": "Past"}
sentence = generate_sentence(frame)
print("Semantic Frame:", frame)
print("\nGenerated Sentence:")
print(" ", sentence)


Output:
Semantic Frame: {'Action': 'Buy', 'Agent': 'Student', 'Object': 'Book', 'Tense': 'Past'}
Generated Sentence:
  The student bought a book.
