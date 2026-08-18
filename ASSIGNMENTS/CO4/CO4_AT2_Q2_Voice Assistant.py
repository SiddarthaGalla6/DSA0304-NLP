from collections import namedtuple
command="book a flight to Delhi with a window seat"
tokens=command.split()
structures=[["book","a flight","to Delhi","with a window seat"],["book","a flight to Delhi","with a window seat"]]
top_down={"method":"Top-Down","backtracking":True,"partial_input":False,"ambiguity":"High","real_time":"Moderate"}
earley={"method":"Earley","backtracking":False,"partial_input":True,"ambiguity":"Handled","real_time":"High"}
print("VOICE ASSISTANT PARSING")
print("Command:",command)
print("\nPossible Parse Structures")
for i,structure in enumerate(structures,1):
    print("Parse",i,":",structure)
print("\nTop-Down Parsing")
for key,value in top_down.items():
    print(key,":",value)
print("\nEarley Parsing")
for key,value in earley.items():
    print(key,":",value)
comparison={"Backtracking":{"Top-Down":"High","Earley":"Low"},"Ambiguity":{"Top-Down":"Difficult","Earley":"Good"},"Partial Input":{"Top-Down":"Poor","Earley":"Good"},"Long Input":{"Top-Down":"Less efficient","Earley":"More efficient"},"Real-Time Response":{"Top-Down":"Moderate","Earley":"High"}}
print("\nPerformance Comparison")
for category,result in comparison.items():
    print(category,": Top-Down =",result["Top-Down"],"| Earley =",result["Earley"])
print("\nConclusion")
print("Top-Down parsing is simple but requires backtracking.")
print("Earley parsing maintains multiple possibilities efficiently.")
print("Earley parsing is more suitable for ambiguous and incomplete voice commands.")


Output:
VOICE ASSISTANT PARSING
Command: book a flight to Delhi with a window seat

Possible Parse Structures
Parse 1 : ['book', 'a flight', 'to Delhi', 'with a window seat']
Parse 2 : ['book', 'a flight to Delhi', 'with a window seat']

Top-Down Parsing
method : Top-Down
backtracking : True
partial_input : False
ambiguity : High
real_time : Moderate

Earley Parsing
method : Earley
backtracking : False
partial_input : True
ambiguity : Handled
real_time : High

Performance Comparison
Backtracking : Top-Down = High | Earley = Low
Ambiguity : Top-Down = Difficult | Earley = Good
Partial Input : Top-Down = Poor | Earley = Good
Long Input : Top-Down = Less efficient | Earley = More efficient
Real-Time Response : Top-Down = Moderate | Earley = High

Conclusion
Top-Down parsing is simple but requires backtracking.
Earley parsing maintains multiple possibilities efficiently.
Earley parsing is more suitable for ambiguous and incomplete voice commands.
