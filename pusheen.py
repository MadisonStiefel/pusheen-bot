import os
import discord
import random

from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()


bot = commands.Bot(command_prefix="p.", case_insensitive=True)
bot.remove_command('help')

TOKEN = os.environ.get("DISCORD_TOKEN")
COLOR = 0xFF85AA
MADO_USER_ID = 283695131738243084

# IDEAS
# -----------------
# option to disable reactions
# use to add custom reactions
# error handling for wrong commands + no input
# daily gif
# fun facts @ pusheen
# pusheen quizzes
# pusheen comics
# give pusheen gifts
# reply to anonymous message without knowing author (w capturing reactions?)
# categorize gifs and give options to users for categories
#    categories: Good Luck, Have a Good Day, Feel Better, Ur Cute
# add reactions https://unicode.org/emoji/charts/full-emoji-list.html
# p.help command_name for detailed help for each command
# add user option for p.hello and p.holiday

@bot.event
async def on_ready():
    print("Pusheen is connected to Discord!")

# add reactions
@bot.event
async def on_message(message):
    if message.author != bot.user and not (":" in message.content.lower()):
        if ("pusheen" in message.content.lower()):
            reactions = ['<:pusheen_heart:699356833793703958>']
            for emoji in reactions:
                await message.add_reaction(emoji)
        if ("sleep" in message.content.lower()):
            reactions = ['<:pusheen_sleep:699028704889929801>']
            for emoji in reactions:
                await message.add_reaction(emoji)
    await bot.process_commands(message)

# help command
@bot.command()
async def help(ctx, command=""):
    embed = discord.Embed(title="Commands Help", description="", color=COLOR)
    embed.add_field(name="\u200b", value="`p.about`\nreturns Pusheen's about page", inline=False)
    embed.add_field(name="\u200b", value="`p.hello`\nsays hello", inline=False)
    embed.add_field(name="\u200b", value="`p.birthday [user=None]`\nsays happy birthday", inline=False)
    #embed.add_field(name="\u200b", value="`p.message user_id`\nsends a random cute message", inline=False)
    embed.add_field(name="\u200b", value="`p.dm user`\nsends an anonymous random cute direct message", inline=False)
    embed.add_field(name="\u200b", value="`p.family [name=None]`\nreturns about pages of Pusheen's family", inline=False)
    embed.add_field(name="\u200b", value="`p.holiday holiday`\ncelebrates specified holiday", inline=False)
    embed.add_field(name="\u200b", value="`p.facts`\nreturns a fun fact about Pusheen", inline=False)
    embed.add_field(name="\u200b", value="`p.horoscope star_sign`\nreturns horoscope of a star sign", inline=False)
    embed.set_thumbnail(url="https://media.giphy.com/media/35OSzwCFjwZsAyVKkY/giphy.gif")
    embed.set_footer(text="Note: [arg_name=None] denotes an optional argument")
    await ctx.send(embed=embed)

# says hello
@bot.command(name="hello")
async def hello(ctx):
    embed = discord.Embed(title="Hi " + ctx.message.author.name + "! ❤️")
    embed.set_image(url="https://media.giphy.com/media/L3nWlmgyqCeU8/giphy.gif")

    await ctx.send(embed=embed)

# who is the mysterious kitty?
@bot.command(name="about", description="Who is Pusheen?", help="")
async def about(ctx):
    description = "Pusheen is a tubby tabby cat who brings smiles and laughter to people all around the world."

    embed = discord.Embed(title="About", description=description, color=COLOR)
    embed.add_field(name="Name", value="Pusheen", inline=False)
    embed.add_field(name="Gender", value="Girl", inline=False)
    embed.add_field(name="Age", value="All 9 lives left", inline=False)
    embed.add_field(name="Birthday", value="February 18th", inline=False)
    embed.add_field(name="Best Feature", value="Toes look like beans", inline=False)
    embed.set_image(url="https://pusheen.com/wp-content/themes/pusheen-custom/img/header-pusheen.gif")
    embed.set_thumbnail(url="https://media.giphy.com/media/dyq18nqPjqi2T8sRNf/giphy.gif")

    await ctx.send(embed=embed)

