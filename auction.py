class Room:
    def __init__(self, array_users, auc_step=100, min_cost=500):
        """
        Initialisation of room
        :param array_users: PlayerChain()
        :param auc_step: minimal value of bet
        """
        self.users_array = array_users
        self.auc_step = auc_step
        self.current_cost = min_cost
        self.send_step()

    def get_number_players(self):
        return len(self.users_array)

    def next_step(self):
        self.player_bet(self.users_array[0].get_bet())

    def player_bet(self, bet):
        if bet > self.users_array.get_max_value() + self.auc_step:
            self.users_array.append()
        else:
            self.users_array.pop()
        if self.users_array.get_len() == 1:
            return self.end_game()
        else:
            self.next_step()

    def send_step(self):
        self.users_array.set_min_value(self.auc_step)

    def end_game(self):
        return self.users_array.get_winner()


class User:
    def __init__(self, name, money, id):
        self.id = id
        self.name = name
        self.money = money
        self.min_value = 10
        self.bet = 0

    def get_bet(self):
        return input('Enter your bet: ')

    def set_min_value(self, value):
        self.min_value = value


class PlayerChain:
    def __init__(self, array_users):
        self.array = array_users

    def append(self):
        self.array.append(self.array.pop(0))

    def pop(self):
        return self.array.pop(0)

    def get_len(self):
        return len(self.array)

    def set_min_value(self, value):
        for i in self.array:
            i.set_min_value(value)

    def get_max_value(self):
        return self.array[-1].bet

    def get_winner(self):
        return self.array[0]
