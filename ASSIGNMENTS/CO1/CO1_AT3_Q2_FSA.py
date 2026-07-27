states = ['q0', 'q1', 'q2']
initial = 'q0'
final = 'q2'
transition = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}
text = input("Enter string: ")
current = initial
path = [current]
for ch in text:
    if ch not in ['a', 'b']:
        print("Invalid Symbol")
        break
    current = transition[current][ch]
    path.append(current)
else:
    print("Transition Path:", " -> ".join(path))
    print("Accepted" if current == final else "Rejected")


Output :
Enter string: aaaab
Transition Path: q0 -> q1 -> q1 -> q1 -> q1 -> q2
Accepted
