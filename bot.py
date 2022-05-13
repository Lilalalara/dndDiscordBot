import os
import random

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from dotenv import load_dotenv
from utils import get_weapons, get_all_weapons, save_new_weapons, get_spellcard, get_all_spells, save_new_spellcard, \
    get_condition, get_all_conditions, roll_all_dice, get_all_races, get_detail_race, get_overview_race

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!', help_command=None)


@bot.command()
async def help(ctx):
    await ctx.send(
        "\n**----- All available commands -----**\n\n"
        "**\!help**  Returns this message\n \n"
        "**\!race overview <race>** Returns an overview of the chosen race. *(short !race o)\n"
        "**\!race detail <race>** Returns detailed information on the chosen race. *(short !race d)\n"
        "**\!race ls** Returns a list of all races currently in the system\n\n"
        "**\!damage <weapon>**  Returns damage dice, damage type, and properties of the weapon *(short !dmg)*\n"
        "**\!dmg ls** Returns a list of all weapons currently in the system\n"
        "**\!spellcard <spell>** Returns a short summary and the spellcard of the spell *(short !spell)*\n"
        "**\!spell ls** Returns a list of all spells currently in the system\n"
        "**\!condition <condition>** Returns a short summary of the condition*(short !con)*\n"
        "**\!con ls**  Returns a list of all conditions\n\n"
        "**\!roll <xdx>** Simulates rolling the dice *(short !r)*\n"
        " -> add modifiers to your rolls by using **+** or **-** \n"
        " -> keep the highest or lowest or drop the highest or lowest by using **kh<number>** or **kl<number>** or **dh<number>** or **dl<number>**\n\n"
        "--- **For Admins when wanting to add new stuff** ---  *Always(!) put every element in quotation marks.*\n"
        "**\!addweapon '<name>' '<damage>' '<damage_type>' '<properties>'** Adds a new instance of a weapon to the database. *(short !addw)*\n"
        "**\!addspellcard '<spell>' '<spellcard>' '<short_description>'** Adds a new instance of a spell to the database.  *(short !adds)*")


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99', hidden=True)
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'Cool. Cool cool cool cool cool cool cool, \nno doubt no doubt no doubt no doubt.'
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='fireball', description="Send fireball gif!", hidden=True)
async def explode(ctx):
    await ctx.send(file=discord.File("gifs/house-explosion.gif"))


@bot.command(name='roll', aliases=['r'], help='Simulates rolling dice.')
async def roll(ctx, roll_input):
    await ctx.send(roll_all_dice(roll_input))


@bot.command(name='damage', aliases=['dmg'], help='Tells you the damage of the weapon')
async def damage(ctx, *args):
    weapon = '_'.join(args)
    if weapon is None:
        damage_res = "A lot of damage! (You need to tell me the weapon! :person_facepalming:)"
    elif weapon == "ls":
        damage_res = get_all_weapons()
    else:
        damage_res = get_weapons(weapon)
    if damage_res is None:
        damage_res = f"No damage! ({weapon} is not a weapon! :person_shrugging:)"
    await ctx.send(damage_res)


@bot.command(name='spellcard', aliases=['spell'], help='Gives you the spellcard of the spell')
async def spellcard(ctx, *args):
    spell = '_'.join(args)
    if spell is None:
        spell_res = "You cast fireball! (You need to tell me the spell! :person_facepalming:)"
    elif spell == "ls":
        spell_res = get_all_spells()
    else:
        spell_res = get_spellcard(spell)
    if spell_res is None:
        spell_res = f"I do not know! ({spell} is not a spell! :person_shrugging:)"

    await ctx.send(spell_res)


@bot.command(name='condition', aliases=['con'], help='Tells you what a condition means')
async def condition(ctx, con):
    if con is None:
        con_res = "You need to tell me the condition! :person_facepalming:"
    elif con == "ls":
        con_res = get_all_conditions()
    else:
        con_res = get_condition(con)
    if con_res is None:
        con_res = f"I do not know! ({con} is not a condition! :person_shrugging:)"

    await ctx.send(con_res)


@bot.command(name='race')
async def races(ctx, how, *args):
    if how == 'ls':
        race_res = get_all_races()
    elif (how == 'detail' or how == 'd') and args is not None:
        race = '_'.join(args)
        race_res = get_detail_race(race)
    elif (how == 'overview' or how == 'o') and args is not None:
        race = '_'.join(args)
        race_res = get_overview_race(race)
    else:
        race_res = "This is not how you use this command! :person_facepalming:"
    if race_res is None:
        race_res = f"I do not know! ({race} is not a race! :person_shrugging:)"

    await ctx.send(race_res)


@bot.command(name='addweapon', aliases=['addw'], hidden=True)
@has_permissions(administrator=True)
async def add_weapon(ctx, name, damage, damage_type, properties):
    if get_weapons(name.replace(' ', '_')) is None:
        save_new_weapons(name.lower().replace(' ', '_'), damage, damage_type, properties)
        await ctx.send(f"You added **{name}** to the database!:thumbsup:")
    else:
        await ctx.send(f"**{name.title()}** already exists in the database!")


@bot.command(name='addspellcard', aliases=['adds'], hidden=True)
@has_permissions(administrator=True)
async def add_spellcard(ctx, spell, spellcard, short_def):
    if get_spellcard(spell.replace(' ', '_')) is None:
        save_new_spellcard(spell.lower().replace(' ', '_'), spellcard, short_def)
        await ctx.send(f"You added **{spell}** to the database!:thumbsup:")
    else:
        await ctx.send(f"**{spell.title()}** already exists in the database!")


bot.run(TOKEN)
