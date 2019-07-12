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

def main():
    player1 = []
    player2 = []
    for i in range(3):
        player1.append(randomCard())
    print(sum(player1), print(player1))



if __name__ == "__main__":
    main()

