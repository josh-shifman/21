from random import randint
ranks = {"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "King":10, "Queen":10, "Jack":10}
Suits = ["S", "H", "D", "C"]
class Card:
    def __init__(self, rank):
        self.rank = rank
    def __repr__(self):
        return str(self.rank)
    def val(self):
        return ranks[self.rank]
    def __add__(self, other):
        return Card(self.val() + other.val())
    def __radd__(self, other):
        return other + self.val()

def randomCard():
    return Card(list(ranks.keys())[randint(0, 12)])

def compare(numbers):
    closestNum = None
    closestPlayer = None
    tie = False
    for i, element in enumerate(numbers):
        if element <= 21:
            if closestNum == None:
                closestNum = element
                closestPlayer = i + 1
                tie = False
            elif element == 21:
                closestNum = element
                closestPlayer = i + 1
                tie = False
                break
            elif element > closestNum:
                closestNum = element
                closestPlayer = i + 1
                tie = False
            elif element == closestNum:
                tie = True
    if closestNum == None or tie == True:
        return "Nobody won"
    return f"Player {closestPlayer} is the winner!"


def play_again():
    again = input("\nDo you want to play again? \n")
    if again.lower() == "Yes":
        main()
    elif again == "No" or again == "no":
        exit()

def main():
    howmany = int(input("How many players? \n"))

    players = [[] for i in range(howmany)]
    playersTurn = [True for i in range(howmany)]
    playerSum = [0 for i in range(howmany)]

    while sum(playersTurn) > 1:
            for j, element in enumerate(players):
                if playersTurn[j] == True:
                    a = input(f"Player {j+1}'s turn: \n")
                    if a == "hit me":
                        players[j].append(randomCard())
                        print(f"Player {j+1}'s cards:", players[j],"\n")
                        playerSum[j] = sum(players[j])
                        if playerSum[j] >= 21:
                            playersTurn[j] = False
                            break
                    elif a == "pass":
                        playerSum[j] = False



    print(compare(playerSum))
    play_again()





if __name__ == "__main__":
    main()

