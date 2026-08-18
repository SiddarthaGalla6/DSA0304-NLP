print("TOP-DOWN PARSING VS EARLEY PARSING")
sentence="Book a flight to Delhi"
top_down={
"Parsing direction":"Root to input",
"Backtracking":"High",
"Ambiguity handling":"Limited",
"Incomplete input":"Poor",
"Memory usage":"Lower"
}
earley={
"Parsing direction":"Dynamic chart parsing",
"Backtracking":"Reduced",
"Ambiguity handling":"Good",
"Incomplete input":"Good",
"Memory usage":"Higher"
}
print("\nInput:",sentence)
print("\nTop-Down Parsing")
for key,value in top_down.items():
    print(key,":",value)
print("\nEarley Parsing")
for key,value in earley.items():
    print(key,":",value)
print("\nComparison")
print("Top-down parsing starts from the grammar start symbol.")
print("It may require backtracking when a prediction fails.")
print("Earley parsing stores partial parsing states in a chart.")
print("Earley parsing can handle incomplete and ambiguous input.")
print("\nConclusion")
print("Earley parsing is more suitable for dynamic real-time input.")

Output:
TOP-DOWN PARSING VS EARLEY PARSING

Input: Book a flight to Delhi

Top-Down Parsing
Parsing direction : Root to input
Backtracking : High
Ambiguity handling : Limited
Incomplete input : Poor
Memory usage : Lower

Earley Parsing
Parsing direction : Dynamic chart parsing
Backtracking : Reduced
Ambiguity handling : Good
Incomplete input : Good
Memory usage : Higher

Comparison
Top-down parsing starts from the grammar start symbol.
It may require backtracking when a prediction fails.
Earley parsing stores partial parsing states in a chart.
Earley parsing can handle incomplete and ambiguous input.

Conclusion
Earley parsing is more suitable for dynamic real-time input.
