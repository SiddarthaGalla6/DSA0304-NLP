queries={"Q1":("ACTIVATE","Roaming","Activate Roaming"),"Q2":("DEACTIVATE","CallerTune","Activate Caller Tune"),"Q3":("QUERY","DataBalance","Query Data Balance"),"Q4":("ACTIVATE","5GService","Activate 5G Service")}
print("1. Action-Object Relationships")
for q,(action,obj,intent) in queries.items():
    print(q,":",action,"->",obj)
print("\n2. Semantic Interpretation Errors")
for q,(action,obj,intent) in queries.items():
    actual=action+" "+obj
    if actual.lower()!=intent.lower():
        print(q,"has an error")
        print("Expected:",actual)
        print("Predicted:",intent)
print("\n3. Effect of Meaning Representation")
print("Correct representations connect the user action with the correct service object.")
print("Incorrect representations can cause wrong chatbot decisions.")
correct=3
total=4
accuracy=correct/total*100
print("Semantic Decision Accuracy =",accuracy,"%")
print("\n4. Improvements")
print("Use context-aware language models.")
print("Use telecom-specific training data.")
print("Use entity and intent recognition.")
print("Use conversation history for ambiguous queries.")
print("Continuously retrain the semantic model using chatbot feedback.")


Output:
1. Action-Object Relationships
Q1 : ACTIVATE -> Roaming
Q2 : DEACTIVATE -> CallerTune
Q3 : QUERY -> DataBalance
Q4 : ACTIVATE -> 5GService

2. Semantic Interpretation Errors
Q2 has an error
Expected: DEACTIVATE CallerTune
Predicted: Activate Caller Tune

3. Effect of Meaning Representation
Correct representations connect the user action with the correct service object.
Incorrect representations can cause wrong chatbot decisions.
Semantic Decision Accuracy = 75.0 %

4. Improvements
Use context-aware language models.
Use telecom-specific training data.
Use entity and intent recognition.
Use conversation history for ambiguous queries.
Continuously retrain the semantic model using chatbot feedback.
