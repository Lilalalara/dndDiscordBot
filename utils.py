import sqlite3 as sl


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
