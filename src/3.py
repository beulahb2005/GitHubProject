import random
def generate_random_python_code(n):
    """
    Generate a random Python code of length n
    """
    code = ""
    for i in range(n):
        code += chr(random.randint(97, 122))
    return code