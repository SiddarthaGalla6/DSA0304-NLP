words = ["relational", "relation", "relate"]
print("-" * 100)
print("{:<15}{:<25}{:<22}{:<15}".format(
    "Word", "Applied Rule", "Intermediate", "Final Stem"))
print("-" * 100)
for word in words:
    if word == "relational":
        rule = "ational -> ate"
        intermediate = "relate"
        final_stem = "relat"
    elif word == "relation":
        rule = "Remove ion"
        intermediate = "relate"
        final_stem = "relat"
    elif word == "relate":
        rule = "Remove e"
        intermediate = "relate"
        final_stem = "relat"
    else:
        rule = "-"
        intermediate = word
        final_stem = word
    print("{:<15}{:<25}{:<22}{:<15}".format(
        word, rule, intermediate, final_stem))


Output :
----------------------------------------------------------------------------------------------------
Word           Applied Rule             Intermediate           Final Stem
----------------------------------------------------------------------------------------------------
relational     ational -> ate           relate                 relat
relation       Remove ion               relate                 relat
relate         Remove e                 relate                 relat
