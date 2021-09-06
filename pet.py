import random as rd
from skill import skill as sk

class pet:
    def __init__(self, name, identity, skill = []):
        self.name = name
        self.identity = identity
        self.skill = skill
        self.skill_num_rand = rd.randrange(4 + 1)
        self.skill_num = 0
        self.skill_blank_cnt = 0
        self.species = "physics"

    def skill_init(self, skill_num):
        print("pet %s skill_num_random is %d" %(self.name, self.skill_num_rand))
        self.skill = []
        self.skill_num = 0
        for index in range(self.skill_num_rand):
            skillTemp = sk( index, 25, self.species,  "", True )
            #print("before skill id assignmented by species %d" %index)
            skillTemp.idById(index)
            #print("after skill id assignmented by species %d" %skillTemp.identity)
            skillTemp.nameById(skillTemp.identity)
            skillTemp.possibilityById(skillTemp.identity)
            #print("skill sort index %d name is %s" %(index, skillTemp.name))
            if rd.randrange(100) < skillTemp.possibility:
                self.skill_num += 1
                self.skill.append(skillTemp)
        print("pet %s skill number is %d" %(self.name, self.skill_num))
        for i in self.skill:
            print(i.name)

        if skill_num is 0:
            self.skill_blank_cnt += 1
            print("you get blank skill count is %d" %self.skill_blank_cnt)
        else:
            self.skill_blank_cnt = 0

    def fuction_choice(self):
        self.state = input("function choice:")
        print("your fuction choice is %s" %self.state)
        switchState = {
            "init": self.skill_init(vampire.skill_num)
        }


vampire = pet("vampire", 65)
vampire.skill_init(vampire.skill_num)
vampire.fuction_choice()
