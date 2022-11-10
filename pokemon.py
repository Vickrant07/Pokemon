# create a Pokemon
class Pokemon:
    def __init__(self, name, primary_type, max_hp)->None:
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp

    def __str__(self) -> str:
        return f"{self.name} ({self.primary_type}: {self.hp}/{self.max_hp})"


# feed them to increase health
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} now has {self.hp} HP.")
        else:
            print(f"{self.name} is Full")

# make them battle and decide for a winner
    def battle(self, other):
        print("Battle: ", self.name, other.name)
        result = self.typewheel(self.primary_type, other.primary_type)
        # depending on result, have effects
        if result == "lost":
            self.hp -= 10
            print(f"{self.name} lost and now has {self.hp} HP")
        elif result == "won":
            self.max_hp += 10
            print(f"{self.name} won and now has {self.max_hp} max HP")
        elif result == "tie":
            self.hp -= 10
            other.hp -= 10
            print(f"It was a tie, fight harder {self.name}, {other.name}")
        print(f"{self.name} fought {other.name} and {result} the match")

    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lost", 1: "won", -1:"tie"}
        # mapping between types and result conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}
        # implementing win-lose matrix
        wl_matrix = [
            [-1, 1, 0], # water
            [0, -1, 1], # fire
            [1, 0, -1], # grass
        ]
        # declare a winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]

# take a look at it
if __name__=='__main__':
    b = Pokemon(name="bulbasaur", primary_type="grass", max_hp=100)
    c = Pokemon(name="charmander", primary_type="fire", max_hp=150)
    b.battle(c)
    c.battle(b)
    b.battle(b)