words = []
pos = 0
def match(word):
    global pos
    if pos < len(words) and words[pos] in word:
        pos += 1
        return True
    return False
def NP():
    return match(["the", "a"]) and match(["boy", "girl", "ball"])
def VP():
    return match(["sees", "likes"]) and NP()
def S():
    return NP() and VP()
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
if S() and pos == len(words):
    print("Sentence Accepted")
else:
    print("Sentence Rejected")


Input:
Enter a sentence: the boy sees a girl

Output:
Sentence Accepted
