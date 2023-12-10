
#___________ validations ___________#

def out_of_range_check(value):
    if value not in [0, 20, 40, 60, 80, 100, 120]:
        print(f"{value} is out of range.")
        return True
    return False