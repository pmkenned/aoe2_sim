#!/usr/bin/env python2

import os
import re

def getText(s):
  s = re.sub(r'<br />', ' ; ', s)
  s = re.sub(r'</?[^>]+>', '', s)
  s = re.sub(r'&nbsp;', ' ', s)
  s = re.sub(r'\n', '', s)
  s = re.sub(r'^\s+', '', s)
  s = re.sub(r'\s+$', '', s)
  return s

def getUnit(url, output):
  if not os.path.exists(output) or not os.path.isfile(output):
    os.system("wget '%s' -O ./data/%s" % (url, output))
  with open(output) as fh:
    line = fh.readline()
    inside_aside = False
    aside_field = ''
    while line:

      if "<aside" in line:
        inside_aside = True
      if "</aside" in line:
        inside_aside = False

      if inside_aside:

        if 'pi-title' in line:
          m = re.search(r'<h2.*>(?P<name>.*)</h2>', line)
          if m:
            name = m.groupdict()['name']
            print "===%s===" % name

        if 'pi-data-label' in line:
          m = re.search(r'<h3.*>(?P<aside_field>.*)</h3>', line)
          if m:
            aside_field = getText(line)
            # aside_field = m.groupdict()['aside_field']

        if not aside_field == '':
          if re.search('<div.*>', line):
            div_txt = getText(line)
            print "%s: '%s'" % (aside_field, div_txt)
            aside_field =''

      line = fh.readline()
  print ''

pages = [
  { 'url': 'https://ageofempires.fandom.com/wiki/Villager_(Age_of_Empires_II)',       'output': 'villager.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Militia_(Age_of_Empires_II)',        'output': 'militia.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Man-at-Arms',                        'output': 'man_at_arms.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Long_Swordsman_(Age_of_Empires_II)', 'output': 'long_swordsman.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Two-Handed_Swordsman',               'output': 'two_handed_swordsman.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Champion',                           'output': 'champion.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Spearman_(Age_of_Empires_II)',       'output': 'spearman.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Pikeman_(Age_of_Empires_II)',        'output': 'pikeman.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Halberdier_(Age_of_Empires_II)',     'output': 'halberdier.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Eagle_Scout',                        'output': 'eagle_scout.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Eagle_Warrior',                      'output': 'eagle_warrior.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Elite_Eagle_Warrior',                'output': 'elite_eagle_warrior.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Condottiero',                        'output': 'condottiero.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Huskarl_(Age_of_Empires_II)',        'output': 'huskarl.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Archer_(Age_of_Empires_II)',         'output': 'archer.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Crossbowman_(Age_of_Empires_II)',    'output': 'crossbowman.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Arbalest',                           'output': 'arbalest.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Skirmisher_(Age_of_Empires_II)',     'output': 'skirmisher.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Elite_Skirmisher',                   'output': 'elite_skirmisher.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Imperial_Skirmisher',                'output': 'imperial_skirmisher.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Cavalry_Archer_(Age_of_Empires_II)', 'output': 'cavalry_archer.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Heavy_Cavalry_Archer',               'output': 'heavy_cavalry_archer.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Hand_Cannoneer',                     'output': 'hand_cannoneer.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Slinger_(Age_of_Empires_II)',        'output': 'sliger.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Genitour_(mounted)',                 'output': 'genitour.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Scout_Cavalry_(Age_of_Empires_II)',  'output': 'scout_cavalry.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Light_Cavalry_(Age_of_Empires_II)',  'output': 'light_cavalry.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Hussar_(Age_of_Empires_II)',         'output': 'hussar.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Knight',                             'output': 'knight.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Cavalier',                           'output': 'cavalier.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Paladin',                            'output': 'paladin.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Camel',                              'output': 'camel.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Heavy_Camel',                        'output': 'heavy_camel.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Imperial_Camel',                     'output': 'imperial_camel.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Battle_Elephant',                    'output': 'battle_elephant.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Elite_Battle_Elephant',              'output': 'elite_battle_elephant.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Tarkan',                             'output': 'tarkan.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Battering_Ram',                      'output': 'battering_ram.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Capped_Ram',                         'output': 'capped_ram.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Siege_Ram',                          'output': 'siege_ram.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Mangonel',                           'output': 'mangonel.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Onager_(Age_of_Empires_II)',         'output': 'onager.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Siege_Onager',                       'output': 'siege_onager.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Scorpion',                           'output': 'scorpion.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Heavy_Scorpion',                     'output': 'heavy_scorpion.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Bombard_Cannon',                     'output': 'bombard_cannon.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Siege_Tower_(Age_of_Empires_II)',    'output': 'siege_tower.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Monk_(Age_of_Empires_II)',           'output': 'monk.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Missionary_(Age_of_Empires_II)',     'output': 'missionary.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Trade_Cart',                         'output': 'trade_cart.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Petard_(Age_of_Empires_II)',         'output': 'petard.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Trebuchet',                          'output': 'trebuchet.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Fishing_Ship_(Age_of_Empires_II)',   'output': 'fishing_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Transport_Ship_(Age_of_Empires_II)', 'output': 'transport_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Trade_Cog',                          'output': 'trade_cog.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Galley_(Age_of_Empires_II)',         'output': 'galley.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/War_Galley_(Age_of_Empires_II)',     'output': 'war_galley.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Galleon_(Age_of_Empires_II)',        'output': 'galleon.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Fire_Galley_(Age_of_Empires_II)',    'output': 'fire_galley.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Fire_Ship_(Age_of_Empires_II)',      'output': 'fire_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Fast_Fire_Ship',                     'output': 'fast_fire_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Demolition_Raft',                    'output': 'demolition_raft.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Demolition_Ship',                    'output': 'demolition_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Heavy_Demolition_Ship',              'output': 'heavy_demolition_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Cannon_Galleon',                     'output': 'cannon_galleon.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Elite_Cannon_Galleon',               'output': 'elite_cannon_galleon.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Longboat_(Age_of_Empires_II)',       'output': 'longboat.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Turtle_Ship',                        'output': 'turtle_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Caravel_(Age_of_Empires_II)',        'output': 'caravel.html'}
]

for d in pages:
    url = d['url']
    output = d['output']
    getUnit(url, output)
