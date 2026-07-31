words = ["connected", "connecting", "connection"]
print("-" * 78)
print("{:<15}{:<12}{:<10}{:<18}{:<15}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))
print("-" * 78)
for word in words:
    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        mtype = "Inflectional"
    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        mtype = "Inflectional"
    elif word.endswith("ion"):
        root = "connect"
        suffix = "ion"
        mtype = "Derivational"
    else:
        root = word
        suffix = "-"
        mtype = "None"
    normalized = "connect"
    print("{:<15}{:<12}{:<10}{:<18}{:<15}".format(
        word, root, suffix, mtype, normalized))


Output :
------------------------------------------------------------------------------
Word           Root        Suffix    Type               Normalized
------------------------------------------------------------------------------
connected      connect     ed        Inflectional       connect
connecting     connect     ing       Inflectional       connect
connection     connect     ion       Derivational       connect