# happy birthday!
@bot.command(name="birthday", description="description", help="")
async def birthday(ctx, user:discord.User=None):
    # hbd text gif : https://i.imgur.com/RK0s2Yt.gif
    birthday_gifs = [
        "https://media.giphy.com/media/jxTnOS8Mkv8n6/giphy.gif",
        "https://media.giphy.com/media/6g564lKXZo796/giphy.gif",
        "https://media.giphy.com/media/PaZNTaXzCnnDG/giphy.gif",
        "https://media.giphy.com/media/jl7GmUfjGy3NC/giphy.gif"
    ]

    if user:
        embed = discord.Embed(title="Happy birthday, " + user.name + "! ❤️")
        embed.set_image(url=random.choice(birthday_gifs))
    else:
        embed = discord.Embed(title="Happy birthday! ❤️")
        embed.set_image(url=random.choice(birthday_gifs))

    await ctx.send(embed=embed)

# positive quotes
categories = []

cute = [
    ("Breaking news! You're super cute.", "https://i.pinimg.com/originals/81/1f/8c/811f8c608a796e041ae6ec12f27e20da.gif"),
    ("And the verdict is...cute! Undeniably cute!", "https://i.pinimg.com/originals/eb/d8/0b/ebd80b2ba5fb95a25ed15dbd94757b95.gif"),
    ("Guess what? You're a cutiepie!", "https://media1.tenor.com/images/035f033ebba7fae7019e543a81a81233/tenor.gif"),
    ("You're cute.", "https://i.pinimg.com/originals/df/de/0f/dfde0f26e3406860990e41b3b1026ab4.gif")
]

friendship = [
    ("We go together like two peas in a pod.", "https://media1.tenor.com/images/631ab0c52d83f0c26238ef9e912c6455/tenor.gif")
]

hugs = [
    ("Sending a penguin hug!", "https://i.pinimg.com/originals/9b/a0/c4/9ba0c49f6eca69622745c4ad35c843e0.gif"),
    ("You've got mail! Penguin hug!", "https://media1.tenor.com/images/92eab6ea538c75bc14249122ef44c6c3/tenor.gif")
]

love = [
    ("Sending you love!", "https://i.pinimg.com/originals/e0/3f/50/e03f5046bb67db6b8439c0ba37243196.gif"),
    ("All my love for you...", "https://media1.tenor.com/images/8cf2b503ad17768be12a861e6bfa731c/tenor.gif"),
    ("My undying love and support for you...", "https://media1.tenor.com/images/e4b4a917280808eee870d676295c616c/tenor.gif"),
    ("Loof ya!", "https://media1.tenor.com/images/12e03d45738fdf76dcf2f57260d852f3/tenor.gif"),
    ("Love you so much!", "https://media1.tenor.com/images/24ac72c718ccc7d1521c16860d8f4958/tenor.gif"),
    ("I love you!", "https://media1.tenor.com/images/a44f5627d5967c7b8d3ea9a0ddf51f4c/tenor.gif"),
    ("I love you!", "https://media1.tenor.com/images/4b9a7d60ef86ffca35faa7d0085bbe45/tenor.gif"),
    ("I love you!", "https://media1.tenor.com/images/ff929c5980833f1d9dcb0d065f984f61/tenor.gif")
]

motivational = [
    ("Motivational toast!", "https://i.pinimg.com/originals/db/3f/0f/db3f0fc003d6599f6537266671b398c5.gif"),
    ("You can do it!", "https://media1.tenor.com/images/e9666dd2054f80e0417d68d323f048df/tenor.gif"),
    ("You can do it!", "https://media1.tenor.com/images/da2c52f4d1cf4141b16d32d6fddbabc9/tenor.gif"),
    ("Good Luck Hamster", "https://media1.tenor.com/images/738f72314d8099f04b58510d6f78c4b3/tenor.gif")
]

