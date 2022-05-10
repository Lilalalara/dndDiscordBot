import sqlite3 as sl

con = sl.connect('dndinfo.db')

# region used
# with con:
#    con.execute("""
#        CREATE TABLE WEAPONS(
#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#            name TEXT,
#            damage TEXT,
#            damage_type TEXT,
#            properties TEXT
#        );
#    """)

# with con:
#    con.execute("""
#        CREATE TABLE SPELLCARDS(
#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#            spell TEXT,
#            spellcard TEXT,
#            short_def TEXT
#        );
#    """)

# with con:
#    con.execute("""
#        CREATE TABLE FEATURES(
#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#            name TEXT,
#            class TEXT,
#           level TEXT,
#            description TEXT
#        );
#    """)

# endregion

#with con:
#    con.execute("""
#        CREATE TABLE CONDITIONS(
#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#            name TEXT,
#            desc TEXT
#        );
#    """)

with con:
    con.execute("""
        CREATE TABLE CONDITIONS(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            kind TEXT,
            description TEXT,
            
            
        )
    """)
