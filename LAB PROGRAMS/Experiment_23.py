import re
text = input("Enter text: ")
sentences = re.split(r"[.!?]+", text)
sentences = [s.strip() for s in sentences if s.strip()]
word_counts = [len(s.split()) for s in sentences]
if len(word_counts) <= 1:
    score = 1.0
else:
    average = sum(word_counts) / len(word_counts)
    score = 1 - (max(word_counts) - min(word_counts)) / max(average, 1)
print("Coherence Score:", round(max(0, score), 2))


Input:
Enter text: I like Python. Python is useful. I learn Python.

Sample Output:
Coherence Score: 1.0
