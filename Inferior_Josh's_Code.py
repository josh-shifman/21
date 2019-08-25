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
class Player:
  def __init__(self, num):
    self.player = num
    self.cards = []
    self.summation = 0
    self.turn = True
  def __repr__(self):
    return f"PlayerNumber: {self.player}, cards: {self.cards}, sum : {self.summation}"

def randomCard():
    return Card(list(ranks.keys())[randint(0, 12)])


def play_again():
    again = input("\nDo you want to play again? \n")
    if again == "Yes" or again == "yes":
        main()
    elif again == "No" or again == "no":
        exit()

def main():
    players = input("how many players are there?")
    playerlist = [[] for i in range(int(players))]
    playerTurn = [True for i in range(int(players))]
    playerSum = [0 for i in range(int(players))]
    while sum(playerTurn) > 1:
      for i, player in enumerate(playerlist):
        if playerTurn[i]:
          a = input(f"Player {i+1}'s turn: Do you want to 'hit me'? (y/n) \n")
          if a == "y":
              player.append(randomCard())
              print(f"Player {i+1}'s cards:", player,"\n")
              playerSum[i] = sum(player)
              print(playerSum[i])
              if playerSum[i] > 21:
                playerTurn[i] = False
                print(f"player {i+1} is out!")
          elif a == "n":
              playerTurn[i] = False
          if sum(playerTurn) == 1:
            break
    diff = [21 - score for score in playerSum]
    winners = []
    for i, player in enumerate(playerlist):
      if playerSum[i]<=21:
        if winners == []:
          winners.append({"player": i +1, "score": playerSum[i]})
        elif playerSum[i]> winners[0]["score"]:
          winners = [{"player": i+1, "score": playerSum[i]}]
        elif playerSum[i] == winners[0]["score"]:
          winners.append({"player": i+1, "score": playerSum[i]})
    if winners == []:
      print("There are no winners :(")
      play_again()
    winner = winners[0]["player"]
    print(f"The Winners are: Player {winner}")
    play_again()

if __name__ == "__main__":
    main()