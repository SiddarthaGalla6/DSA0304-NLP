words = ["govern", "government", "governance"]
def normalize(word):
    root = "govern"
    affix = "-"
    level = "Base"
    if word.endswith("ment"):
        affix = "-ment"
        level = "Level 1"
    elif word.endswith("ance"):
        affix = "-ance"
        level = "Level 1"
    return [word, root, affix, level, root]
print("-"*80)
print("{:<15}{:<15}{:<15}{:<20}{:<15}".format(
    "Original","Root","Affix",
    "Derivational Level","Normalized"))
print("-"*80)
for word in words:
print("{:<15}{:<15}{:<15}{:<20}{:<15}".format(*normalize(word)))


Output 
--------------------------------------------------------------------------------
Original                 Root           Affix          Derivational Level    Normalized
--------------------------------------------------------------------------------
govern          govern         -                         Base                    govern
government      govern         -ment                Level 1                govern
governance      govern         -ance                 Level 1                govern
