import discord
from discord.ext import commands
import random
from main import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
@bot.command()
async def ia(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            name=attachment.filename
            url=attachment.url
            await attachment.save(f"./{attachment.filename}")
            result = get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}")
            if result:
                await ctx.send(result)
            else:
                await ctx.send("No se pudo clasificar la imagen.")
    else:
        await ctx.send("weeeeeeeeeey pasa foto ")
        await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def suma(ctx,numero1 :int, numero2 :int):
    await ctx.send(f"{numero1+numero2}")

@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)

@bot.command()
async def lanzardado(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

bot.run("MTM5MDExMDkyOTQyNTAxMDgzOQ.G5hdGu.ncnHLYaCG0LEpKbZzwFvgs42LIYlDbN2uOQrs4")
