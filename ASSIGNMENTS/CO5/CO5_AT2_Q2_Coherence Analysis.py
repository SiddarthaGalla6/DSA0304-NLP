Pseudocode :
CUE_TABLE <- {'therefore': CAUSE_EFFECT, 'because': CAUSE_EFFECT, 'however': CONTRAST, 'then': SEQUENCE}
FUNCTION analyse_coherence(sentences):
    FOR i FROM 1 TO length(sentences)-1:
        cue <- find_cue_phrase(sentences[i])
        IF cue found: relation <- CUE_TABLE[cue]
        ELSE: relation <- infer_implicit_relation(sentences[i-1], sentences[i])
        relations.append((i-1, i, relation))
    RETURN relations, coherence_score


Python Code:
python
CUE_TABLE = {
    "therefore": "CAUSE_EFFECT",
    "because": "CAUSE_EFFECT",
    "however": "CONTRAST",
    "then": "SEQUENCE"
}
def find_cue(sentence):
    low = sentence.lower()
    for cue in CUE_TABLE:
        if cue in low:
            return cue
    return None
def infer_implicit(prev, curr):
    return "ELABORATION"
def analyse_coherence(sentences):
    relations = []
    for i in range(1, len(sentences)):
        cue = find_cue(sentences[i])
        relation = CUE_TABLE[cue] if cue else infer_implicit(sentences[i - 1], sentences[i])
        relations.append((f"S{i}", f"S{i+1}", relation))
    return relations
sentences = [
    "The roads were flooded after heavy rainfall",
    "Therefore, schools were closed for the day",
    "Students attended classes online"
]
relations = analyse_coherence(sentences)
print("Discourse Relations:")
for left, right, rel in relations:
    print(f"  {left} -> {right} : {rel}")
connected = len(relations) == len(sentences) - 1
score = 1.0 if connected else 0.5
print(f"\nCoherence Score: {score}  (fully connected: {connected})")


Output:
Discourse Relations:
  S1 -> S2 : CAUSE_EFFECT
  S2 -> S3 : ELABORATION
Coherence Score: 1.0  (fully connected: True)
