queries={"Apple accessories":("Technology Brand","iPhone Charger"),"Mouse wireless":("Computer Device","Bluetooth Mouse"),"Java tutorial":("Programming Language","Coding Lessons"),"Python course":("Programming Language","Software Development Training")}
print("1. Correct Word Sense")
for query,(sense,result) in queries.items():
    print(query,"->",sense)
print("\n2. Semantic Cues")
print("Apple accessories -> iPhone Charger -> technology context")
print("Mouse wireless -> Bluetooth Mouse -> computer device context")
print("Java tutorial -> Coding Lessons -> programming context")
print("Python course -> Software Development Training -> programming context")
print("\n3. Impact of Incorrect Sense Selection")
print("Incorrect sense selection produces irrelevant search results.")
print("It reduces user satisfaction and click-through rate.")
print("It can also reduce recommendation accuracy and sales.")
print("\n4. Industrial-Scale WSD Strategy")
print("Use contextual language models.")
print("Use query history and clicked results.")
print("Use product categories and metadata.")
print("Use user behavior and personalization.")
print("Continuously train the WSD model using search and click data.")

Output:
1. Correct Word Sense
Apple accessories -> Technology Brand
Mouse wireless -> Computer Device
Java tutorial -> Programming Language
Python course -> Programming Language

2. Semantic Cues
Apple accessories -> iPhone Charger -> technology context
Mouse wireless -> Bluetooth Mouse -> computer device context
Java tutorial -> Coding Lessons -> programming context
Python course -> Software Development Training -> programming context

3. Impact of Incorrect Sense Selection
Incorrect sense selection produces irrelevant search results.
It reduces user satisfaction and click-through rate.
It can also reduce recommendation accuracy and sales.

4. Industrial-Scale WSD Strategy
Use contextual language models.
Use query history and clicked results.
Use product categories and metadata.
Use user behavior and personalization.
Continuously train the WSD model using search and click data.
