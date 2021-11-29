import discord
import os
import openpyxl 
import parsivar 
client = discord.Client()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$help'):
        text="In the first line, you have to write the language that is your input word and the language that you want to be your output like this: \n en fr \n In the second line, you must write the sentence you want to translate like this: \n hi world"
        await message.channel.send(text)

    elif message.content.startswith('$'):
        my_string=message.content
        first = my_string.split('\n', 1)[0]
        second_line = my_string.split('\n', 1)[1]
        if first=="$Finglish":
            from parsivar import Normalizer
            my_normalizer = Normalizer(pinglish_conversion_needed=True)
            out_text=(my_normalizer.normalize(second_line))
        await message.channel.send(out_text)

client.run(TOKEN)
