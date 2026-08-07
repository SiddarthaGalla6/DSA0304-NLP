words = ["create", "creates", "creating"]
def normalize(word):
    suffix = "-"
    category = "Base Form"
    root = "create"
    if word.endswith("ing"):
        suffix = "-ing"
        category = "Present Participle"
    elif word.endswith("s"):
        suffix = "-s"
        category = "Third-Person Singular"
    normalized = root
    return [word, suffix, category, root, normalized]
print("-"*90)
print("{:<15}{:<15}{:<25}{:<15}{:<15}".format(
    "Original",
    "Suffix",
    "Grammatical Category",
    "Root",
    "Normalized"))
print("-"*90)
for word in words:
    result = normalize(word)
print("{:<15}{:<15}{:<25}{:<15}{:<15}".format(*result))



Output 
------------------------------------------------------------------------------------------
Original       Suffix         Grammatical Category      Root            Normalized
------------------------------------------------------------------------------------------
create              -                    Base Form                    create            create
creates           -s               Third-Person Singular      create            create
creating       -ing               Present Participle            create             create