uncategorized = [
    ("I'm really happy you're here.", "https://i.pinimg.com/originals/b6/5b/b4/b65bb49e3df537f610da508115b2b0b6.gif"),
    ("Be my Va-lint-ine?", "https://i.pinimg.com/originals/46/29/aa/4629aaddfb0db7abdbd06f16218c703a.gif"),
    ("Hey! You are awesome :)", "https://media1.tenor.com/images/1828c0b4c53065247cbb17e41e227629/tenor.gif"),
    ("Remember: You are pawsitively purrrrfect!", "https://media1.tenor.com/images/de2f0830342af9a280a99a3859868a9f/tenor.gif"),
    ("You are the beary best.", "https://media1.tenor.com/images/49ab0e73f6ce9dc8c616f378899a083d/tenor.gif"),
    ("It's a good day to be happy!", "https://i.pinimg.com/originals/06/64/44/0664447c4165c45c81fcaaba14c1bdd6.gif"),
    ("Penguin of the week", "https://i.pinimg.com/originals/f8/0e/a0/f80ea035bdd492f31533548b8e1a4ec7.gif"),
    ("Pocket hedgehog", "https://i.pinimg.com/originals/21/42/e0/2142e029f85f813a467ddb88c77d4ed7.gif")
]

supportive = []

quotes = cute + friendship + hugs + love + motivational + uncategorized + supportive
quotes = cute + hugs + motivational + uncategorized + supportive

# positive messages by Emm Roy + ChiiBird
'''
@bot.command(name="message", description="description", help="", pass_context=True)
async def message(ctx, user:discord.User):
    quote = random.choice(quotes)

    embed = discord.Embed(title="Hi, " + user.name + "!", description=quote[0])
    embed.set_image(url=quote[1])

    if user == ctx.message.author:
        embed.add_field(name="To:", value=ctx.message.author.mention)
        embed.add_field(name="From:", value="Pusheen <3")
    else:
        embed.add_field(name="To:", value=user.mention)
        embed.add_field(name="From:", value=ctx.message.author.mention)

    await ctx.send(embed=embed)
'''

# dm mado with da logs
async def mado(ctx, author:discord.User, recipient:discord.User):
    channel = await bot.get_user(MADO_USER_ID).create_dm()
    log_msg = author.name + " sent an anonymous message to " + recipient.name + "."
    await channel.send(log_msg)

# send an anonymous dm to another user via Pusheen
@bot.command(name="dm", description="description", help="", pass_context=True)
async def dm(ctx, user:discord.User):
    author = ctx.message.author
    quote = random.choice(quotes)

    embed = discord.Embed(title="Hi, " + user.name + "!", description="Someone wanted to send you this message! :D")
    embed.add_field(name="Description", value=quote[0])
    embed.set_image(url=quote[1])

    # sends embeded message to recipient
    channel = await user.create_dm()
    await channel.send(embed=embed)

    # sends copy of embeded message to author
    channel = await author.create_dm()
    await channel.send("The following message was sent to " + user.name + ".")
    await channel.send(embed=embed)

    # send logs to mado
    await mado(ctx, author, user)

