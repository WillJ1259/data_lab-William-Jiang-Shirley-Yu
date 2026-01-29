"""Part 1: Lists as Tables
Each row is a list: [id, name, school, credits]
Schema is implicit — your code depends on correct indexes.
"""

students = [
    [1, "Alice", "GSAS", 32],
    [2, "Bob", "Tandon", 28],
    [3, "Carol", "GSAS", 40],
    [4, "Dan", "CAS", 18]
]
# columns: [id, name, school, credits]

# TODO 1: Print all student names (one per line)
for s in students:
    print(s[1])
# TODO 2: Print only the students in GSAS (id and name)
for s in students:
    if s[2] == "GSAS":
        print(s[1])
# TODO 3: Print students with credits > 30 (name and credits)
for s in students:
    if s[3] > 30:
        print(s[1],s[3])
# TODO 4: Insert a new student row for: id=5, name='Eve', school='CAS', credits=22
students.insert(4, [5, "Eve", "CAS", 22])
print(students)
# TODO 5: Update Bob’s credits to 30
students[1][3] = 30
print(students)
# Reflection (answer in a comment):
# TODO: What breaks if we insert a new column at position 2?
# Answer: It will add a new student between Bob and Carol.
