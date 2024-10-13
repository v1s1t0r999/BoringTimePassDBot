# #fr

# import discord
# import ShitDB
# import asyncio
# from discord.ext import commands, tasks
# import os

# class Env:
# 	def __init__(self):
# 		self.prefix = ["-"] # multiple prefixes?? Eww
# 		self.github_token = os.getenv("gtk") # How-To?: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
# 		self.github_repo = os.getenv("repo")
# 		self.github_email = os.getenv("ghemail")
# 		self.github_username = os.getenv("ghusername")
# 		self.intents = discord.Intents.all() # Or whatever you want
# 		self.token = os.getenv("dtk") # Don't as how....or gtfo


# env = Env()

# bot = commands.Bot(command_prefix = env.prefix, intents = env.intents, strip_after_prefix=True)

# db = ShitDB.AsyncDB(
# 	github_token = env.github_token,
# 	database_repo = env.github_repo,
# 	author = (env.github_username, env.github_email)
# )



# @bot.event
# async def on_ready():
# 	print(f"""
# 	=========
# 	BOT: {bot.user}
# 	ID: {bot.id}
# 	SERVERS: {len(bot.guilds)}
# 	=========
	
# 	[+] CONNECTED TO DISCORD!
	
# 	=========
# 	""")



# @bot.event
# async def on_message(ctx):
# 	all_levels = await db.load_remote_data("level.json", eval_output = True) # see: https://v1s1t0r999.github.io/ShitDB/usage#fetching-data | for why eval_output=True
	
# 	user_data = all_levels.get(ctx.author.id)                                # Get the user's data
	
# 	if user_data is None:                                                    # It means the bot is meeting the user for the first time
# 		all_levels.update(
# 			{
# 				ctx.author.id:{"msg":0,"lvl":0,"mul":1}		# mul param is the multiplier
# 			}
# 		)       						         # Make a new data for the user with everything as 0 (start)
# 		user_data = all_levels.get(ctx.author.id)                            # {"msgs":0,"lvl":0}
# 	user_data['msg']+=1                                                     # Increment the number of messages for the user
	
# 	if user_data['msg']>=(10*user_data['mul']):                             # If the nuber of messages is more than 10, goes to next level
# 		user_data['lvl']+=1
# 		user_data['msg']=0
# 		user_data['mul']+=1
# 		await ctx.send(f"Bruh!! **{ctx.author}** just levelled up to level: {user_data['lvl']} WTF! ||{user_data['mul']*10} mesages for level {user_data['lvl']}!!||")
# 	all_levels[ctx.author.id] = user_data                                    # Add the user's info to the main data
# 	await db.push_remote_data(content=all_levels, file_path="levels.json")   # Push it using: ShitDB.AsyncDB.push_remote_data()
# 	return await bot.process_commands(ctx)




# @bot.command(help="Check your fucking rank smh!",aliases=["lvl","level"])
# async def rank(ctx,user=None):
# 	if not user:
# 		user=ctx.author
# 	all_data = await db.load_remote_data("level.json", eval_output=True)
# 	user_data = all_data.get(user.id)
# 	if user_data is None:
# 		all_levels.update({user.id:{"msg":0,"lvl":0,"mul":1}})
# 		return await ctx.send(f"User {user} just got registered in the db. Am I meeting him/her/||da gae|| for the first time??")
# 	return await ctx.send(embed=discord.Embed(
# 		description = f"""\
# 		{user.mention}?? Ooo
# 		Level: {user_data["lvl"]}
# 		Needs more `{user_data["mul"]*10-user_data["msg"]}` messages for level {user_data["lvl"]+1}!!
# 		"""))




# @bot.command(help="Set a rainbow role?")
# async def rainbow(ctx,role:discord.Role=None):
# 	if role is None:
# 		role = ctx.guild.create_role(name="Rainbow Perm!")
# 	if not isinstance(role,discord.Role):
# 		return await ctx.send("Mention an existing role stupid!")
# 	all_guilds = await db.load_remote_data("rainbow.json", eval_output=True)
# 	try:
# 		r = discord.utils.get(ctx.guild.roles, id=all_guilds[ctx.guild.id]["roleid"])
# 		await ctx.send(embed=discord.Embed(description=f"{r.mention} is already a rainbow role!!\nSend `1` to change; `2` for nvm"))
# 		try:
# 			msg = await bot.wait_for("message",check=chk,timeout=20.0)
# 			if msg.content.lower()=="1":
# 				await ctx.send("Ok! passed!")
# 				pass
# 			else:
# 				return await ctx.send("Nvm!")
# 		except asyncio.TimeoutError:
# 			return await ctx.send(f"You didnt reply in time stupido!")
# 	except:
# 		await ctx.send(f"Eh? smth happend!")
# 	all_guilds.update({ctx.guild.id:{"roleid":role.id,"name":role.name}})
# 	await db.push_remote_data(content=all_guilds, file_path="rainbow.json")
# 	await ctx.send(embed=discord.Embed(description=f"{role.mention} is now a Rainbow role. It will change its colour in every 5 minutes!"))


# @tasks.loop(minutes=5.0)
# async def rainbow_task():
# 	all_guilds = await db.load_remote_data("rainbow.json", eval_output=True) # {"guild1":{"roleid":1234,"name":"R.R"},"guild2":{"roleid":6789,"n":"rainbow!"}}
# 	guild_list = list(all_guilds) # [guild1,guild2]
# 	for g in guild_list:
# 		# g = guild1 and guild2
# 		# all_guilds["guild1" or g]["roleid"] = rainbow role id
# 		r = discord.utils.get(g.roles, id=all_guilds[g]["roleid"])
# 		await r.edit(colour=discord.Colour.random())




# if __name__=="__main__":
# 	bot.run(env.token)
##################################################################################################################################################
# from discord.ext import commands
# from discord import Intents
# import os

# prefix = "?"
# bot = commands.Bot(command_prefix=prefix, intents=Intents.all())


# @bot.event
# async def on_ready():
#     print("Everything's all ready to go~")


# # @bot.event
# # async def on_message(message):
# #     print("The message's content was", message.content)
# #     await bot.process_commands(message)


# @bot.command()
# async def ping(ctx):
#     '''
#     This text will be shown in the help command
#     '''

#     # Get the latency of the bot
#     latency = bot.latency  # Included in the Discord.py library
#     # Send it to the user
#     await ctx.send(latency)


# @bot.command()
# async def echo(ctx, *, content:str):
#     await ctx.send(content)


# bot.run(os.getenv("dtk"))  # Where 'TOKEN' is your bot token



import discord
import os

prefix="-"
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.lower().startswith(f'{prefix}'):
		cmd = msg.content.replace(prefix,"").lower()
		channel = msg.channel
		if cmd=="hello":
			await channel.send('Hello!')
		if cmd=="yo":
			await channel.send("yooooo")
		if cmd.startswith("rp"):
			say = cmd.replace("rp","")
			await channel.send(say)
		else:
			await message.channel.send("BOZOOOOOOOO")

client.run(os.getenv("dtk"))
