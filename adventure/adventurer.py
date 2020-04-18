class Adventurer:
    def __init__(self):
        """TODO: Initialises an adventurer object."""
        self.inv = []
        self.skill = 5
        self.will = 5

        self.add_skill = 0
        self.add_will = 0

    def get_inv(self):
        """TODO: Returns the adventurer's inventory."""
        return self.inv

    def get_skill(self):
        """TODO: Returns the adventurer's skill level. Whether this value is generated before or after item bonuses are applied is your decision to make."""
        return self.skill + self.add_skill

    def get_will(self):
        """TODO: Returns the adventurer's will power. Whether this value is generated before or after item bonuses are applied is your decision to make."""
        return self.will + self.add_will

    def take(self, item):
        """TODO: Adds an item to the adventurer's inventory."""
        self.inv.append(item)
        self.add_skill += item.get_skill()
        self.add_will += item.get_will()

    def check_self(self):
        """TODO: Shows adventurer stats and all item stats."""
        print()
        print("You are an adventurer, with a SKILL of %s and a WILL of %s." % (self.skill, self.will))
        print("You are carrying:")
        if self.inv:
            for item in self.inv:
                item.get_info()
        else:
            print("\nNothing.\n")
        
        print("With your items, you have a SKILL level of %s and a WILL power of %s." % (self.get_skill(), self.get_will()))