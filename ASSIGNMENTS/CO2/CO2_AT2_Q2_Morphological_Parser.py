words = ["disagree", "agreement", "agreeable"]
def parse(word):
    prefix = "-"
    suffix = "-"
    root = "agree"
    category = "Derivational"
    meaning = ""
    if word.startswith("dis"):
        prefix = "dis"
        meaning = "Negative / Opposite"
    elif word.endswith("ment"):
        suffix = "-ment"
        meaning = "State or Result"
    elif word.endswith("able"):
        suffix = "-able"
        meaning = "Capable / Positive Quality"
    return [word, prefix, root, suffix, category, meaning, root]
print("-"*110)
print("{:<15}{:<10}{:<12}{:<10}{:<18}{:<28}{:<12}".format(
    "Original","Prefix","Root","Suffix",
    "Transformation","Semantic Meaning","Normalized"))
print("-"*110)
for word in words:
print("{:<15}{:<10}{:<12}{:<10}{:<18}{:<28}{:<12}".format(*parse(word)))


Output
--------------------------------------------------------------------------------------------------------------
Original        Prefix    Root        Suffix    Transformation     Semantic Meaning             Normalized
--------------------------------------------------------------------------------------------------------------
disagree          dis       agree           -           Derivational       Negative / Opposite                agree
agreement        -         agree       -ment       Derivational       State or Result                        agree
agreeable         -         agree       -able         Derivational       Capable / Positive Quality     agree