# Pusheen's family
@bot.command(name="family")
async def family(ctx, name="none"):
    name = name.upper()

    if name == "STORMY":
        stormy_gifs = [
            "https://media1.giphy.com/media/TRKpNMh9CKG1a/giphy.gif",
            "https://media.giphy.com/media/LP6dGDluQqlpK/giphy.gif",
            "https://media.giphy.com/media/Dbon6L6Dnoa08/giphy.gif"
        ]
        stormy = discord.Embed(title="Stormy", description="Younger sister of Pusheen", color=COLOR)
        stormy.add_field(name="Birthday", value="October 24th")
        stormy.add_field(name="Gender", value="Female")
        stormy.add_field(name="Best Feature", value="My fluffy pants")
        stormy.add_field(name="Where I Live", value="With my family")
        stormy.add_field(name="Hobbies", value="Chasing things")
        stormy.add_field(name="Favorite Food", value="Kibbles & milk")
        stormy.add_field(name="Favorite Word", value="Wa wa")
        stormy.add_field(name="Dream", value="To grow up to be just like my sister, Pusheen")
        stormy.set_image(url=random.choice(stormy_gifs))
        await ctx.send(embed=stormy)
    elif name == "PIP":
        pip_gifs = [
            "https://media.giphy.com/media/82kXCTHlCZKb6ro4CA/giphy.gif",
            "https://media.giphy.com/media/1o1fMgTGbyvetAFW9b/giphy.gif",
            "https://media.giphy.com/media/1ZuN9z1foqAIUahKB8/giphy.gif"
        ]
        pip = discord.Embed(title="Pip", description="Younger brother of Pusheen", color=COLOR)
        pip.add_field(name="Birthday", value="June 24th")
        pip.add_field(name="Gender", value="Male")
        pip.add_field(name="Best Feature", value="My fur")
        pip.add_field(name="Where I Live", value="With my sisters")
        pip.add_field(name="Hobbies", value="Playing")
        pip.add_field(name="Favorite Food", value="All of them")
        pip.add_field(name="Favorite Word", value="Oh no")
        pip.add_field(name="Dream", value="Same as Pusheen's")
        pip.set_image(url=random.choice(pip_gifs))
        await ctx.send(embed=pip)
    elif name == "MOM":
        mom = discord.Embed(title="Mom", description="Mother of Pusheen", color=COLOR)
        mom.set_image(url="https://media.giphy.com/media/PMfqAVSoWeZ3y/giphy.gif")
        await ctx.send(embed=mom)
    elif name == "DAD":
        dad = discord.Embed(title="Dad", description="Father of Pusheen", color=COLOR)
        dad.set_image(url="https://media.giphy.com/media/IL6xVeyx77rRC/giphy.gif")
        await ctx.send(embed=dad)
    else:
        await ctx.send("Pusheen has four family members: Dad, Mom, Stormy, and Pip!\n"
        + "Type `p.family [name]` to find out more about each of them!\n"
        + "https://media.giphy.com/media/SV0UrYruj5E9Fa1Amp/giphy.gif")

# happy holidays!
# TODO: add user_id feature
@bot.command(name="holiday")
async def holiday(ctx, holiday="none"):
    holiday = holiday.upper()

    if holiday == "CHRISTMAS":
        message = "Merry Christmas!\n"
        christmas_gifs = [
            "https://tenor.com/view/christmas-cookies-pusheen-christmas-gif-7327534",
            "https://tenor.com/view/pusheen-christmas-gif-6107482",
            "https://tenor.com/view/pusheen-christmas-gif-7310734",
            "https://tenor.com/view/pusheen-christmas-tree-gif-7310740",
            "https://tenor.com/view/pusheen-christmas-gif-6107503",
            "https://tenor.com/view/pusheen-christmas-super-festive-gif-13038507",
            "https://tenor.com/view/pusheen-christmas-super-festive-gif-13038507",
            "https://tenor.com/view/christmas-pusheen-train-wreck-cat-gif-16009742",
            "https://tenor.com/view/merry-christmas-pusheen-gif-12893916",
            "https://tenor.com/view/merry-christmas-pusheen-gif-12893920",
            "https://tenor.com/view/pusheen-christmas-lights-merry-christmas-happy-xmas-christmas-tree-gif-10598678",
            "https://giphy.com/gifs/haven-minion-movie-josie-11P3ugnVUX03Ly"
        ]
        gif = random.choice(christmas_gifs)
    elif holiday == "EASTER":
        message = "Happy Easter!\n"
        easter_gifs = [
            "https://tenor.com/view/cute-easter-pusheen-happy-easter-gif-7819306",
            "https://giphy.com/gifs/easter-cat-pusheen-YwkcAa6l7uVQA",
            "https://giphy.com/gifs/bb75armJfgCHK"
        ]
        gif = random.choice(easter_gifs)
    elif holiday == "HALLOWEEN":
        message = "Happy Halloween!\n"
        halloween_gifs = [
            "https://giphy.com/gifs/halloween-holiday-pumpkin-7nRDHmVQ96Gly",
            "https://tenor.com/view/pusheen-halloween-cute-gif-12797108",
            "https://tenor.com/view/pumkins-cat-pusheen-halloween-gif-10874745",
            "https://tenor.com/view/spooky-halloween-pusheen-gif-13278175",
            "https://tenor.com/view/cat-happy-halloween-pusheen-gif-13278158",
            "https://tenor.com/view/pusheen-cat-halloween-gif-5947152",
            "https://tenor.com/view/pusheen-trex-angry-costume-halloween-gif-5087598",
            "https://giphy.com/gifs/cat-halloween-pusheen-WyAFMfpFSB6Bq",
            "https://tenor.com/view/pusheen-halloween-cats-gif-10019089"
        ]
        gif = random.choice(halloween_gifs)
    elif holiday == "THANKSGIVING":
        message = "Happy Thanksgiving!\n"
        thanksgiving_gifs = [
            "https://tenor.com/view/thanksgiving-pusheen-cat-gif-11670307",
            "https://tenor.com/view/thanksgiving-pusheen-thankful-for-you-gif-15444569",
            "https://tenor.com/view/thanksgiving-pusheen-gif-8723104"
        ]
        gif = random.choice(thanksgiving_gifs)
    else:
        await ctx.send("ERROR: No holiday specified")

    await ctx.send(message + gif)

