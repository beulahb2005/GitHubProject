import random
def get_random_code():
    # Generate a random 5-digit number
    rand_num = str(random.randint(10000, 99999))
    # Add a hyphen to the number
    hyphenated_num = "-".join([rand_num[:3], rand_num[3:]])
    return hyphenated_num