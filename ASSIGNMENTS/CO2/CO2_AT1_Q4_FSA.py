words = ["writes", "writing", "written"]
print("-" * 100)
print("{:<12}{:<22}{:<10}{:<15}{:<15}".format(
    "Word", "State Transition", "Root", "Pattern", "Normalized"))
print("-" * 100)
for word in words:
    if word.endswith("s"):
        transition = "S0->S1->S2"
        root = "write"
        pattern = "Regular"
    elif word.endswith("ing"):
        transition = "S0->S1->S2"
        root = "write"
        pattern = "Regular"
    elif word == "written":
        transition = "S0->S3->S2"
        root = "write"
        pattern = "Irregular"
    else:
        transition = "-"
        root = word
        pattern = "Unknown"
    normalized = "write"
    print("{:<12}{:<22}{:<10}{:<15}{:<15}".format(
        word, transition, root, pattern, normalized))


Output :
----------------------------------------------------------------------------------------------------
Word        State Transition      Root      Pattern         Normalized
----------------------------------------------------------------------------------------------------
writes      S0->S1->S2            write     Regular         write
writing     S0->S1->S2            write     Regular         write
written     S0->S3->S2            write     Irregular       write
