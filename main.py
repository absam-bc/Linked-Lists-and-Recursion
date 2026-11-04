from linked_list import LinkedList


if __name__ == "__main__":
    employee_ids = LinkedList()

    # Insert employee IDs.
    employee_ids.insert_at_end(101)
    employee_ids.insert_at_end(102)
    employee_ids.insert_at_end(103)
    employee_ids.insert_at_end(104)

    print("Employee IDs:")
    employee_ids.display()

    # Calculate the sum recursively.
    print("Sum of employee IDs:", employee_ids.recursive_sum())

    # Search for an employee ID.
    print("Is employee 103 in the list?",
          employee_ids.recursive_search(103))

    print("Is employee 999 in the list?",
          employee_ids.recursive_search(999))

    # Reverse the list recursively.
    employee_ids.recursive_reverse()

    print("Reversed employee IDs:")
    employee_ids.display()
