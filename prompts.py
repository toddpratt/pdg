def print_dict(treasure):
    for k in treasure:
        print(f"    {treasure[k]} {k}")


def confirm(prompt):
    response = ''
    while True:
        response = input(prompt)
        if response == 'y' or response == 'n':
            break
    return response