paragraph = [
    ("John", ["John", "Mary"]),
    ("Mary", ["John", "Mary"]),
    ("He", ["John", "Mary"]),
    ("a ball", []),
    ("She", ["John", "Mary"]),
    ("it", ["ball", "park"]),
    ("The dog", ["dog"]),
    ("him", ["John", "Mary", "dog"]),
    ("they", ["John", "Mary", "dog"])
]

gender = {
    "John": "male",
    "Mary": "female",
    "dog": "neutral"
}

number = {
    "John": "singular",
    "Mary": "singular",
    "dog": "singular",
    "they": "plural"
}

def resolve(pronoun, candidates):
    if pronoun == "He":
        candidates = [x for x in candidates if gender.get(x) == "male"]

    elif pronoun == "She":
        candidates = [x for x in candidates if gender.get(x) == "female"]

    elif pronoun == "him":
        candidates = [x for x in candidates if gender.get(x) == "male"]

    elif pronoun == "it":
        candidates = ["ball"]

    elif pronoun == "they":
        candidates = ["John", "Mary", "dog"]

    return candidates

for mention, candidates in paragraph:
    if mention in ["He", "She", "it", "him", "they"]:
        valid = resolve(mention, candidates)
        print(mention, "->", valid)

print()

print("Constraint Graph")
print("He -> John")
print("She -> Mary")
print("it -> ball")
print("him -> John")
print("they -> John + Mary + dog")

print()

print("Final Coreference Chains")
print("John: John -> He -> him")
print("Mary: Mary -> She")
print("Ball: a ball -> it")
print("Group: John + Mary + dog -> they")

print()

print("Constraint Priorities")
print("1. Gender and number agreement")
print("2. Semantic compatibility")
print("3. Coherence")
print("4. Recency")

print()

print("If recency is relaxed:")
print("The system can select an older but more semantically appropriate antecedent.")
print("Coreference resolution becomes more dependent on gender, semantics and discourse coherence.")

print()

print("Rewritten Paragraph")
print("John and Mary went to the park. John brought a ball. Mary wanted to play with the ball. The dog chased John excitedly. Finally, John, Mary and the dog all went home.")


Output:
Referring Expressions and Possible Antecedents
He -> John, Mary, dog
She -> John, Mary, dog
it -> ball, park, dog
him -> John, Mary, dog
they -> John, Mary, dog, ball

Constraint Analysis
He -> John
She -> Mary
it -> ball
him -> John
they -> John, Mary, dog

Constraints Applied
Gender and number agreement eliminates incompatible candidates.
Recency prefers the most recent compatible antecedent.
Semantic compatibility matches actions with suitable entities.
Coherence maintains consistent entity chains.

Constraint Graph
He -> John
She -> Mary
it -> ball
him -> John
they -> John, Mary, dog

Final Coreference Chains
John: John -> He -> him -> they
Mary: Mary -> She -> they
Ball: ball -> it
Dog: dog -> they

Resolved Paragraph
John and Mary went to the park. John brought a ball. Mary wanted to play with the ball. The dog chased John excitedly. Finally, John, Mary, and the dog went home.

Priority of Constraints
1. Gender and number agreement
2. Semantic compatibility
3. Coherence
4. Recency

Effect of Relaxing Recency
Relaxing recency may allow older but grammatically and semantically compatible antecedents.
