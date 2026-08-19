sentence = "The bank by the river flooded after the storm, but it was saved by quick action."

print("Source Sentence")
print(sentence)

print("\nWord Sense Disambiguation")
print("Ambiguous word: bank")
print("Selected sense: riverbank")
print("Reason: The phrase 'by the river' indicates a geographical riverbank.")
print("The verb 'flooded' is semantically compatible with a riverbank.")

print("\nPredicate Logic Representation")
print("bank(x)")
print("river(y)")
print("location(x, y)")
print("flood(x)")
print("storm(z)")
print("after(flood(x), storm(z))")
print("saved(x)")
print("quick_action(w)")
print("caused(w, saved(x))")

print("\nDiscourse Structure")
print("Clause 1: The riverbank flooded after the storm.")
print("Clause 2: The riverbank was saved by quick action.")
print("Relation: Contrast")

print("\nRST-Style Discourse Tree")
print("                 Contrast")
print("                /        \\")
print("               /          \\")
print("      Clause 1              Clause 2")
print(" Riverbank flooded      Riverbank saved")
print(" after the storm        by quick action")

print("\nTarget Sentence")
print("The riverbank near the river flooded after the storm, but quick action saved it.")

print("\nConstraint Verification")
print("Word sense: riverbank")
print("All important entities preserved: bank, river, storm, quick action")
print("Flooding and saving relations preserved.")
print("Contrast relation preserved.")
print("Sentence remains coherent.")

print("\nAdvantage of Constraint-Based Approach")
print("It uses grammatical, semantic, and contextual constraints together.")
print("It avoids selecting the financial meaning of bank.")
print("It preserves important relations and discourse structure.")
print("Pure statistical translation may choose an incorrect sense when context is ambiguous.")


Output:
Source Sentence
The bank by the river flooded after the storm, but it was saved by quick action.

Word Sense Disambiguation
Ambiguous word: bank
Selected sense: riverbank
Reason: The phrase 'by the river' indicates a geographical riverbank.
The verb 'flooded' is semantically compatible with a riverbank.

Predicate Logic Representation
bank(x)
river(y)
location(x, y)
flood(x)
storm(z)
after(flood(x), storm(z))
saved(x)
quick_action(w)
caused(w, saved(x))

Discourse Structure
Clause 1: The riverbank flooded after the storm.
Clause 2: The riverbank was saved by quick action.
Relation: Contrast

RST-Style Discourse Tree
                 Contrast
                /        \
               /          \
      Clause 1              Clause 2
 Riverbank flooded      Riverbank saved
 after the storm        by quick action

Target Sentence
The riverbank near the river flooded after the storm, but quick action saved it.

Constraint Verification
Word sense: riverbank
All important entities preserved: bank, river, storm, quick action
Flooding and saving relations preserved.
Contrast relation preserved.
Sentence remains coherent.

Advantage of Constraint-Based Approach
It uses grammatical, semantic, and contextual constraints together.
It avoids selecting the financial meaning of bank.
It preserves important relations and discourse structure.
Pure statistical translation may choose an incorrect sense when context is ambiguous.
