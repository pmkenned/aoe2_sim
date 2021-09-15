#!/usr/bin/env python3

import subprocess
import sys
import os
import re

verbose = True

def getText(s):
    s = re.sub(r'<br/>', ' ; ', s)
    s = re.sub(r'</?[^>]+>', '', s)
    s = re.sub(r'&nbsp;', ' ', s)
    s = re.sub(r'\n', '', s)
    s = re.sub(r'^\s+', '', s)
    s = re.sub(r'\s+$', '', s)
    return s

def getPages(pages):

    ps = dict()

    for page in pages:
        if verbose:
            sys.stderr.write('getting %s...' % page['filename'])
            sys.stderr.flush()
        if os.path.isfile('./data/%s' % page['filename']):
            if verbose:
                sys.stderr.write(' skipping\n')
            continue
        else:
            if verbose:
                sys.stderr.write('\n')
        ps[page['filename']] = subprocess.Popen(['wget', '-q', '-O', '-', page['url']], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    for filename, p in ps.items():
        out, err = p.communicate()
        out = out.decode()
        os.makedirs('./data/', exist_ok=True)
        with open('./data/%s' % filename, 'w', encoding='utf-8') as fh:
            fh.write(out)
        if verbose:
            sys.stderr.write('got %s)\n' % filename)


def getUnit(filename):

    with open(filename, encoding='utf-8') as fh:

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
                        print("===%s===" % name)

                if 'pi-data-label' in line:
                    m = re.search(r'<h3.*>(?P<aside_field>.*)</h3>', line)
                    if m:
                        aside_field = getText(line)
                        # aside_field = m.groupdict()['aside_field']

                if not aside_field == '':
                    if re.search('<div.*>', line):
                        div_txt = getText(line)
                        print("%s: '%s'" % (aside_field, div_txt))
                        aside_field =''

            line = fh.readline()

    print('')


pages = [
  { 'url': 'https://ageofempires.fandom.com/wiki/Villager_(Age_of_Empires_II)',       'filename': 'villager.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Militia_(Age_of_Empires_II)',        'filename': 'militia.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Man-at-Arms',                        'filename': 'man_at_arms.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Long_Swordsman_(Age_of_Empires_II)', 'filename': 'long_swordsman.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Two-Handed_Swordsman',               'filename': 'two_handed_swordsman.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Champion',                           'filename': 'champion.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Spearman_(Age_of_Empires_II)',       'filename': 'spearman.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Pikeman_(Age_of_Empires_II)',        'filename': 'pikeman.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Halberdier_(Age_of_Empires_II)',     'filename': 'halberdier.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Eagle_Scout_(Age_of_Empires_II)',    'filename': 'eagle_scout.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Eagle_Warrior',                      'filename': 'eagle_warrior.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Elite_Eagle_Warrior',                'filename': 'elite_eagle_warrior.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Condottiero',                        'filename': 'condottiero.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Huskarl_(Age_of_Empires_II)',        'filename': 'huskarl.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Archer_(Age_of_Empires_II)',         'filename': 'archer.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Crossbowman_(Age_of_Empires_II)',    'filename': 'crossbowman.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Arbalester',                         'filename': 'arbalest.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Skirmisher_(Age_of_Empires_II)',     'filename': 'skirmisher.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Elite_Skirmisher',                   'filename': 'elite_skirmisher.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Imperial_Skirmisher',                'filename': 'imperial_skirmisher.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Cavalry_Archer_(Age_of_Empires_II)', 'filename': 'cavalry_archer.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Heavy_Cavalry_Archer',               'filename': 'heavy_cavalry_archer.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Hand_Cannoneer',                     'filename': 'hand_cannoneer.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Slinger_(Age_of_Empires_II)',        'filename': 'sliger.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Genitour_(mounted)',                 'filename': 'genitour.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Scout_Cavalry_(Age_of_Empires_II)',  'filename': 'scout_cavalry.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Light_Cavalry_(Age_of_Empires_II)',  'filename': 'light_cavalry.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Hussar_(Age_of_Empires_II)',         'filename': 'hussar.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Knight',                             'filename': 'knight.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Cavalier',                           'filename': 'cavalier.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Paladin',                            'filename': 'paladin.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Camel_Rider_(Age_of_Empires_II)',    'filename': 'camel.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Heavy_Camel_Rider',                  'filename': 'heavy_camel.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Imperial_Camel_Rider',               'filename': 'imperial_camel.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Battle_Elephant',                    'filename': 'battle_elephant.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Elite_Battle_Elephant',              'filename': 'elite_battle_elephant.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Tarkan',                             'filename': 'tarkan.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Battering_Ram',                      'filename': 'battering_ram.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Capped_Ram',                         'filename': 'capped_ram.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Siege_Ram',                          'filename': 'siege_ram.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Mangonel',                           'filename': 'mangonel.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Onager_(Age_of_Empires_II)',         'filename': 'onager.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Siege_Onager',                       'filename': 'siege_onager.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Scorpion',                           'filename': 'scorpion.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Heavy_Scorpion',                     'filename': 'heavy_scorpion.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Bombard_Cannon',                     'filename': 'bombard_cannon.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Siege_Tower_(Age_of_Empires_II)',    'filename': 'siege_tower.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Monk_(Age_of_Empires_II)',           'filename': 'monk.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Missionary_(Age_of_Empires_II)',     'filename': 'missionary.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Trade_Cart',                         'filename': 'trade_cart.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Petard_(Age_of_Empires_II)',         'filename': 'petard.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Trebuchet',                          'filename': 'trebuchet.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Fishing_Ship_(Age_of_Empires_II)',   'filename': 'fishing_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Transport_Ship_(Age_of_Empires_II)', 'filename': 'transport_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Trade_Cog',                          'filename': 'trade_cog.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Galley_(Age_of_Empires_II)',         'filename': 'galley.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/War_Galley_(Age_of_Empires_II)',     'filename': 'war_galley.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Galleon_(Age_of_Empires_II)',        'filename': 'galleon.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Fire_Galley_(Age_of_Empires_II)',    'filename': 'fire_galley.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Fire_Ship_(Age_of_Empires_II)',      'filename': 'fire_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Fast_Fire_Ship',                     'filename': 'fast_fire_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Demolition_Raft',                    'filename': 'demolition_raft.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Demolition_Ship',                    'filename': 'demolition_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Heavy_Demolition_Ship',              'filename': 'heavy_demolition_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Cannon_Galleon',                     'filename': 'cannon_galleon.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Elite_Cannon_Galleon',               'filename': 'elite_cannon_galleon.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Longboat_(Age_of_Empires_II)',       'filename': 'longboat.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Turtle_Ship',                        'filename': 'turtle_ship.html'},
  { 'url': 'https://ageofempires.fandom.com/wiki/Caravel_(Age_of_Empires_II)',        'filename': 'caravel.html'}
]

getPages(pages)

for d in pages:
    url = d['url']
    filename = d['filename']
    getUnit("./data/%s" % filename)
