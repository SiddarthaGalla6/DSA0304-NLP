words = ["played", "player", "playing"]
print("-" * 90)
print("{:<15}{:<12}{:<15}{:<20}{:<15}".format(
    "Word", "Stem", "Removed Affix", "Transformation", "Normalized"))
print("-" * 90)
for word in words:
    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        ttype = "Inflectional"
    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        ttype = "Derivational"
    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        ttype = "Inflectional"
    else:
        stem = word
        affix = "-"
        ttype = "None"
    normalized = "play"
    print("{:<15}{:<12}{:<15}{:<20}{:<15}".format(
        word, stem, affix, ttype, normalized))


Output :
------------------------------------------------------------------------------------------
Word           Stem        Removed Affix  Transformation       Normalized
------------------------------------------------------------------------------------------
played         play        ed             Inflectional         play
player         play        er             Derivational         play
playing        play        ing            Inflectional         play
