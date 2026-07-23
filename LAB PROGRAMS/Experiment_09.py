import re
def pos_tag(word):
    if re.match(r'.*ing$', word):
        return "VBG"
    elif re.match(r'.*ed$', word):
        return "VBD"
    elif re.match(r'.*ly$', word):
        return "RB"
    elif re.match(r'.*ous$', word):
        return "JJ"
    elif re.match(r'^[0-9]+$', word):
        return "CD"
    elif word.lower() in ["a", "an", "the"]:
        return "DT"
    else:
        return "NN"
sentence = input("Enter a sentence: ")
words = sentence.split()
print("POS Tags:")
for word in words:
    print(word, "->", pos_tag(word))


Input :
Enter a sentence: The boy is running quickly

Output :
POS Tags:
The -> DT
boy -> NN
is -> NN
running -> VBG
quickly -> RB
