import sqlite3 as sl

con = sl.connect('dndinfo.db')

sql_weapons = 'INSERT INTO WEAPONS (id, name, damage, damage_type, properties) values(?, ?, ?, ?, ?)'
data_weapons = [
    (1, 'battleaxe', '1d8', 'slashing', 'versatile(1d10)'),
    (2, 'blowgun', '1', 'piercing', 'ammunition(25/100ft), loading'),
    (3, 'club', '1d4', 'bludgeoning', 'light'),
    (4, 'dagger', '1d4', 'piercing', 'finesse, light, thrown(20/60ft)'),
    (5, 'dart', '1d4', 'piercing', 'finesse, thrown(20/60ft)'),
    (6, 'flail', '1d8', 'bludgeoning', ''),
    (7, 'glaive', '1d10', 'slashing', 'heavy, reach, two-handed'),
    (8, 'greataxe', '1d12', 'slashing', 'heavy, two-handed'),
    (9, 'greatclub', '1d8', 'bludgeoning', 'two-handed'),
    (10, 'greatsword', '2d6', 'slashing', 'heavy, two-handed'),
    (11, 'halberd', '1d10', 'slashing', 'heavy, reach, two-handed'),
    (12, 'hand_crossbow', '1d6', 'piercing', 'light, loading, ammunition(30/120ft)'),
    (13, 'javelin', '1d6', 'piercing', 'thrown(30/120ft)'),
    (14, 'lance', '1d12', 'piercing', 'reach, special'),
    (15, 'light_crossbow', '1d8', 'piercing', 'two-handed, loading, ammunition(80/320ft)'),
    (16, 'light_hammer', '1d4', 'bludgeoning', 'light, thrown(20/60ft)'),
    (17, 'longbow', '1d8', 'piercing', 'heavy, tow-handed, ammunition(150/600ft)'),
    (18, 'longsword', '1d8', 'slashing', 'versatile(1d10)'),
    (19, 'mace', '1d6', 'bludgeoning', ''),
    (20, 'maul', '2d6', 'bludgeoning', 'heavy, tow-handed'),
    (21, 'morningstar', '1d8', 'piercing', ''),
    (22, 'net', 'restrained', '', 'thrown(5/15ft)'),
    (23, 'pike', '1d10', 'piercing', 'heavy, reach, two-handed'),
    (24, 'quarterstaff', '1d6', 'bludgeoning', 'versatile(1d8)'),
    (25, 'rapier', '1d8', 'piercing', 'finesse'),
    (26, 'scimitar', '1d6', 'slashing', 'finesse, light'),
    (27, 'shortbow', '1d6', 'piercing', 'ammunition(80/320ft), two-handed'),
    (28, 'shortsword', '1d6', 'piercing', 'finesse, light'),
    (29, 'sickle', '1d4', 'slashing', 'light'),
    (30, 'sling', '1d4', 'bludgeoning', 'ammunition(30/120ft)'),
    (31, 'spear', '1d6', 'piercing', 'thrown(20/60ft), versatile(1d8)'),
    (32, 'trident', '1d6', 'piercing', 'thrown(20/60ft), versatile(1d8)'),
    (33, 'war_pick', '1d8', 'piercing', ''),
    (34, 'warhammer', '1d8', 'bludgeoning', 'versatile(1d10)'),
    (35, 'whip', '1d4', 'slashing', 'finesse, reach'),
    (36, 'handaxe', '1d6', 'slashing', 'light, thrown(20/60ft)'),
    (37, 'heavy_crossbow', '1d10', 'piercing', 'ammunition(100/400ft), heavy, loading, two-handed'),
]

# with con:
#   con.executemany(sql_weapons, data_weapons)


sql_spellcards = 'INSERT INTO SPELLCARDS (id, spell, spellcard, short_def) values(?, ?, ?, ?)'
data_spellcards = [
    (1, 'fireball', 'A bright streak flashes from your pointing finger to a point you choose within range then blossoms with a low roar into an explosion of flame. Each creature in a 20-foot radius must make a Dexterity saving throw. A target takes 8d6 fire damage on a failed save, or half as much damage on a successful one. The fire spreads around corners. It ignites flammable objects in the area that aren’t being worn or carried.', '150ft range, 20ft radius, Dexterity saving throw, 8d6 fire damage'),
    (2, 'chromatic_orb', 'You hurl a 4-inch-diameter sphere of energy at a creature that you can see within range. You choose acid, cold, fire, lightning, poison, or thunder for the type of orb you create, and then make a ranged spell attack against the target. If the attack hits, the creature takes 3d8 damage of the type you chose.', '90ft range, ranged spell attack, 3d8 of chosen damage'),
    (3, 'chill_touch', 'You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage, and it can’t regain hit points until the start of your next turn. Until then, the hand clings to the target. If you hit an undead target, it also has disadvantage on attack rolls against you until the end of your next turn.', '120ft range, ranged spell attack, 1d8 necrotic damage, disadvantage on attacking you'),
    (4, 'mass_heal', 'A flood of healing energy flows from you into injured creatures around you. You restore up to 700 hit points, divided as you choose among any number of creatures that you can see within range. Creatures healed by this spell are also cured of all diseases and any effect making them blinded or deafened. This spell has no effect on undead or constructs.', '60ft range, restore up to 700 HP')
]
with con:
    con.executemany(sql_spellcards, data_spellcards)
