machines={"M1":"Active","M2":"Active","M3":"Maintenance","M4":"Active"}
print("1. First-Order Predicate Calculus Representation")
for machine,status in machines.items():
    if status=="Active":
        print("Active("+machine+")")
        print("Producing("+machine+")")
    else:
        print("Maintenance("+machine+")")
        print("¬Producing("+machine+")")
print("\n2. Currently Available Products")
print("No specific product can be inferred because Produces(x,y) facts are not provided.")
print("\n3. Gear Production")
print("M3 is under maintenance.")
print("Maintenance(M3) -> ¬Producing(M3)")
print("Gear production is affected only if Produces(M3,Gear) is true.")
print("Therefore, Gear production cannot be conclusively determined from the given data.")
print("\n4. Effectiveness of Predicate Logic")
print("Predicate logic represents machine states and production rules clearly.")
print("It supports automated reasoning and decision making.")
print("It can identify production restrictions caused by maintenance.")
print("It is useful for industrial monitoring and decision-support systems.")


Output:
1. First-Order Predicate Calculus Representation
Active(M1)
Producing(M1)
Active(M2)
Producing(M2)
Maintenance(M3)
¬Producing(M3)
Active(M4)
Producing(M4)

2. Currently Available Products
No specific product can be inferred because Produces(x,y) facts are not provided.

3. Gear Production
M3 is under maintenance.
Maintenance(M3) -> ¬Producing(M3)
Gear production is affected only if Produces(M3,Gear) is true.
Therefore, Gear production cannot be conclusively determined from the given data.

4. Effectiveness of Predicate Logic
Predicate logic represents machine states and production rules clearly.
It supports automated reasoning and decision making.
It can identify production restrictions caused by maintenance.
It is useful for industrial monitoring and decision-support systems.