# fun facts
@bot.command(name="facts")
async def facts(ctx):
    responses = [
        ("Pusheen's name is based upon the Irish word for kitten, puisín.",
        "https://tenor.com/view/irish-pusheen-stpatricksday-gif-5217392"),
        ("Stormy is the younger sister of Pusheen. She looks up to Pusheen and wants to be just like her. She is also fluffy and cute.",
        "https://tenor.com/view/pusheen-animated-pusheen-wanna-play-play-with-me-wake-up-gif-14765703"),
        ("Pusheen has two younger siblings: Stormy and Pip.",
        "https://media.giphy.com/media/3q3Sm0HP9BPHGLBOlh/giphy.gif")
    ]

    response = random.choice(responses)
    await ctx.send(response[0] + "\n" + response[1])

# horoscope
@bot.command(name="horoscope")
async def horoscope(ctx, star_sign="none"):
    star_sign = star_sign.upper()

    if star_sign == "ARIES":
        description = "Ambitious, independent, and energetic. Aries likes to lead the way and try new things – just don’t disagree with them!"
        gem = "Diamond"
        color = "Red"
        element = "Fire"
        likes = "Making new friends, loyalty, fun challenges"
        dislikes = "Boredom, being ignored, having to wait"
        best_feature = "Has the curliest horns"
        hobby = "Playing outside"
        words = "I do what I want!"
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Aries.gif"
    elif star_sign == "TAURUS":
        description = "Strong and dependable, yet stubborn. Taurus will always be there for you, but don’t try to change them!"
        gem = "Emerald"
        color = "Pink"
        element = "Earth"
        likes = "Food, beauty, music"
        dislikes = "Being rushed, being disturbed"
        best_feature = "Can carry all your luggage. Easily."
        hobby = "Sleeping under an 1800 thread count duvet."
        words = "There’s always room for dessert. Always."
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Taurus.gif"
    elif star_sign == "GEMINI":
        description = "Witty, chatty, and ever curious. Gemini always lands on their feet!"
        gem = "Tiger’s Eye & Emerald"
        color = "Yellow"
        element = "Air"
        likes = "Talking, playing tricks, novelty"
        dislikes = "Being bored, wasting time, being alone"
        best_feature = "Double the toe beans"
        hobby = "Bonding with their reflection"
        words = "Be your own best friend!"
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Gemini.gif"
    elif star_sign == "CANCER":
        description = "Helpful, sensitive, and caring. Cancer loves to protect and take care of their friends & family!"
        gem = "Ruby & Pearl"
        color = "Violet"
        element = "Water"
        likes = "Staying home, cooking/baking, comfort"
        dislikes = "Rudeness, being misunderstood"
        best_feature = "Always invited to ribbon-cutting ceremonies"
        hobby = "Hiding in the sand"
        words = "Why go out when you could just stay in?"
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Cancer.gif"
    elif star_sign == "LEO":
        description = "Fun-loving, proud, and the life of the party. Leo is a natural born leader and a friend for life, but don’t steal their thunder!"
        gem = "Carnelian"
        color = "Gold"
        element = "Fire"
        likes = "Grand gestures, being social, performing"
        dislikes = "Being one-upped, being ignored, laziness."
        best_feature = "A purrfectly manicured mane"
        hobby = "Basking under a warm spotlight"
        words = "There’s only two types of people in the world: Me…and everyone else"
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Leo.gif"
    elif star_sign == "VIRGO":
        description = "Organized, sophisticated, and kind. Virgo is the best friend who will always be there to give you good advice."
        gem = "Peridot"
        color = "Silver"
        element = "Earth"
        likes = "Planning, self care, small animals, to-do lists"
        dislikes = "Lateness, things being out of order, complaining"
        best_feature = "Knows which flowers are edible"
        hobby = "Digging holes in the garden"
        words = "Sharp claws, sharp mind, sharp dresser"
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Virgo.gif"
    elif star_sign == "LIBRA":
        description = "Trustworthy, fair, and charming. Libra is always ready to lend an ear and give advice!"
        gem = "Sapphire"
        color = "Blue"
        element = "Air"
        likes = "Harmony, loyalty, thank you notes"
        dislikes = "Mayhem, messes, criticism"
        best_feature = "Always knows how to balance their time"
        hobby = "Staring very intensely"
        words = "Be picky"
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Libra.gif"
    elif star_sign == "SCORPIO":
        description = "Authentic, intense, and loyal. Scorpio will be a friend for life, but watch out for that stinger!"
        gem = "Topaz & Opal"
        color = "Black"
        element = "Water"
        likes = "Mysteries, being right, winning"
        dislikes = "Strangers, know-it-alls"
        best_feature = "All of them, not to put too fine a point on it"
        hobby = "Sashaying up and down the catwalk"
        words = "Trust no one… (except me, you can trust me)"
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Scorpio.gif"
    elif star_sign == "SAGITTARIUS":
        description = "Adventurous, driven, and creative. Sagittarius loves to travel and party!"
        gem = "Topaz"
        color = "Light Blue"
        element = "Fire"
        likes = "Adventure, traveling, parties"
        dislikes = "Being held back, the same old routine, sitting still"
        best_feature = "Half majesty, half precision"
        hobby = "Laser hunting"
        words = "Travel, eat, party, repeat"
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Sagittarius.gif"
    elif star_sign == "CAPRICORN":
        description = "Hard-working, focused, and driven. Capricorn means business!"
        gem = "Lapis Lazuli"
        color = "Dark Blue"
        element = "Earth"
        likes = "Perfectly organized spreadsheets, freshly swept floors"
        dislikes = "Mess, laziness"
        best_feature = "Can swim and eat at the same time"
        hobby = "Swimming and eating"
        words = "Always be one step ahead!"
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Capricorn.gif"
    elif star_sign == "AQUARIUS":
        description = "Problem-solver, humanitarian, and independent. Aquarius has it figured out!"
        gem = "Turquoise"
        color = "Turquoise"
        element = "Air"
        likes = "Real adventurers, being reasonable, a good story"
        dislikes = "Being bored, people who knock over their water jug"
        best_feature = "Always stays hydrated"
        hobby = "Knocking over flower vases"
        words = "Listen, I’ve got a plan"
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Aquarius.gif"
    elif star_sign == "PISCES":
        description = "Caring, thoughtful, a good friend to the end!"
        gem = "Moonstone"
        color = "Sea Green, Aqua"
        element = "Water"
        likes = "Big gatherings, parties, group-texts"
        dislikes = "Disorder, lies, sharks"
        best_feature = "Never thirsty"
        hobby = "Daydreaming about fancy snacks"
        words = "You know I’ve got your back!"
        gif = "https://pusheen.com/wp-content/uploads/2019/01/Pisces.gif"
    else:
        await ctx.send("ERROR: No star sign specified")

    embed = discord.Embed(title=star_sign, description=description, color=COLOR)
    embed.add_field(name="Lucky Gem", value=gem)
    embed.add_field(name="Lucky Color", value=color)
    embed.add_field(name="Element", value=element)
    embed.add_field(name="Likes", value=likes)
    embed.add_field(name="Dislikes", value=dislikes)
    embed.add_field(name="Best Feature", value=best_feature)
    embed.add_field(name="Words to Live By", value=words)
    embed.set_image(url=gif)

    await ctx.send(embed=embed)

bot.run(TOKEN)
