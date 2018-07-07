'''
Created on 21 Jun 2018

@author: Elias
'''

class Effect:


    def __init__(self, name, etype, eff):
        self.name = name
        self.etype = etype
        self.eff = eff
        
    def t_damage(self, att, dmg):
        return att - dmg
    
    def t_gameplay(self):
        
    def t_conversational(self):