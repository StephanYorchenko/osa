class Player:
    count = 0
    ids = 0
    lisOfClass = {}

    def __init__(self):
        self.name = input('Enter your name: ')
        self.bet = 0
        self.coins = 1000
        self.items = []
        self.auc_id = -1
        Player.count += 1
        Player.ids += 1
        self.id = Player.ids
        Player.lisOfClass[self.id] = self

    def make_a_bet(self, min_bet):
        bet = int(input('Make ur bet (from {}): '.format(min_bet)))
        if self.bet != bet:
            self.bet = max(min_bet, min(self.coins, bet))
            return 1
        return 0

    def win_a_round(self):
        self.coins -= self.bet
        self.bet = 0
        self.items.append(Auction.lisOfClass[self.auc_id].pop(0))

    def __del__(self):
        Player.count -= 1
        Player.lisOfClass.pop(self.id)


class Auction:
    count = 0
    ids = 0
    lisOfClass = {}

    def __init__(self):
        Auction.count += 1
        Auction.ids += 1
        self.id = Auction.ids
        self.items = []  #
        self.players = []
        self.step = 10
        Auction.lisOfClass[self.id] = self

    def join(self, pl_id):
        self.players.append(Player.lisOfClass[pl_id])
        self.players[-1].auc_id = self.id

    def pop(self):
        return self.items.pop(0)

    def bets(self):
        n = len(self.players)
        while n > 1:
            for player in self.players:
                if player.bet != -1:
                    if player.make_a_bet(player.bet + self.step) == 0:
                        n -= 1
                        player.bet = -1
        for player in self.players:
            if player.bet == -1:
                player.bet = 0
            else:
                player.win_a_round()
        return len(self.items) > 0

    def __del__(self):
        Auction.count -= 1
        Auction.lisOfClass.pop(self.id)


if __name__ == '__main__':
    pass
