user_input = "I have an important exam tomorrow but I’m not able to concentrate."
responses = [
    "Your exam is important, so take a short break and return with better focus. You can stay confident by studying one small topic at a time.",
    "Because your exam is tomorrow, avoid studying continuously and take a short break. Focus on the most important topics and stay confident.",
    "Your exam may feel stressful, but you can improve your concentration with a short break. Then focus on one topic at a time and stay confident."
]
print("Input:")
print(user_input)
print("\nDiscourse Planning Steps")
print("1. Identify the dialog act: Advise + Encourage")
print("2. Identify entities: exam, concentrate, you")
print("3. Establish Cause-Effect relation")
print("4. Add advice and motivation")
print("5. Check required keywords")
print("6. Generate a positive response")
print("\nPossible Responses")
for i, response in enumerate(responses, 1):
    print("\nResponse", i)
    print(response)
print("\nEvaluation")
scores = [5, 5, 5]
for i, score in enumerate(scores, 1):
    print("Response", i, ":", score, "/ 5")
best = responses[1]
print("\nBest Response")
print(best)
print("\nJustification")
print("Response 2 directly connects the exam with concentration advice.")
print("It contains focus, break, and confident.")
print("It maintains entity coherence and uses a clear Cause-Effect relation.")
print("It is polite, positive, logically consistent, and has 2 sentences.")
print("\nEffect of Constraint Violations")
print("Violating entity coherence can make the conversation confusing.")
print("Violating the positive tone can reduce motivation and encouragement.")


Output:
Input:
I have an important exam tomorrow but I’m not able to concentrate.
Discourse Planning Steps
1. Identify the dialog act: Advise + Encourage
2. Identify entities: exam, concentrate, you
3. Establish Cause-Effect relation
4. Add advice and motivation
5. Check required keywords
6. Generate a positive response

Possible Responses

Response 1
Your exam is important, so take a short break and return with better focus. You can stay confident by studying one small topic at a time.

Response 2
Because your exam is tomorrow, avoid studying continuously and take a short break. Focus on the most important topics and stay confident.

Response 3
Your exam may feel stressful, but you can improve your concentration with a short break. Then focus on one topic at a time and stay confident.

Evaluation
Response 1 : 5 / 5
Response 2 : 5 / 5
Response 3 : 5 / 5

Best Response
Because your exam is tomorrow, avoid studying continuously and take a short break. Focus on the most important topics and stay confident.

Justification
Response 2 directly connects the exam with concentration advice.
It contains focus, break, and confident.
It maintains entity coherence and uses a clear Cause-Effect relation.
It is polite, positive, logically consistent, and has 2 sentences.

Effect of Constraint Violations
Violating entity coherence can make the conversation confusing.
Violating the positive tone can reduce motivation and encouragement.
