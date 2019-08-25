numbers = [19,22,23,24]

def compare(numbers):
    closestNum = None
    closestPlayer = None

    for i, element in enumerate(numbers):
        if element <= 21:
            if closestNum == None:
                closestNum = element
                closestPlayer = i + 1
            if element == 21:
                closestNum = element
                closestPlayer = i + 1
                break
            if element > closestNum:
                closestNum = element
                closestPlayer = i + 1
    if closestNum == None:
        return "Nobody won              "
    return f"Player {closestPlayer} is the winner!"


