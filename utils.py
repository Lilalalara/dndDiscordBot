import random
import re
import sqlite3 as sl


def roll_all_dice(expr):
    is_valid_overall = re.match(r"^\d*[d]\d+.*", expr)
    if is_valid_overall:
        d = expr.find('d')
        number_dice = expr[:d]
        if number_dice == '':
            number_dice = 1
        else:
            number_dice = int(number_dice)
        # 2d4
        only_roll = re.match(r"^\d*[d]\d+$", expr)
        if only_roll:
            number_sides = int(expr[d + 1:])
            dice = roll_dice(number_dice, number_sides)
            return f"You rolled: {'  '.join(dice)}  sum: {sum(list_to_int(dice))}"

        # 1d4+2
        roll_with_modifier = re.match(r"^\d*[d]\d+[+-]\d+$", expr)
        if roll_with_modifier:
            plus = expr.find('+')
            if plus == -1:
                minus = expr.find('-')
                number_sides = int(expr[d + 1:minus])
                mod = -int(expr[minus + 1:])
            else:
                number_sides = int(expr[d + 1:plus])
                mod = int(expr[plus + 1:])

            dice = roll_dice(number_dice, number_sides)
            return f"You rolled: {'  '.join(dice)}  mod: {mod}  sum: {sum(list_to_int(dice))+mod}"

        # 1d4kh1 2d4dl1
        roll_with_drop_keep = re.match(r"^\d*[d]\d+[kd][hl]\d+$", expr)
        if roll_with_drop_keep:
            kh, kl, dh, dl = expr.find('kh'), expr.find('kl'), expr.find('dh'), expr.find('dl')
            if kh != -1:
                number_sides = int(expr[d + 1:kh])
                keep_high = int(expr[kh + 2:])
                dice = roll_dice(number_dice, number_sides)
                final_rolls, extra_rolls = keep_drop(dice, 'h', number_dice - keep_high)
            elif kl != -1:
                number_sides = int(expr[d + 1:kl])
                keep_low = int(expr[kl + 2:])
                dice = roll_dice(number_dice, number_sides)
                final_rolls, extra_rolls = keep_drop(dice, 'l', number_dice - keep_low)
            elif dh != -1:
                number_sides = int(expr[d + 1:dh])
                drop_high = int(expr[dh + 2:])
                dice = roll_dice(number_dice, number_sides)
                final_rolls, extra_rolls = keep_drop(dice, 'l', drop_high)
            elif dl != -1:
                number_sides = int(expr[d + 1:dl])
                drop_low = int(expr[dl + 2:])
                dice = roll_dice(number_dice, number_sides)
                final_rolls, extra_rolls = keep_drop(dice, 'h', drop_low)
            return f"You rolled: {'  '.join(final_rolls)} {' '.join(extra_rolls)}  sum: {sum(list_to_int(final_rolls))}"
    else:
        return "Not a valid roll!"


def roll_dice(number_dice, number_sides):
    dice = [
        str(random.choice(range(1, number_sides + 1)))
        for _ in range(number_dice)
    ]
    return dice


def list_to_int(string_list):
    int_list = []
    for x in string_list:
        int_list.append(int(x))
    return int_list


def keep_drop(dice_rolls, high_low, mod):
    new_rolls = dice_rolls
    extra = []
    for _ in range(mod):
        if high_low == 'h':
            mini = min(dice_rolls)
            new_rolls.remove(mini)
            extra.append(f"({mini})")
        if high_low == 'l':
            maxi = max(dice_rolls)
            new_rolls.remove(maxi)
            extra.append(f"({maxi})")
    return new_rolls, extra


def get_weapons(weapon_name):
    con = sl.connect('dndinfo.db')
    with con:
        data = con.execute(f"SELECT * FROM WEAPONS WHERE name == '{weapon_name.lower()}'")
        row = data.fetchone()
        if row is None:
            return None
        else:
            response = f"**{row[1].replace('_', ' ').title()}** \n >>> Damage: {row[2]} {row[3]} \nProperties: {row[4]}"
            return response


def get_all_weapons():
    con = sl.connect('dndinfo.db')
    with con:
        data = con.execute(f"SELECT name FROM WEAPONS")
        rows = data.fetchall()
        resp = ""
        for r in rows:
            resp += r[0].replace('_', ' ').title() + "\n"
    return resp


def save_new_weapons(name, damage, damage_type, properties):
    con = sl.connect('dndinfo.db')

    ids = con.execute("SELECT max(id) FROM WEAPONS").fetchone()
    new_id = ids[0] + 1

    sql = 'INSERT INTO WEAPONS (id, name, damage, damage_type, properties) values(?, ?, ?, ?, ?)'
    data = [(new_id, f'{name}', f'{damage}', f'{damage_type}', f'{properties}')]
    with con:
        con.executemany(sql, data)


def get_spellcard(spell_name):
    con = sl.connect('dndinfo.db')
    with con:
        data = con.execute(f"SELECT * FROM SPELLCARDS WHERE spell == '{spell_name.lower()}'")
        row = data.fetchone()
        if row is None:
            return None
        else:
            response = f"**{row[1].replace('_', ' ').title()}** \n > {row[3]} \n\n{row[2]}"
            return response


def get_all_spells():
    con = sl.connect('dndinfo.db')
    with con:
        data = con.execute(f"SELECT spell FROM SPELLCARDS")
        rows = data.fetchall()
        resp = ""
        for r in rows:
            resp += r[0].replace('_', ' ').title() + "\n"
    return resp


def save_new_spellcard(spell, spellcard, short_def):
    con = sl.connect('dndinfo.db')

    ids = con.execute("SELECT max(id) FROM SPELLCARDS").fetchone()
    new_id = ids[0] + 1

    sql = 'INSERT INTO SPELLCARDS (id, spell, spellcard, short_def) values(?, ?, ?, ?)'
    data = [(new_id, f'{spell}', f'{spellcard}', f'{short_def}')]
    with con:
        con.executemany(sql, data)


def get_condition(cond_name):
    con = sl.connect('dndinfo.db')
    with con:
        data = con.execute(f"SELECT * FROM CONDITIONS WHERE name == '{cond_name.lower()}'")
        row = data.fetchone()
        if row is None:
            return None
        else:
            response = f"**{row[1].replace('_', ' ').title()}** \n >>> {row[2]}"
            return response


def get_all_conditions():
    con = sl.connect('dndinfo.db')
    with con:
        data = con.execute(f"SELECT name FROM CONDITIONS")
        rows = data.fetchall()
        resp = ""
        for r in rows:
            resp += r[0].replace('_', ' ').title() + "\n"
    return resp
