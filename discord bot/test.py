#https://discordapp.com/oauth2/authorize?client_id=601962388006109195&scope=bot&permissions=67648
#601962388006109195

import discord

client = discord.Client()
token = open("token.txt","r").read()


@client.event  # event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    await client.wait_until_ready()
    sentdex_guild = client.get_guild('601962388006109195')

    if "sentdebot.member_count()" == message.content.lower():
        await message.channel.send(f"```py\n{sentdex_guild.member_count}```")

    elif "sentdebot.logout()" == message.content.lower():
        await client.close()

    elif "sentdebot.community_report()" == message.content.lower():
        online = 0
        idle = 0
        offline = 0

        for m in sentdex_guild.members:
            if str(m.status) == "online":
                online += 1
            if str(m.status) == "offline":
                offline += 1
            else:
                idle += 1

        await message.channel.send(f"```Online: {online}.\nIdle/busy/dnd: {idle}.\nOffline: {offline}```")


client.run(token)
