import discord
import praw

redditCredentials = [line.rstrip('\n') for line in open('reddit.token')]
discordCredentials = [line.rstrip('\n') for line in open('discord.token')]
client = discord.Client()

reddit = praw.Reddit(client_id = redditCredentials[0],
                     client_secret = redditCredentials[1],
                     username = redditCredentials[2],
                     password = redditCredentials[3],
                     user_agent = redditCredentials[4])

token = discordCredentials[0]

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    raw_msg = message.content.lower()
    split_msg = raw_msg.split()

    if split_msg[0] == "!m":
        if len(split_msg) > 1:

            if split_msg[1] == "hi":
                await message.channel.send(f"Hello fellow gamers.")

            elif split_msg[1] == "load":
                if len(split_msg) > 2:
                    urls = f""
                    subreddit = reddit.subreddit(split_msg[2])
                    hot_subreddit = subreddit.hot(limit=10)
                    for submission in hot_subreddit:
                        if not submission.stickied:
                            urls += submission.url + "\n"
                    await message.channel.send(urls)
                else:
                    await message.channel.send(f'You look like you need some help. Consult Jerry.')

            else:
                await message.channel.send(f"You look like you need some help. Consult Jerry.")
        else:
            await message.channel.send(f"You look like you need some help. Consult Jerry.")

client.run(token)
