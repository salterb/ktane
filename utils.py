def get_input(string):
    """Removes spaces and forces uppercase for all inputs to ensured
    uniformity.
    """
    return input(string).upper().replace(' ', '')


def get_bool(string):
    while True:
        value = get_input(string)
        if value.startswith("Y"):
            return True
        if value.startswith("N"):
            return False
        print("Invalid input")
