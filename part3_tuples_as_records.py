"""Part 3: Tuples as Records
A tuple is immutable. In databases, 'tuple' can also mean a row/record.
"""

students = [
    (1, "Alice", "GSAS", 32),
    (2, "Bob", "Tandon", 28),
    (3, "Carol", "GSAS", 40)
]
# columns: (id, name, school, credits)

# TODO 1: Print the name for each record
for s in students:
    print(s[1])
# TODO 2: Try to change Bob’s credits directly (observe the error)
students[1][3] = 30
print(students)
# TODO 3: Create a new tuple for Bob with credits=30 and replace the old record in the list
students[1] = (2, "Bob", "Tandon", 30)
print(students)

# Reflection (answer in a comment): Tuples are immutable but we can change them by add a new column and replace the old one.
# TODO: Why might immutability be good for data integrity?
# We can see the historical versions of how data is changed, so that important information will not be removed easily. Our data is ensured to be accurate and reliable.
