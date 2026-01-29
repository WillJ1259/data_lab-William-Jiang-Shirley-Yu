"""Part 2: Dictionaries as Rows
Each row is a dict: {"id": ..., "name": ..., ...}
Schema becomes explicit and safer to access.
"""

students = [
    {"id": 1, "name": "Alice", "school": "GSAS", "credits": 32},
    {"id": 2, "name": "Bob", "school": "Tandon", "credits": 28},
    {"id": 3, "name": "Carol", "school": "GSAS", "credits": 40},
    {"id": 4, "name": "Dan", "school": "CAS", "credits": 18}
]

# TODO 1: Print all student names
for s in students:
    print(s["name"])

# TODO 2: Print only GSAS students (name + credits)
gsas = [s for s in students if s["school"] == "GSAS"]
print([s["name"] for s in gsas])

# TODO 3: Add a new field to each row:
#   status='full-time' if credits >= 30 else 'part-time'
for s in students:
    if s["credits"] >= 30:
        s["status"] = "full-time"
    else:
        s["status"] = "part-time"
print(students)

# TODO 4: Update Bob’s credits to 30 AND ensure his status updates correctly
students[1].update({"credits":30, "status":"full-time"})
print(students[1])

def get_students_by_school(rows, school):
    """Return a list of rows where row['school'] == school."""
    # TODO 5: implement
    return [s["name"] for s in rows if s["school"] == school]

# TODO 6: Call get_students_by_school(students, "GSAS") and print results
print(get_students_by_school(students, "GSAS"))

# Reflection (answer in a comment):
# TODO: Why is dict-based code safer than index-based list code?
# It is safer because it relies on key-value pairs to access, and it doesn't break sliently
