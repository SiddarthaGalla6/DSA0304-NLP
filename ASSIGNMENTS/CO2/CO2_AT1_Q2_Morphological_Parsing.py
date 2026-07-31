words = ["unhappy", "happiness", "happily"]
print("-" * 95)
print("{:<15}{:<10}{:<12}{:<10}{:<18}{:<15}".format(
    "Word", "Prefix", "Root", "Suffix", "Type", "Normalized"))
print("-" * 95)
for word in words:
    prefix = "-"
    suffix = "-"
    root = ""
    mtype = "Derivational"
    if word.startswith("un"):
        prefix = "un"
        root = word[2:]
    elif word.endswith("ness"):
        suffix = "ness"
        root = "happy"
    elif word.endswith("ly"):
        suffix = "ly"
        root = "happy"
    normalized = "happy"
    print("{:<15}{:<10}{:<12}{:<10}{:<18}{:<15}".format(
        word, prefix, root, suffix, mtype, normalized))

Output :
-----------------------------------------------------------------------------------------------
Word           Prefix    Root        Suffix    Type               Normalized
-----------------------------------------------------------------------------------------------
unhappy        un        happy       -         Derivational       happy
happiness      -         happy       ness      Derivational       happy
happily        -         happy       ly        Derivational       happy
