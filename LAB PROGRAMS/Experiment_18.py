import re
def parse(expression):
    pattern = r"^\s*([A-Za-z]+)\s*(AND|OR)\s*([A-Za-z]+)\s*$"
    match = re.match(pattern, expression, re.IGNORECASE)
    if match:
        left, op, right = match.groups()
        print("Operator:", op.upper())
        print("Left:", left)
        print("Right:", right)
        print("Valid FOPC expression")
    else:
        print("Invalid FOPC expression")
expression = input("Enter logical expression: ")
parse(expression)


Input:
Enter logical expression: P AND Q

Output:
Operator: AND
Left: P
Right: Q
Valid FOPC expression
