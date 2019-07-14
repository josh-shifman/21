from random import randint

class Card:
    def __init__(self, rank):
        self.rank = rank
    def __repr__(self):
        return str(self.rank)
    def __add__(self, other):
        return Card(self.rank + other.rank)
    def __radd__(self, other):
        return other + self.rank


def randomCard():
    return Card(randint(1, 10))

def play_again():
    again = input("\nDo you want to play again? \n")
    if again == "Yes" or again == "yes":
        main()
    elif again == "No" or again == "no":
        exit()

def main():
    player1 = []
    player2 = []
    game = 0
    turn = True
    while game < 2:
        while turn == True:
            a = input("Player 1's turn: \n")
            if a == "hit me":
                player1.append(randomCard())
                print("Player 1's cards:", player1,"\n")
                turn = False
                game = 0
            elif a == "pass":
                turn = False
                game +=1
        while turn == False:
            b = input("Player 2's turn: \n")
            if b == "hit me":
                player2.append(randomCard())
                print("Player 2's cards:", player2,"\n")
                turn = True
            elif b == "pass":
                turn = True
                game+=1

    player1sum = sum(player1)
    player2sum = sum(player2)
    print("\nPlayer 1:", player1sum, "\nPlayer 2:", player2sum, "\n")

    if (player1sum <= 21) and (player2sum > 21):
        print("Player 1 Wins")
    elif (player1sum > 21) and (player2sum <= 21):
        print("Player 2 Wins")
    elif player1sum == player2sum:
        print("It's a tie")
    elif player1sum == 21 and player2sum != 21:
        print("Player 1 Wins")
    elif player1sum != 21 and player2sum == 21:
        print("Player 2 Wins")
    elif player1sum > player2sum:
        print("Player 1 Wins")
    elif player2sum > player1sum:
        print("Player 2 Wins")
    play_again()






if __name__ == "__main__":
    main()

