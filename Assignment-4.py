employee = {
    "emp_id": 101,
    "name": "Amit",
    "department": "IT",
    "salary": 50000
}

print("Original dict:", employee)

# accessing elements
print("Employee Name:", employee["name"])

# updating dictionary
employee["salary"] = 55000
employee["location"] = "Pune"

print("After Update:", employee)

# Merging dictionaries
additional_info = {"experience": "2 Years"}
employee.update(additional_info)

print("Final Dictionary:", employee)