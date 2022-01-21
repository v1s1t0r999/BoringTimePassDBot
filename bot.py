

import discord
import ShitDB
from discord.ext import commands
from modules import global_variables as env



bot = commands.Bot(command_prefix = env.prefix, intents = env.intents)

db = ShitDB.AsyncDB(
	github_token = env.github_token,
	database_repo = env.github_repo,
	author = (env.github_username, env.github_email)
)


@bot.event
async def on_ready():
	print(f"""
	=========
	BOT: {bot.user}
	ID: {bot.id}
	SERVERS: {len(bot.guilds)}
	=========
	
	[+] CONNECTED TO DISCORD!
	
	=========
	""")

	

@bot.event
async def on_message(ctx):
	all_levels = await db.load_remote_data("level.json", eval_output = True) # see: https://v1s1t0r999.github.io/ShitDB/usage#fetching-data | for why eval_output=True
	
	user_data = all_levels.get(ctx.author.id)                                # Get the user's data
	
	if user_data is None:                                                    # It means the bot is meeting the user for the first time
		all_levels.update({ctx.author.id:{"msgs":0,"lvl":0}})                # Make a new data for the user with everything as 0 (start)
		user_data = all_levels.get(ctx.author.id)                            # {"msgs":0,"lvl":0}
	user_data['msgs']+=1                                                     # Increment the number of messages for the user
	
	if user_data['msgs']>=10:                                                # If the nuber of messages is more than 10, goes to next level
		user_data['lvl']+=1
		user_data['msgs']=0
	all_levels[ctx.author.id] = user_data                                    # Add the user's info to the main data
	
	await db.push_remote_data(content=all_levels, file_path="levels.json")   # Push it using: ShitDB.AsyncDB.push_remote_data()
	await bot.process_commands(ctx)

	
	
	
bot.run(env.token)
	
