import random as rd
class skill:
    def __init__(self, identity, possibility, species = "physics",  name = "EmptySkill", activation = False):
        self.name = name
        self.identity = identity
        self.possibility = possibility
        self.activation = activation
        self.species = species

    def detail(self):
        self.name = self.nameById(self.identity)
        if self.activation:
            print(self.name)
            #print(self.idById)

    def nameById(self, identity):
        switcherName = {
            0: "EmptySkill",
            1001: "Strength",
            1002: "MustKill",
            1003: "DoubleClick",
            1004: "SuckBlood",
            1005: "SneakAttack",
            1006: "SuddenAttack",
            1007: "NullPhysics",
            2001: "MagicHeart",
            2002: "MagicCrit",
            2003: "MagicDoubleClick",
            2004: "MagicForeSee",
            2005: "MagicFLuctuation",
            2006: "LightningStrike",
            2007: "NullMagic"
        }
        self.name = switcherName[identity]
        return (switcherName.get(identity))

    def possibilityById(self, identity):
        switcherName = {
            0: 100,
            1001: 50,
            1002: 50,
            1003: 50,
            1004: 80,
            1005: 50,
            1006: 50,
            1007: 0,
            2001: 50,
            2002: 50,
            2003: 50,
            2004: 80,
            2005: 50,
            2006: 50,
            2007: 0
        }
        self.possibility= switcherName[identity]
        return (switcherName.get(identity))


    def idById(self, identity, species = "physics"):
        if species is "physics":
            switcherId = {
                0: 0,
                1: 1001,
                2: 1002,
                3: 1003,
                4: 1004,
                5: 1005,
                6: 1006
            }
        else:
            switcherId = {
                0: 0,
                1: 2001,
                2: 2002,
                3: 2003,
                4: 2004,
                5: 2005,
                6: 2006
            }
        #print(identity,"idByID skill.idByID")
        self.identity = switcherId[identity]
        return switcherId[identity]


#strength = skill( 2003, 25, "", "",  True)
#strength.detail()
#print(strength.idById(2))
