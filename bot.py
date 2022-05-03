import os
import random

from discord.ext import commands
from discord.ext.commands import has_permissions
from dotenv import load_dotenv
from utils import get_weapons, save_new_weapons, get_spellcard, save_new_spellcard

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
help_command = commands.DefaultHelpCommand(no_category='Commands', indent=4)
bot = commands.Bot(command_prefix='!', help_command=help_command)


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99', hidden=True)
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'Cool. Cool cool cool cool cool cool cool, \nno doubt no doubt no doubt no doubt.'
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='roll', aliases=['r'], help='Simulates rolling dice.')
async def roll(ctx, roll_input):
    d = roll_input.find('d')
    number_dice = int(roll_input[:d])
    number_sides = int(roll_input[d + 1:])
    dice = [
        str(random.choice(range(1, number_sides + 1)))
        for _ in range(number_dice)
    ]
    await ctx.send('  '.join(dice))


@bot.command(name='damage', aliases=['dmg'], help='Tells you the damage of the weapon')
async def damage(ctx, *args):
    weapon = '_'.join(args)
    if weapon is None:
        damage_res = "A lot of damage! (You need to tell me the weapon! :person_facepalming:)"
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
    else:
        spell_res = get_spellcard(spell)
    if spell_res is None:
        spell_res = f"I do not know! ({spell} is not a spell! :person_shrugging:)"

    await ctx.send(spell_res)


@bot.command(name='features', aliases=['feat'], help='Tells you, what the feature is doing')
async def features():
    pass


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
