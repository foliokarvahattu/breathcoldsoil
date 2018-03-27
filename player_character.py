'''
Created on 26.2.2018

@author: Elias
'''
import random

class Player_Character:

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mana = 100
        self.spells = {}
        self.inventory = {}
        self.stats = {'STR': 1,'CHR': 1, 'INT': 1, 'PER': 1, 'LCK': 1}
        
    def roll_stats(self):
        a = 25
        dice = random.randint(1, a)
        self.stats['STR'] = dice
        a = a - dice
        if a <= 0:
            a = 1
        dice = random.randint(1, a)
        self.stats['INT'] = dice
        a = a - dice
        if a <= 0:
            a = 1
        dice = random.randint(1, a)
        self.stats['CHR'] = dice
        a = a - dice
        if a <= 0:
            a = 1
        dice = random.randint(1, a)
        self.stats['PER'] = dice
        a = a - dice
        if a <= 0:
            a = 1
        self.stats['LCK'] = a
        
    def add_spell(self, spellname, spelleffect):
        a = spelleffect[0]
        b = spelleffect[1]
        self.spells[spellname] = [a,b]
    def spell_list(self):
        for i in self.spells:
            print("Name: {:s} Damage: {:d}p Effect: {:s}".format(i, self.spells[i][0], self.spells[i][1]))
        
player = Player_Character('Pasi')
player.roll_stats()
print(player.stats)
player.add_spell('Fart of Doom', [10,'Fart so much everyone dies'])
player.add_spell('LOVE', [0,'Give everyone love <3'])
player.spell_list()