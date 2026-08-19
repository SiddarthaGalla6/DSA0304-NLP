def dialog_act(sentence):
    text = sentence.lower().strip()
    if text.endswith("?"):
        return "QUESTION"
    elif text.startswith(("hi", "hello", "hey")):
        return "GREETING"
    elif text.startswith(("thanks", "thank you")):
        return "THANKS"
    elif text.startswith(("please", "can you", "could you")):
        return "REQUEST"
    else:
        return "STATEMENT"
sentence = input("Enter dialog: ")
print("Dialog Act:", dialog_act(sentence))


Input:
Enter dialog: How are you?

Output:
Dialog Act: QUESTION
