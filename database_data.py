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
    (4, 'mass_heal', 'A flood of healing energy flows from you into injured creatures around you. You restore up to 700 hit points, divided as you choose among any number of creatures that you can see within range. Creatures healed by this spell are also cured of all diseases and any effect making them blinded or deafened. This spell has no effect on undead or constructs.', '60ft range, restore up to 700 HP'),
    (5, "fire_bolt", "You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn’t being worn or carried.", "120ft range, ranged spell attack, 1d10 fire damage"),
    (6, "friends", "For the duration, you have advantage on all Charisma checks directed at one creature of your choice that isn’t hostile toward you. When the spell ends, the creature realizes that you used magic to influence its mood and becomes hostile toward you. A creature prone to violence might attack you. Another creature might seek retribution in other ways (at the DM’s discretion), depending on the nature of your interaction with it.", "self range, concentration, up to 1 minute, advantage on Charisma Checks"),
    (7, "frostbite" "You cause numbing frost to form on one creature that you can see within range. The target must make a Constitution saving throw. On a failed save, the target takes 1d6 cold damage, and it has disadvantage on the next weapon attack roll it makes before the end of its next turn.", "60ft range, Constitution saving throw, 1d6 cold damage + disadvantage on next attack roll"),
]
#with con:
 #   con.executemany(sql_spellcards, data_spellcards)


sql_cond = 'INSERT INTO CONDITIONS (id, name, desc) values(?, ?, ?)'
data_cond = [
    (1, 'blinded', 'A blinded creature can not see and automatically fails any ability check that requires sight. \nAttack rolls against the creature have advantage, and the creatures attack rolls have disadvantage.'),
    (2, 'charmed', 'A charmed creature can not attack the charmer or target the charmer with harmful abilities or magical effects. \nThe charmer has advantage on any ability check to interact socially with the creature.'),
    (3, 'deafened', 'A deafened creature can not hear and automatically fails any ability check that requires hearing.'),
    (4, 'exhaustion', 'Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effects description.\n1 - Disadvantage on ability checks\n2 - Speed halved\n3 - Disadvantage on attack rolls and saving throws\n4 - Hit point maximum halved\n5 - Speed reduced to 0\n6 - Death\n    "If an already exhausted creature suffers another effect that causes exhaustion, its current level of exhaustion increases by the amount specified in the effects description. \nA creature suffers the effect of its current level of exhaustion as well as all lower levels. For example, a creature suffering level 2 exhaustion has its speed halved and has disadvantage on ability checks. An effect that removes exhaustion reduces its level as specified in the effects description, with all exhaustion effects ending if a creatures exhaustion level is reduced below 1. Finishing a long rest reduces a creatures exhaustion level by 1, provided that the creature has also ingested some food and drink.'),
    (5, 'frightened', 'A frightened creature has disadvantage on ability checks and attack rolls while the source of its fear is within line of sight.\nThe creature can not willingly move closer to the source of its fear.'),
    (6, 'grappled', 'A grappled creatures speed becomes 0, and it can not benefit from any bonus to its speed. \nThe condition ends if the grappler is incapacitated. \nThe condition also ends if an effect removes the grappled creature from the reach of the grappler or grappling effect.'),
    (7, 'incapacitated', 'An incapacitated creature can not take actions or reactions.'),
    (8, 'invisible', 'An invisible creature is impossible to see without the aid of magic or a special sense. For the purpose of hiding, the creature is heavily obscured. The creatures location can be detected by any noise it makes or any tracks it leaves. \nAttack rolls against the creature have disadvantage, and the creatures attack rolls have advantage.'),
    (9, 'paralyzed', 'A paralyzed creature is incapacitated and can not move or speak.\nThe creature automatically fails Strength and Dexterity saving throws.\nAttack rolls against the creature have advantage.\nAny attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.'),
    (10, 'petrified', 'A petrified creature is transformed, along with any nonmagical object it is wearing or carrying, into a solid inanimate substance (usually stone). Its weight increases by a factor of ten, and it ceases aging.\nThe creature is incapacitated can’t move or speak, and is unaware of its surroundings.\nAttack rolls against the creature have advantage.\nThe creature automatically fails Strength and Dexterity Saving Throws.\nThe creature has Resistance to all damage.\nThe creature is immune to poison and disease, although a poison or disease already in its system is suspended, not neutralized.\n'),
    (11, 'poisoned', 'A poisoned creature has disadvantage on attack rolls and ability checks.'),
    (12, 'prone', 'A prone creatures only movement option is to crawl, unless it stands up and thereby ends the condition.\nThe creature has disadvantage on attack rolls.\nAn attack roll against the creature has advantage if the attacker is within 5 feet of the creature. Otherwise, the attack roll has disadvantage.'),
    (13, 'restrained', ' A restrained creatures speed becomes 0, and it can not benefit from any bonus to its speed.\nAttack rolls against the creature have advantage, and the creatures attack rolls have disadvantage.\nThe creature has disadvantage on Dexterity saving throws.'),
    (14, 'stunned', 'A stunned creature is incapacitated, can not move, and can speak only falteringly. \nThe creature automatically fails Strength and Dexterity saving throws.\nAttack rolls against the creature have advantage.'),
    (15, 'unconscious', 'An unconscious creature is incapacitated, can not move or speak, and is unaware of its surroundings.\nThe creature drops whatever it is holding and falls prone.\nThe creature automatically fails Strength and Dexterity saving throws.\nAttack rolls against the creature have advantage.\nAny attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.')
]
with con:
    con.executemany(sql_cond, data_cond)
