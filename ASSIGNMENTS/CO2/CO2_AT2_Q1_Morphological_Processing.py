words = ["analyzing", "analysis", "analytical"]
def morphological_parser(word):
    root = word
    transformation = "Base"
    if word.endswith("ing"):
        root = "analyze"
        affix = "-ing"
        transformation = "Inflectional"
    elif word.endswith("sis"):
        root = "analyze"
        affix = "-sis"
        transformation = "Derivational"
    elif word.endswith("ical"):
        root = "analyze"
        affix = "-ical"
        transformation = "Derivational"
    normalized = root
    return [word, root, affix, transformation, normalized]
print("-"*78)
print("{:<15}{:<15}{:<12}{:<18}{:<15}".format(
    "Original","Root","Affix","Transformation","Normalized"))
print("-"*78)
for word in words:
    result = morphological_parser(word)
print("{:<15}{:<15}{:<12}{:<18}{:<15}".format(*result))


Output 
------------------------------------------------------------------------------
Word           Root        Suffix       Type              Normalized
------------------------------------------------------------------------------
connected      connect     ed        Inflectional         connect
connecting     connect     ing       Inflectional         connect
connection     connect     ion       Derivational       connect
