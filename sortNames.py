def find(userName):
    with open("users.txt", 'r') as f:
        for line in f:
            if userName == line.strip():
                return True

    return False


def insert(userName):
    with open("users.txt", 'r') as f:
        lines = f.readlines()

    index = 0
    for i in range(len(lines)):
        if userName < lines[i]:
            index = i
            break
        else:
            index = i + 1

    lines.insert(index, userName + '\n')

    with open('users.txt', 'w') as f:
        f.writelines(lines)
