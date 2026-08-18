print("TRANSITION-BASED VS GRAPH-BASED DEPENDENCY PARSING")
sentence="The student reads a book"
words=sentence.lower().split()
transition_steps=[]
stack=[]
buffer=words.copy()
while buffer:
    word=buffer.pop(0)
    stack.append(word)
    transition_steps.append(("SHIFT",word))
print("\nSentence:",sentence)
print("\nTransition-Based Parsing")
for step,word in transition_steps:
    print(step,":",word)
transition_speed=len(words)
graph_candidates=len(words)*(len(words)-1)
print("\nTransition-Based Statistics")
print("Words processed:",transition_speed)
print("Local decisions:",transition_speed)
print("Processing type: Incremental")
print("Speed: Fast")
print("\nGraph-Based Parsing")
print("Possible dependency edges:",graph_candidates)
print("Processing type: Global")
print("Decision type: Complete tree evaluation")
print("Speed: Slower")
print("\nComparison")
methods={
"Transition-Based":{"speed":3,"memory":2,"global":1},
"Graph-Based":{"speed":1,"memory":3,"global":3}
}
for method,values in methods.items():
    print(method)
    print("Speed:",values["speed"])
    print("Memory:",values["memory"])
    print("Global Optimization:",values["global"])
if methods["Transition-Based"]["speed"]>methods["Graph-Based"]["speed"]:
    best="Transition-Based"
else:
    best="Graph-Based"
print("\nRecommended Method:",best)
print("Reason: It provides faster incremental parsing for large-scale applications.")

Output:
TRANSITION-BASED VS GRAPH-BASED DEPENDENCY PARSING

Sentence: The student reads a book

Transition-Based Parsing
SHIFT : the
SHIFT : student
SHIFT : reads
SHIFT : a
SHIFT : book

Transition-Based Statistics
Words processed: 5
Local decisions: 5
Processing type: Incremental
Speed: Fast

Graph-Based Parsing
Possible dependency edges: 20
Processing type: Global
Decision type: Complete tree evaluation
Speed: Slower

Comparison
Transition-Based
Speed: 3
Memory: 2
Global Optimization: 1
Graph-Based
Speed: 1
Memory: 3
Global Optimization: 3

Recommended Method: Transition-Based
Reason: It provides faster incremental parsing for large-scale applications.
