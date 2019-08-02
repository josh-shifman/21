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

def compare(p1, p2):
    if p1 == p2:
        return "It's a tie"
    elif p1 == 21 and p2 != 21:
        return "Player 1 Wins"
    elif p1 != 21 and p2 == 21:
        return "Player 2 Wins"
    elif p1 > p2:
        return "Player 1 Wins"
    elif p2 > p1:
        return "Player 2 Wins"


def play_again():
    again = input("\nDo you want to play again? \n")
    if again == "Yes" or again == "yes":
        main()
    elif again == "No" or again == "no":
        exit()
def main():
    player1 = []
    player2 = []
    player1Turn = True
    player2Turn = True
    while player1Turn or player2Turn:
            if player1Turn:
                a = input("Player 1's turn: \n")
                if a == "hit me":
                    player1.append(randomCard())
                    print("Player 1's cards:", player1,"\n")
                    player1sum = sum(player1)
                    if player1sum > 21:
                        break
                elif a == "pass":
                    player1Turn = False

            if player2Turn:
                b = input("Player 2's turn: \n")
                if b == "hit me":
                    player2.append(randomCard())
                    print("Player 2's cards:", player2,"\n")
                    player2sum = sum(player2)
                    if player2sum > 21:
                        break
                elif b == "pass":
                    player2Turn = False

    player1sum = sum(player1)
    player2sum = sum(player2)
    print("\nPlayer 1:", player1sum, "\nPlayer 2:", player2sum, "\n")
    print(compare(player1sum, player2sum))
    play_again()





if __name__ == "__main__":
    main()

