#!/usr/bin/env python2

# Collect relics first
# Build walls
# Create strong economy
# Explore
# 

# strategies:
#  dark age rush
#  feudal rush
#  monk rush
#  fast castle

# game state:
#   time into game
#   current age
#   amount of each resource collected
#   amount of each resource left on the map
#   which research has been done
#   list of units and their current state
#   list of buildings and their current state
#   which buildings have been built

# formulas:
#   villager-seconds required to produce a given amount of a given resource

# List of armor classes
#   Unit classes
#       Infantry
#       Spearman
#       Eagle Warrior
#       Condottiero
#       Archer
#       Cavalry Archer
#       Camel
#       War elephant
#       Mameluke
#       Gunpowder unit
#       Siege weapon
#       Ram
#       Monk
#       Ship
#       Fishing Ship
#       Turtle Ship
#       Unique Unit
#   Building classes
#       Building
#       Standard building
#       Stone defense
#       Wall and gate
#       Castle

# Civilizations:
#     Aztecs
#     Britons
#     Byzantines
#     Celts
#     Chinese
#     Franks
#     Goths
#     Huns
#     Japanese
#     Koreans
#     Mayans
#     Mongols
#     Persians
#     Saracens
#     Spanish
#     Teutons
#     Turks
#     Vikings
# 
# Dark Age Buildings:
#     Barracks
#     Dock
#     Outpost
#     Palisade Wall
#     House
#     Town Center (cannot create)
#     Mining Camp
#     Lumber Camp
#     Mill
#     Farm
# 
# Dark Age Research:
#     Loom
#     Feudal Age
# 
# Dark Age Units:
#     Militia
#     Fishing Ship
#     Villager
# 
# Feudal Age Buildings:
#     Archery Range (requires Barracks)
#     Stables (requires Barracks)
#     Fish Trap (requires Dock)
#     Watch Tower
#     Gate
#     Stone Wall
#     Blacksmith
#     Market (requires Mill)
# 
# Feudal Age Research:
#     // TODO
# 
# Feudal Age Units :
#     // TODO
# 
# Castle Age Buildings:
#     Guard Tower
#     Fortified Wall
#     Monastary
#     Castle
#     Town Center
#     Siege Workshop
#     University
# 
# Castle Age Research:
#     // TODO
# 
# Castle Age Units:
#     // TODO
# 
# Imperial Age Buildings:
#     Wonder
#     Keep
#     Bombard Tower
# 
# Imperial Age Research:
#     // TODO
# 
# Imperial Age Units:
#     // TODO
# 
# 
# 

class Building:
    def __init__(self, name):
        self.name = name

class Barracks(Building):
    def __init__(self, name):
        Building.__init__(self, name)

x = Barracks('foo')
print x.name
