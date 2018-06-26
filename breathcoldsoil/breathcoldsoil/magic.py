'''
Created on 28 Mar 2018

@author: Elias
'''

class Spell:



    def __init__(self, name, damage, description, effects):
        self.name = name
        self.damage = int(damage)
        self.description = description
        self.effects = effects
        
    def __str__(self):
        return "{Name: {:s} Damage: {:d}p Description: {:s} Status effect: {:s}}".format(self.name, self.damage, self.description, self.effects)
        