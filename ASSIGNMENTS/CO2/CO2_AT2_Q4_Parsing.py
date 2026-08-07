words = ["activate", "activation", "reactivation"]
def parser(word):
    prefix = "-"
    suffix = "-"
    root = "activate"
    sequence = "Base Form"
    if word.endswith("ion"):
        suffix = "-ion"
        sequence = "Verb → Noun"
    if word.startswith("re"):
        prefix = "re"
        sequence = "Prefix + Verb → Noun"
    return [word,prefix,root,suffix,sequence,root]
print("-"*100)
print("{:<18}{:<10}{:<15}{:<10}{:<28}{:<15}".format(
    "Original","Prefix","Root",
    "Suffix","Derivational Sequence","Normalized"))
print("-"*100)
for word in words:
    print("{:<18}{:<10}{:<15}{:<10}{:<28}{:<15}".format(*parser(word)))



Output
----------------------------------------------------------------------------------------------------
Original          Prefix    Root            Suffix    Derivational Sequence       Normalized
----------------------------------------------------------------------------------------------------
activate             -         activate            -               Base Form                      activate
activation          -         activate        -ion          Verb → Noun                    activate
reactivation      re        activate        -ion        Prefix + Verb → Noun        activate
