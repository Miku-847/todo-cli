def get_input(prompt):
    value = input(prompt).strip()
    if not value:
        print("Input cannot be empty!\n")
        return None
    return value
