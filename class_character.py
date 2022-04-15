""" Character <- Friend, Enemy, MainCharacter """


class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.phrases = set()
        self.question = None

    def set_conservation(self, phrase1, phrase2):
        self.phrases[phrase1] = phrase2

    def set_question(self, question):
        self.question = question


class Friend(Character):
    def __init__(self, name, description):
        super(Friend, self).__init__(name, description)
        self.inducement = None
        self.help = None

    def set_inducement(self, inducement):
        self.inducement = inducement

    def set_assistance(self, help):
        self.help = help


class Enemy(Character):
    def __init__(self, name, description):
        super(Enemy, self).__init__(name, description)
        self.power = None
        self.weakness = None

    def set_power(self, power):
        self.power = power

    def set_weakness(self, weakness):
        self.weakness = weakness


class MainCharacter(Character):
    def __init__(self, name, description):
        super(MainCharacter, self).__init__(name, description)
        self.lives = 100
        self.energy = 100
        self.balance = 43  # tram - 8, coffee - 35
        self.backpack = []

    def remove_live(self, remove):
        self.lives -= remove

    def add_live(self, add):
        self.lives += add

    def remove_energy(self, remove):
        self.energy -= remove

    def add_energy(self, add):
        self.energy += add

    def add_balance(self, add):
        self.balance += add

    def remove_balance(self, remove):
        self.balance += remove

    def take_thing(self, thing):
        self.backpack.append(thing)
