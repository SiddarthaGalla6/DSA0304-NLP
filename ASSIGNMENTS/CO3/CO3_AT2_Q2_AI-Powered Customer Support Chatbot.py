print("CASE STUDY 2: AI-Powered Customer Support Chatbot")
s1=[("Book","VB"),("a","DT"),("flight","NN"),("ticket","NN"),("now","RB")]
s2=[("This","DT"),("book","NN"),("is","VBZ"),("interesting","JJ")]
print("\n1. POS Tags")
print("Sentence 1:",s1)
print("Sentence 2:",s2)
p_book_vb=0.6
p_start_vb=0.5
p_book_nn=0.4
p_start_nn=0.5
vb=p_start_vb*p_book_vb
nn=p_start_nn*p_book_nn
print("\n2. HMM Probability for book as VB")
print("P(Start->VB) =",p_start_vb)
print("P(book|VB) =",p_book_vb)
print("Likelihood =",round(vb,3))
print("NN likelihood =",round(nn,3))
print("Result: VB is preferred because its likelihood is higher.")
print("\n3. Rule-Based vs HMM Tagging")
print("Rule-Based: Uses fixed grammatical rules and is simple.")
print("HMM: Uses emission and transition probabilities and handles context better.")
print("Recommendation: HMM is more suitable for large-scale chatbot deployment.")
print("\n4. Role of POS Tagsets")
print("Standard POS tags provide consistent word classes.")
print("They improve intent detection and response generation.")
print("They also improve grammatical analysis and chatbot accuracy.")

Output :
CASE STUDY 2: AI-Powered Customer Support Chatbot

1. POS Tags
Sentence 1: [('Book', 'VB'), ('a', 'DT'), ('flight', 'NN'), ('ticket', 'NN'), ('now', 'RB')]
Sentence 2: [('This', 'DT'), ('book', 'NN'), ('is', 'VBZ'), ('interesting', 'JJ')]

2. HMM Probability for book as VB
P(Start->VB) = 0.5
P(book|VB) = 0.6
Likelihood = 0.3
NN likelihood = 0.2
Result: VB is preferred because its likelihood is higher.

3. Rule-Based vs HMM Tagging
Rule-Based: Uses fixed grammatical rules and is simple.
HMM: Uses emission and transition probabilities and handles context better.
Recommendation: HMM is more suitable for large-scale chatbot deployment.

4. Role of POS Tagsets
Standard POS tags provide consistent word classes.
They improve intent detection and response generation.
They also improve grammatical analysis and chatbot accuracy.
