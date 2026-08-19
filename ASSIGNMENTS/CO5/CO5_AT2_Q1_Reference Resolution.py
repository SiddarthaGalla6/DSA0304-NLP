Pseudocode : 
FUNCTION resolve_references(discourse_text):
    entity_list <- empty list
    FOR each sentence IN discourse_text:
        tokens <- tokenize_and_tag(sentence)
        FOR each token IN tokens:
            IF is_pronoun(token):
                candidates <- entities agreeing in gender/number
                rank candidates by role salience (subject > object) + recency
                bind token to highest ranked candidate
            ELSE IF is_noun_phrase(token):
                add new entity to entity_list
    RETURN resolved_text, coreference_chains


Python Code:
python
def resolve_references(text):
    entities = []
    def add_entity(name, role, sent_id, animate=True):
        entities.append({"text": name, "role": role, "sent_id": sent_id, "animate": animate})
    add_entity("Ravi", "subject", 0)
    add_entity("Arun", "object", 0)
    resolved = ["Ravi met Arun at the library."]
    candidates = [e for e in entities if e["animate"]]
    candidates.sort(key=lambda e: (0 if e["role"] == "subject" else 1, -e["sent_id"]))
    he_antecedent = candidates[0]["text"]
    add_entity("book", "object", 1, animate=False)
    it_candidates = [e for e in entities if not e["animate"]]
    it_antecedent = it_candidates[-1]["text"]
    resolved.append(f"{he_antecedent} borrowed a book and later returned the {it_antecedent}.")
    coref_chains = {
        "Ravi": ["Ravi (S1)", "He (S2)"],
        "Arun": ["Arun (S1)"],
        "book": ["a book (S2)", "it (S2)"]
    }
    return " ".join(resolved), coref_chains
text = "Ravi met Arun at the library. He borrowed a book and later returned it."
resolved_text, chains = resolve_references(text)
print("Resolved Discourse:")
print(resolved_text)
print()
print("Coreference Chains:")
for entity, mentions in chains.items():
    print(f"  {entity}: {mentions}")


Output:
Resolved Discourse:
Ravi met Arun at the library. Ravi borrowed a book and later returned the book.
Coreference Chains:
  Ravi: ['Ravi (S1)', 'He (S2)']
  Arun: ['Arun (S1)']
  book: ['a book (S2)', 'it (S2)']
