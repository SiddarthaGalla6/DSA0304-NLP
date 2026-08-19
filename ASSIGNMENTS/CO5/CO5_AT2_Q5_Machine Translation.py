Pseudocode:
FUNCTION translate(source_sentence):
    interlingua <- extract_semantic_frame(source_sentence)
    candidates <- generate_target_candidates(interlingua)
    FOR each candidate: score <- combine(translation_model_score, language_model_score)
    RETURN candidate with max score


Python Code:
python
def analyse(sentence):
    return {"predicate": "PLAY", "agent": "BOY", "object": "FOOTBALL", "aspect": "PROGRESSIVE"}
def generate_candidates(interlingua):
    return [
        "Le garcon joue au football.",
        "Le garcon est en train de jouer au football."
    ]
def score(candidate):
    length_penalty = len(candidate.split())
    return round(1.0 - 0.02 * length_penalty, 2)
def translate(sentence):
    interlingua = analyse(sentence)
    candidates = generate_candidates(interlingua)
    scored = [(c, score(c)) for c in candidates]
    best = max(scored, key=lambda x: x[1])
    return interlingua, scored, best
source = "The boy is playing football."
interlingua, scored, best = translate(source)
print("Interlingua Frame:")
print(" ", interlingua)
print("\nCandidates & Scores:")
for c, s in scored:
    print(f"  {c!r:50} score = {s}")
print("\nFinal Translation:")
print(" ", best[0])


Output

Interlingua Frame:
  {'predicate': 'PLAY', 'agent': 'BOY', 'object': 'FOOTBALL', 'aspect': 'PROGRESSIVE'}
Candidates & Scores:
  'Le garcon joue au football.'                      score = 0.9
  'Le garcon est en train de jouer au football.'     score = 0.82
Final Translation:
  Le garcon joue au football.
